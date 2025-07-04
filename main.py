from fastapi import FastAPI

app = FastAPI()

from routes.auth import router_auth
from routes.orders import router_order

app.include_router(router_auth)
app.include_router(router_order)