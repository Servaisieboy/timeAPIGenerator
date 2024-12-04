
document.getElementById("city-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const city = document.getElementById("city").value;
    const timezone = document.getElementById("timezone").value;

    const responseDiv = document.getElementById("response");

    try {
        const response = await fetch("/api/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ city, timezone })
        });

        const result = await response.json();
        if (response.ok) {
            responseDiv.innerHTML = `<p>Success! Your API is available at <strong>${result.message}</strong></p>`;
        } else {
            responseDiv.innerHTML = `<p>Error: ${result.error}</p>`;
        }
    } catch (err) {
        responseDiv.innerHTML = `<p>Error: Unable to create API.</p>`;
    }
});
