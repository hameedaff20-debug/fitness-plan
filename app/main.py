import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
from app.database import init_db

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

# SQLite can only be written to /tmp on Vercel Functions. init_db() is safe here
# because database.py selects /tmp when running in the Vercel environment.
init_db()

# Static assets are committed under app/templates/static. Do not create directories
# at import time because Vercel's deployed filesystem is read-only.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "app", "templates", "static")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
