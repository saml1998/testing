"use client";

import { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Spinner } from "@/components/ui/spinner";

// backend model type
interface Platform {
  platform_code: string;
  platform_name: string;
  practice_code?: string;
  practice_name?: string;
  offering_code?: string;
  offering_name?: string;
  impact_percentage?: number;
  revenue?: number;
}

interface PlatformChartData {
  name: string;
  percentage: number;
  color: string;
  textColor: "white" | "dark";
}

interface ImpactByPlatformProps {
  platforms?: Platform[];
  isLoading?: boolean;
}

export function ImpactByPlatform({
  platforms = [],
  isLoading = false,
}: ImpactByPlatformProps) {
  const [platformChartData, setPlatformChartData] = useState<PlatformChartData[]>([]);
  const [totalRevenue, setTotalRevenue] = useState<number>(0);
  const [revenuePerHead, setRevenuePerHead] = useState<number>(0);

  const platformColors = [
    { color: "#C1400A", textColor: "white" },
    { color: "#E74906", textColor: "white" },
    { color: "#FE7C39", textColor: "white" },
    { color: "#FF8C42", textColor: "white" },
    { color: "#FFAA72", textColor: "dark" },
    { color: "#FFCDA8", textColor: "dark" },
    { color: "#FFF2E6", textColor: "dark" },
    { color: "#FFE8D4", textColor: "dark" },
  ];

  // 🔹 Transform backend platforms into chart-ready data
  useEffect(() => {
    if (!platforms || platforms.length === 0) return;

    // Calculate total revenue
    const total = platforms.reduce((sum, p) => sum + (p.revenue ?? 0), 0);
    setTotalRevenue(total);

    // Calculate revenue per head (example: total/employee_count, if available)
    const perHead = platforms.length > 0 ? total / platforms.length : 0;
    setRevenuePerHead(perHead);

    // Use impact_percentage or derive percentage share by revenue
    const chartData = platforms
      .map((p, index) => {
        const percentage =
          p.impact_percentage ??
          (total > 0 ? Math.round(((p.revenue ?? 0) / total) * 100) : 0);

        return {
          name: p.platform_name,
          percentage,
          color: platformColors[index % platformColors.length].color,
          textColor: platformColors[index % platformColors.length]
            .textColor as "white" | "dark",
        };
      })
      .filter((p) => p.percentage > 0);

    setPlatformChartData(chartData);
  }, [platforms]);

  return (
    <div className="space-y-4">
      <Card className="py-8 rounded-2xl shadow-[0px_2px_4px_-2px_rgba(71,71,71,0.24)] border border-black/20 bg-[rgba(255,255,255,.1)]">
        <CardContent>
          {isLoading ? (
            <div className="flex items-center justify-center h-48">
              <Spinner size="lg" />
            </div>
          ) : (
            <>
              <div className="flex items-center justify-between mb-6">
                <h2
                  style={{
                    fontFamily: "Helvetica Neue, Arial, sans-serif",
                    fontWeight: 500,
                    fontSize: "24px",
                    color: "#252525",
                  }}
                >
                  Impact by Platform
                </h2>
              </div>

              {/* ===== Bar Visualization ===== */}
              <div className="flex flex-col lg:flex-row gap-6">
                <div className="w-full lg:w-[65%]">
                  <div className="flex items-center gap-2 mb-4">
                    <div className="w-full h-10 flex gap-1">
                      {platformChartData.map((platform, index) => (
                        <div
                          key={index}
                          className="rounded-2xl flex items-center justify-end pr-2 relative"
                          style={{
                            width: `${platform.percentage}%`,
                            backgroundColor: platform.color,
                          }}
                        >
                          <span
                            className={`text-xs font-bold ${
                              platform.textColor === "white"
                                ? "text-white"
                                : "text-zinc-700"
                            }`}
                          >
                            {platform.percentage}%
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Legend */}
                  <div className="flex flex-wrap gap-2 text-xs">
                    {platformChartData.map((platform, index) => (
                      <div
                        key={index}
                        className="px-2 py-1 bg-white rounded-sm outline outline-1 outline-offset-[-1px] outline-zinc-200 inline-flex justify-center items-center gap-2.5"
                      >
                        <div>
                          <svg
                            width="8"
                            height="9"
                            viewBox="0 0 8 9"
                            fill="none"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <circle cx="4" cy="4.5" r="4" fill={platform.color} />
                          </svg>
                        </div>
                        <div className="text-center justify-center text-zinc-700 text-xs font-normal leading-normal">
                          {platform.name}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* ===== Stats (Revenue) Section ===== */}
                <div className="w-full lg:w-[35%] flex justify-center">
                  <div
                    className="w-1/2 text-center"
                    style={{ borderRight: "1px solid #CBD1D6" }}
                  >
                    <div
                      className="font-normal text-[rgba(105,105,105,1)] text-sm"
                      style={{ fontFamily: "Helvetica Neue, Arial, sans-serif" }}
                    >
                      Total Revenue
                    </div>
                    <div
                      className="text-4xl font-light text-[rgba(37,37,37,1)]"
                      style={{ fontFamily: "Helvetica Neue, Arial, sans-serif" }}
                    >
                      {totalRevenue.toLocaleString("en-US", {
                        style: "currency",
                        currency: "USD",
                        notation: "compact",
                      })}
                    </div>
                  </div>

                  <div className="w-1/2 text-center">
                    <div
                      className="text-[rgba(105,105,105,1)] text-sm"
                      style={{ fontFamily: "Helvetica Neue, Arial, sans-serif" }}
                    >
                      Revenue per Head
                    </div>
                    <div
                      className="text-4xl font-light text-[rgba(37,37,37,1)]"
                      style={{ fontFamily: "Helvetica Neue, Arial, sans-serif" }}
                    >
                      {revenuePerHead.toLocaleString("en-US", {
                        style: "currency",
                        currency: "USD",
                        notation: "compact",
                      })}
                    </div>
                  </div>
                </div>
              </div>
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
