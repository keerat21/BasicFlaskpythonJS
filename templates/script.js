const processBtn = document.getElementById("process-btn");
const inputText = document.getElementById("input-text");
const inputText2 = document.getElementById("input-text2");
const processedText = document.getElementById("processed-text");

processBtn.addEventListener("click", async () => {
  const text = inputText.value;
  const text2 = inputText2.value;

  // Create an object with both text inputs
  const data = {
    text: text,
    text2: text2
  };

  const response = await fetch("http://localhost:8080/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data) // Send the data object as JSON
  })
    .then(response => response.json())
    .then(data => {
      processedText.textContent = data.result.sentiment.label;
    })
    .catch(error => {
      console.error("Error during AJAX request:", error);
    });
});
