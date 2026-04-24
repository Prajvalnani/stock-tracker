const API = "https://stock-tracker-production-7037.up.railway.app/"; // replace later

async function loadMovers() {
  const res = await fetch(`${API}/stocks/movers`);
  const data = await res.json();

  const app = document.getElementById("app");

  app.innerHTML = `
    <h1>📈 Market Movers</h1>
    <pre>${JSON.stringify(data, null, 2)}</pre>
  `;
}

loadMovers();
