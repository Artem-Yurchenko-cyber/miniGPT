document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    const inputField = document.getElementById("user-input");
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
    const chatBox = document.getElementById("chat-box");
    const msgElement = document.createElement("div");
    msgElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(msgElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}