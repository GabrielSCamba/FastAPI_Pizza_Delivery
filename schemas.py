from pydantic import BaseModel
from typing import List

class Schema_Users(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes=True

class Schema_Order(BaseModel):
    id_customer: int

    class Config:
        from_attributes=True

class Schema_Login(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes=True

class Schema_Order_Item(BaseModel):
    quantity: int 
    topping: str
    size: str
    unit_price: float

    class Config:
        from_attributes=True

class Schema_Response_Order(BaseModel):
    id: int
    status: str
    price: float
    items: List[Schema_Order_Item]

    class Config:
        from_attributes=True