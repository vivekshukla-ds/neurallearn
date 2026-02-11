"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [data, setData] = useState<any>({
    hero_title: "Loading...",
    hero_subtitle: "Connecting to backend...",
  });

  useEffect(() => {
    const loadConfig = async () => {
      try {
        const res = await fetch("http://localhost:8000/config");
        const json = await res.json();
        setData(json);
      } catch (err) {
        console.error("Fetch error:", err);
        setData({
          hero_title: "Backend not reachable",
          hero_subtitle: "Check backend terminal",
        });
      }
    };

    loadConfig();
  }, []);

  return (
    <main style={{ padding: "60px", fontFamily: "sans-serif" }}>
      <h1 style={{ fontSize: "36px", fontWeight: "bold" }}>
        {data.hero_title}
      </h1>
      <p style={{ marginTop: "16px", fontSize: "18px" }}>
        {data.hero_subtitle}
      </p>
    </main>
  );
}
