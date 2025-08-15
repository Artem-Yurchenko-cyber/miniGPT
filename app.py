from flask import Flask, render_template, request, jsonify
from logic.handlers import handle_message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    response = handle_message(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
