// слухачі подій
document.querySelector("button").addEventListener("click", sendMessage);
document.getElementById("message").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

// показ/приховування інструкції
document.getElementById("instruction-btn").addEventListener("click", function() {
    const helpBox = document.getElementById("help-box");
    helpBox.classList.toggle("hidden");
});

function sendMessage() {
    const inputField = document.getElementById("message");
    const message = inputField.value.trim();
    if (!message) return;

    appendMessage("Ви", message);
    inputField.value = "";

    fetch("/get", {
        method: "POST",
        body: JSON.stringify({ message: message }),
        headers: { "Content-Type": "application/json" }
    })
    .then(res => res.json())
    .then(data => {
        appendMessage("Бот", data.response);
    });
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById("chat");
    const msgElement = document.createElement("div");
    msgElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msgElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
