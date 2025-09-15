from flask import Flask, render_template, send_from_directory
import os
from werkzeug.exceptions import NotFound    
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static")
)

@app.route("/")
def home():
    cert_dir = os.path.join(app.static_folder, "files", "certifications")
    certs = []
    for filename in os.listdir(cert_dir):
        if filename.endswith(".pdf"):
            name = filename.replace(".pdf", "").replace("_", " ").title()
            certs.append({
                "filename": filename,
                "title": name,
                "description": generate_description(name)
            })
    return render_template("index.html", certifications=certs)



@app.route("/certifications/<filename>")
def serve_certification(filename):
    cert_dir = os.path.join(app.static_folder, "files", "certifications")
    return send_from_directory(cert_dir, filename)


def generate_description(title):
    desc_map = {
        "Ai Essentials": "Fundamental principles and concepts of artificial intelligence.",
        "Ai For Everyone": "A non-technical introduction to AI and its impact across industries.",
        "Ai Foundations Prompt Engineering With Chatgpt": "How to design effective prompts for AI language models like ChatGPT.",
        "Artificial Intelligence On Microsoft Azure": "Implementing AI solutions using Azure's AI and cognitive services.",
        "Building Ai Powered Chatbots": "Creating intelligent chatbots powered by AI technologies.",
        "Chatbotbuildingessentialswithibmwatsonxassistantv2 Badge20250825-6-Slgjug": "Essentials of building chatbots using IBM Watson Assistant V2.",
        "Generative Ai With Large Language Models": "Techniques and applications of generative AI with large language models.",
        "Goitseone Rakgomo-210294342": "Certification awarded to Goitseone Rakgomo (ID: 210294342).",
        "Ibmdesign20250825-6-Ori41": "IBM Design certification — focused on user-centered design principles.",
        "Intro To Ai": "Introduction to AI concepts, history, and basic techniques.",
        "Intro To Responsible Ai": "Principles and best practices for ethical AI development.",
        "Python For Data Science, Ai & Development": "Python programming for data science and AI development."
    }
    # Normalize key to match desc_map keys if needed
    normalized_title = title.replace('_', ' ').strip()
    return desc_map.get(normalized_title, "A professional certification showcasing technical skills and achievements.")

if __name__ == "__main__":
    app.run(debug=True)
