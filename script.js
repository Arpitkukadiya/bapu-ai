async function ask() {
  const question = document.getElementById("question").value;
  const res = await fetch("/api/jarvis", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });
  const data = await res.json();
  document.getElementById("answer").innerText = data.answer;
  document.getElementById("suggestions").innerHTML =
    "<p><strong>Related Questions:</strong></p><ul>" +
    data.suggestions.map((q) => `<li>${q}</li>`).join("") +
    "</ul>";
}