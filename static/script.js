function analyzeJob() {
    const jobText = document.getElementById("jobText").value.trim();
    const resultDiv = document.getElementById("result");
    const button = document.querySelector("button");

    if (!jobText) {
        resultDiv.innerHTML = `<p style="color:red;">⚠️ Please enter a job description first.</p>`;
        return;
    }

    // Show loading
    button.disabled = true;
    button.textContent = "Analyzing...";
    resultDiv.innerHTML = `<p>🔍 Analyzing job posting...</p>`;

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: jobText })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = `<p style="color:red;">⚠️ ${data.error}</p>`;
        } else {
            const color = data.prediction === "Fake" ? "#e74c3c" : "#27ae60";
            const icon = data.prediction === "Fake" ? "🚨" : "✅";
            resultDiv.innerHTML = `
                <div style="border: 2px solid ${color}; border-radius: 8px; padding: 15px; margin-top: 10px;">
                    <h3 style="color:${color};">${icon} ${data.prediction} Job Posting</h3>
                    <p>Confidence: <strong>${data.confidence}%</strong></p>
                </div>`;
        }
    })
    .catch(() => {
        resultDiv.innerHTML = `<p style="color:red;">❌ Something went wrong. Please try again.</p>`;
    })
    .finally(() => {
        button.disabled = false;
        button.textContent = "Check Authenticity";
    });
}