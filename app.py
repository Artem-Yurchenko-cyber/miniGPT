from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower().strip()

    numbers = [int(s) for s in question.split() if s.isdigit()]

    if "додай" in question or "склади" in question:
        answer = sum(numbers)
    elif "перемнож" in question or "помнож" in question:
        if len(numbers) >= 2:
            answer = numbers[0] * numbers[1]
        else:
            answer = "не знайшов два числа"
    else:
        try:
            answer = eval(question)
        except:
            answer = "Не зрозумів завдання"

    return jsonify({"answer": str(answer)})

if __name__ == "__main__":
    app.run(debug=True)