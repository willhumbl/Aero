from flask import Flask, render_template, request
from markdown2 import Markdown



app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def markdown_editor():
    if request.method == "POST":
        text = request.form["text"]
        markdown = Markdown()
        html = markdown.convert(text)
        return render_template("markdown_editor.html", text=html)
    return render_template("markdown_editor.html")


if __name__ == "__main__":
    app.run(debug=True)
