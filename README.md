# Flask Portfolio (Vercel-ready)

This is a polished starter Flask portfolio project scaffolded for deployment on **Vercel** as a serverless Python function.

## Features
- Clean project structure
- Theming and responsive template
- SQLite-ready via SQLAlchemy
- Vercel deployment configuration included

## Run locally
1. Create virtualenv and install:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the API entrypoint:
   ```bash
   python api/index.py
   ```
3. Open http://127.0.0.1:5000

## Deploy on Vercel
1. Install Vercel CLI (if needed): `npm i -g vercel`
2. From the project root, run `vercel` and follow prompts.
3. This project uses `@vercel/python` to serve `api/index.py`.
4. `vercel.json` is included and routes all requests to the Python server.

## Files to customize
- `app/config.py` for production settings
- `app/templates/` and `app/static/` for content and branding
- `README.md` to add project-specific details

## Notes
Vercel will run the file in `api/index.py` using the Python runtime. The Flask `app` object is exposed and served as a serverless function. For advanced production usage consider using a container or another PaaS (Railway, Render, Heroku) for full WSGI support.
