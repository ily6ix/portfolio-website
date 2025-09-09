from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "🚀 Flask is running on Vercel!"

    return app
