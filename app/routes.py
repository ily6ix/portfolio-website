from flask import Blueprint, render_template, url_for
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    projects = [
        {"name": "Smart Classifier", "desc": "A beginner-friendly ML classifier demo.", "url": "#"},
        {"name": "NLP Explorer", "desc": "Text processing and embeddings demo.", "url": "#"},
        {"name": "Capstone Demo", "desc": "Interactive capstone with live demo.", "url": "#"},
    ]
    return render_template('index.html', projects=projects)

@main_bp.route('/projects/<name>')
def project_detail(name):
    return render_template('project_detail.html', name=name)
