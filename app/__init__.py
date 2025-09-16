from flask import Flask, render_template

# Flask needs explicit paths for templates and static in Vercel
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/")
def home():
    return render_template("index.html")

import os
from flask import send_from_directory

@app.route("/download-cv")
def download_cv():
    # Get absolute path to the folder containing cv.pdf
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # go up from 'app' folder
    cv_folder = os.path.join(base_dir, "static", "files")
    return send_from_directory(cv_folder, "cv.pdf", as_attachment=True)
