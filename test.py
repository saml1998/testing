<div className="p-6 space-y-6">

  {/* ===== Dropdown Filters Section ===== */}
  <div style={{ display: "flex", gap: "1rem", marginBottom: "1.5rem" }}>
    
    {/* Platform Dropdown */}
    <div>
      <label style={{ fontWeight: "bold", marginRight: "0.5rem" }}>Platform:</label>
      <select
        value={selectedPlatform}
        onChange={(e) => setSelectedPlatform(e.target.value)}
      >
        <option value="">-- Select Platform --</option>
        {platforms.map((p) => (
          <option key={p.platform_code} value={p.platform_code}>
            {p.platform_name}
          </option>
        ))}
      </select>
    </div>

    {/* Practice Dropdown */}
    <div>
      <label style={{ fontWeight: "bold", marginRight: "0.5rem" }}>Practice:</label>
      <select
        value={selectedPractice}
        onChange={(e) => setSelectedPractice(e.target.value)}
        disabled={!selectedPlatform}
      >
        <option value="">-- Select Practice --</option>
        {practices.map((pr) => (
          <option key={pr.practice_code} value={pr.practice_code}>
            {pr.practice_name}
          </option>
        ))}
      </select>
    </div>

    {/* Offering Dropdown */}
    <div>
      <label style={{ fontWeight: "bold", marginRight: "0.5rem" }}>Offering:</label>
      <select disabled={!selectedPractice}>
        <option value="">-- Select Offering --</option>
        {offerings.map((o) => (
          <option key={o.offering_code} value={o.offering_code}>
            {o.offering_name}
          </option>
        ))}
      </select>
    </div>

  </div>
  {/* ===== End of Dropdown Filters Section ===== */}

  {/* Existing Dashboard Components Below */}
  <AIAssetReportHeader />
  <AdvisorySummary />
  <MainMetricsCards />
  <ImpactByPlatform platforms={platformsData} isLoading={isPlatformsLoading} />
  <PlatformRankingsTable data={platformsData} isLoading={isPlatformsLoading} />
</div>
