from fastapi import APIRouter
from .schemas import ItemCreate, ItemResponse
from .service import create_item, get_items

router = APIRouter()

@router.post("/", response_model=ItemResponse)
async def create(item: ItemCreate):
    return await create_item(item)

@router.get("/", response_model=list[ItemResponse])
async def list_items():
    return await get_items()