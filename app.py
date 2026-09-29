"""Vercel/FastAPI application entrypoint.

Vercel's zero-configuration FastAPI runtime detects a root-level app.py.
The actual application remains in the app package.
"""
from app.main import app

__all__ = ["app"]
