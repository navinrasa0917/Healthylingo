from flask import Flask, render_template, request

app = Flask(__name__)

def simplify_text(text, language):
    # Prototype logic (placeholder for AI model)
    simplified = text.replace("hypertension", "high blood pressure") \
                     .replace("myocardial infarction", "heart attack") \
                     .replace("diabetes mellitus", "diabetes")

    if language == "Tamil":
        simplified = "எளிய விளக்கம்: " + simplified

    return simplified

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        medical_text = request.form["medical_text"]
        language = request.form["language"]
        output = simplify_text(medical_text.lower(), language)

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
