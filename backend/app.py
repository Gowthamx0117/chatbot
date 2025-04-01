from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    chatbot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": chatbot_reply})

if __name__ == "__main__":
    app.run(debug=True)
