from fastapi import APIRouter

#---------------auth---------------
router_auth = APIRouter(prefix="/auth", tags=["auth"])

@router_auth.get("/")
async def home():
    return {"message": "Page: Auth"}
