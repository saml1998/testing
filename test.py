// Load Platforms when page mounts
useEffect(() => {
  fetch("http://127.0.0.1:8000/mapping/platforms")
    .then((res) => res.json())
    .then((data) => {
      setPlatforms(data);
      console.log("Loaded Platforms:", data);
    })
    .catch((err) => console.error("Error fetching platforms:", err));
}, []);

// Load Practices when Platform selected
useEffect(() => {
  if (selectedPlatform) {
    fetch(`http://127.0.0.1:8000/mapping/practices/${selectedPlatform}`)
      .then((res) => res.json())
      .then((data) => {
        setPractices(data);
        console.log("Loaded Practices:", data);
      })
      .catch((err) => console.error("Error fetching practices:", err));
  } else {
    setPractices([]);
    setOfferings([]);
  }
}, [selectedPlatform]);

// Load Offerings when Practice selected
useEffect(() => {
  if (selectedPlatform && selectedPractice) {
    fetch(
      `http://127.0.0.1:8000/mapping/offerings/${selectedPlatform}/${selectedPractice}`
    )
      .then((res) => res.json())
      .then((data) => {
        setOfferings(data);
        console.log("Loaded Offerings:", data);
      })
      .catch((err) => console.error("Error fetching offerings:", err));
  } else {
    setOfferings([]);
  }
}, [selectedPractice]);
