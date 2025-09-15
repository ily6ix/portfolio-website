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

@app.route("/download-cv")
def download_cv():
    # Fixed the path parameter - it should be the filename only
    return send_from_directory(
        directory=os.path.join(os.path.dirname(__file__), "../static/files"),
        filename="cv.pdf",  # Changed from 'path' to 'filename'
        as_attachment=True
    )
