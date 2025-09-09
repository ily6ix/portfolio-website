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
