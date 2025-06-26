document.getElementById("predict-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = {};

    // Convert form values to numbers
    for (let [key, value] of formData.entries()) {
        data[key] = parseFloat(value);
    }

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        const resultBox = document.getElementById("result-box");
        const resultText = document.getElementById("result");

        if (result.prediction !== undefined) {
            resultText.innerText = "Prediction: " + result.prediction;
        } else {
            resultText.innerText = "Error: No prediction returned.";
        }

        // Show result box
        resultBox.style.display = "block";

    } catch (error) {
        console.error("Fetch error:", error);
        const resultBox = document.getElementById("result-box");
        resultBox.style.display = "block";
        document.getElementById("result").innerText = "Error: API request failed.";
    }
});
