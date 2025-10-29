const chartData = platforms
  .filter((platform) => platform.impactPercentage !== null && platform.impactPercentage >= 0)
  .map((platform, index) => ({
    name: platform.shortName,
    percentage:
      typeof platform.impactPercentage === "number"
        ? platform.impactPercentage
        : 0,
    color: platformColors[index % platformColors.length].color,
    textColor:
      platformColors[index % platformColors.length].textColor as "white" | "dark",
  }));




















