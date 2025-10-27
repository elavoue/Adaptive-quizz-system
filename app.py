from flask import Flask, render_template, request, redirect, url_for
from db import get_all_users, get_user
from backend.adapt_quiz import adapt_quiz

app = Flask(__name__)

@app.route("/")
def index():
    users = get_all_users()
    return render_template("index.html", users=users)

@app.route("/quiz/<int:user_id>")
def quiz(user_id):
    user = get_user(user_id)
    if not user:
        return "User not found", 404

    context = {"time_available": 15, "device": "mobile", "connection_quality": "fast"}
    quiz_result = adapt_quiz(user, context)
    return render_template("quiz.html", user=user, quiz=quiz_result)

if __name__ == "__main__":
    app.run(debug=True)
