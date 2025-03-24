from .schemas import ItemCreate, ItemResponse

fake_db = []

async def create_item(item: ItemCreate) -> ItemResponse:
    new_item = ItemResponse(id=len(fake_db) + 1, **item.dict())
    fake_db.append(new_item)
    return new_item

async def get_items():
    return fake_db