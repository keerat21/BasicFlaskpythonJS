const processBtn = document.getElementById("process-btn");
const inputText = document.getElementById("input-text");
const inputText2 = document.getElementById("input-text2");
const processedText = document.getElementById("processed-text");

processBtn.addEventListener("click", async () => {
  const text = inputText.value;
  const text2 = inputText2.value;
  const response = await fetch("http://localhost:8080/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({text: [text, text2]})
  })
    .then(response => response.json())
    .then(data => {
      processedText.textContent = data.result.sentiment.label;
    })
    .catch(error => {
      console.error("Error during AJAX request:", error);
    });
});
