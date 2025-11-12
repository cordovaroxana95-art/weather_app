import React, { useState } from "react";

export default function WeatherApp() {
  const [city, setCity] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSearch() {
    if (!city.trim()) {
      setError("⚠️ Ingresa una ciudad válida.");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch(
        `http://localhost:8000/weather?city=${encodeURIComponent(city)}`
      );

      if (!response.ok) throw new Error("No se pudo obtener el clima.");

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col items-center p-8 space-y-6 max-w-lg mx-auto">
      <h1 className="text-3xl font-bold text-blue-700">🌍 WeatherApp Global</h1>

      <input
        type="text"
        className="w-full p-3 rounded-2xl shadow border"
        placeholder="Ingresa una ciudad (Ej. Madrid, Tokyo)"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />

      <button
        onClick={handleSearch}
        className="px-6 py-3 rounded-2xl shadow bg-blue-600 text-white hover:bg-blue-700 transition"
      >
        Buscar Clima
      </button>

      {loading && <p>Cargando...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {result && (
        <div className="p-6 rounded-2xl shadow bg-white w-full text-left space-y-2">
          <h2 className="text-xl font-semibold">🌦️ Resultados</h2>
          <p>📍 Ciudad: {result.city}</p>
          <p>🌡️ Temperatura: {result.temp_c} °C</p>
          <p>🔥 Fahrenheit: {result.temp_f} °F</p>
          <p>💨 Viento: {result.wind} km/h</p>
          <p>☁️ Código del clima: {result.code}</p>
        </div>
      )}
    </div>
  );
}