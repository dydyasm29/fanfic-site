import os
from flask import Flask, render_template, request, send_file
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        if prompt:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un auteur de fanfiction."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800
            )
            generated_text = response["choices"][0]["message"]["content"]
            with open("fanfiction.txt", "w", encoding="utf-8") as f:
                f.write(generated_text)
    return render_template("index.html", generated_text=generated_text)

@app.route("/download")
def download():
    return send_file("fanfiction.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
