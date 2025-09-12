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

@app.route("/download-cv")
def download_cv():
    # Fixed the path parameter - it should be the filename only
    return send_from_directory(
        directory=os.path.join(os.path.dirname(__file__), "../static/files"),
        filename="cv.pdf",  # Changed from 'path' to 'filename'
        as_attachment=True
    )
