from fastapi import FastAPI
from app.api.items import endpoints as items

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["Items"])