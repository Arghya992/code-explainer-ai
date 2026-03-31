# =============================================================
# app.py - Backend for Code Explainer AI (Groq Version - Secure)
# =============================================================

from flask import Flask, render_template, request, jsonify
from groq import Groq
import os


# =============================================================
# CONFIGURE GROQ API
# =============================================================

# 🔴 PASTE YOUR API KEY HERE (ONLY HERE)

# Get API key securely
API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=API_KEY)


# =============================================================
# CREATE FLASK APP
# =============================================================
app = Flask(__name__)


# =============================================================
# HOME PAGE
# =============================================================
@app.route("/")
def home():
    return render_template("index.html")


# =============================================================
# EXPLAIN CODE ROUTE
# =============================================================
@app.route("/explain", methods=["POST"])
def explain_code():

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        user_code = data.get("code", "")

        if not user_code.strip():
            return jsonify({"error": "Please paste some code first."}), 400


        # Prompt for AI
        prompt = f"""
You are a friendly coding teacher helping beginners understand code.

Explain the following code in this format:

## What This Code Does
Explain the purpose in simple language.

## Line-by-Line Explanation
Explain each important line.

## Simple Summary
Explain it like you would to a beginner.

Code:
{user_code}
"""


        # Call Groq model
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        explanation = response.choices[0].message.content

        return jsonify({"explanation": explanation})


    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# =============================================================
# RUN SERVER
# =============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("🚀 Code Explainer AI running (Groq)")
    print("Open: http://localhost:5000")
    print("=" * 50)

    app.run(debug=True)