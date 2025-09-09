from flask import Flask, render_template
import os

def create_app():
    # Get the absolute path to the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
