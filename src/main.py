from fastapi import FastAPI
from src.api import query
from fastapi.responses import RedirectResponse
from utils import helpers


# TODO: Pre-load the dataset

app = FastAPI(
    title="ML API",
    description="API for ML Model Inference",
    version="1.0.0",
)

@app.on_event("startup")
def preload_data():
    helpers.data_loader()

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

app.include_router(query.router)

