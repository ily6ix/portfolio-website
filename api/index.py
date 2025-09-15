from flask import Flask, render_template, send_from_directory
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static")
)

@app.route("/")
def home():
    return render_template("index.html")

from werkzeug.exceptions import NotFound

@app.route("/download-cv")
def download_cv():
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cv_folder = os.path.join(base_dir, "static", "files")
        return send_from_directory(cv_folder, "cv.pdf", as_attachment=True)
    except NotFound:
        return "CV not found", 404



if __name__ == "__main__":
    app.run(debug=True)
