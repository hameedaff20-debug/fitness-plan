"""Vercel FastAPI entrypoint.

The application implementation lives in app.main; this file is the
Vercel-supported root entrypoint and deliberately avoids the name app.py,
which would shadow the app Python package.
"""
from app.main import app

__all__ = ["app"]
