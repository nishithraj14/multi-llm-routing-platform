from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.config import validate_keys
from backend.ui_routes import router as ui_router

validate_keys()

app = FastAPI(
    title="Multi-Model Routing Platform",
    docs_url=None,
    redoc_url=None
)

# Mount static files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Include UI routes
app.include_router(ui_router)


@app.get("/health")
def health():
    return {"status": "running"}
