from fastapi import APIRouter

router_order = APIRouter(prefix="/order", tags=["order"])

@router_order.get("/")
async def home():
    return {"message": "Page: Orders"}  