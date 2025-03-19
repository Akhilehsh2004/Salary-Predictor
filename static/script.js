document.getElementById("predictForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let experience = document.getElementById("experience").value;

    fetch('/predict', {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `experience=${experience}`
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").textContent = data.salary || "Error: " + data.error;
        })
        .catch(error => console.error("Error:", error));
});
