{/* Practice Dropdown */}
<div className="bg-neutral-100 rounded-lg p-4 mb-6">
  <label className="block text-sm font-medium text-gray-600 mb-2">
    Select Practice
  </label>
  <select
    value={selectedPractice}
    onChange={(e) => setSelectedPractice(e.target.value)}
    className="w-full p-2 border border-gray-300 rounded-md text-sm"
  >
    <option value="All Practices">All Practices</option>
    {platform?.platform && platformPractices[platform.platform]?.map((practice) => (
      <option key={practice} value={practice}>{practice}</option>
    ))}
  </select>
</div>
