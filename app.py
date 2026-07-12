from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

# Cosmos API function
def cosmos_fact():
    try:
        response = requests.get("https://cosmos-api-production.onrender.com/api/v1/random").json()
        return response["content"]
    except:
        return "Space is full of mysteries — try again!"

# Greeting function
def greeting():
    greetings = [
        "👋 Welcome, cosmic explorer!",
        "🌌 Hello there, ready to journey through the stars?",
        "🚀 Greetings, space adventurer!",
        "✨ Hi! Let’s uncover some cosmic wonders together.",
        "💫 COSMO AI was created by Midhun to share the wonders of the universe!"
    ]
    return random.choice(greetings)

# DuckDuckGo search function
def duckduckgo_answer(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url).json()
    if response.get("AbstractText"):
        return response["AbstractText"]
    else:
        return cosmos_fact()  # fallback

@app.route("/")
def home():
    fact = cosmos_fact()
    greet = greeting()
    return render_template("index.html", fact=fact, greet=greet)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()   # read JSON instead of form
    user_question = data.get("question", "")
    answer = duckduckgo_answer(user_question)
    return jsonify({"answer": answer})
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")



if __name__ == "__main__":
    app.run(debug=True)
