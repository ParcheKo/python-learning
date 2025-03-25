from fastapi import FastAPI
from app.api.items import endpoints as items

app = FastAPI(
    title="Simple FastAPI example with CI configured",
    description="This is a simple example API with an in-memory implementation for a create and a get-all endpoint. The CI pipeline is also configured to build and test the API. The configured Dockerfile can be used to deploy the API to the Render platform on any push to the branch practice/001_getting_started",
    version="1.0.0",
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc"     # ReDoc
)

app.include_router(items.router, prefix="/items", tags=["Items"])