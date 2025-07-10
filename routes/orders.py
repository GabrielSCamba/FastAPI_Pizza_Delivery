from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_session, check_token
from schemas import Schema_Order, Schema_Order_Item, Schema_Response_Order
from models import Order, Users, OrderItem

router_order = APIRouter(prefix="/order", tags=["order"], dependencies=[Depends(check_token)])

@router_order.get("/")
async def home():
    return {"message": "Page: Orders"}  

@router_order.post("/order")
async def create_order(Schema_Order: Schema_Order, session: Session=Depends(get_session)):
   new_order = Order(customer=Schema_Order.id_customer)
   session.add(new_order)
   session.commit()
   return {"message": f"Order created successfully. Order ID: {new_order.id}"}

@router_order.post("/order/cancel/{id_order}")
async def order_cancel(id_order: int, session: Session=Depends(get_session), user: Users = Depends(check_token)):
    order = session.query(Order).filter(Order.id==id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail="Order not found.")
    if not user.admin and user.id != order.customer:
        raise HTTPException(status_code=400, detail="User not authorized to modify this order.")
    order.status = "CANCELED"
    session.commit()
    return {
        "messagem": f"order {id_order} canceled successfully.",
        "order" : id_order
        }

@router_order.get("/list")
async def list_orders(session: Session=Depends(get_session), user: Users = Depends(check_token)):
    if not user.admin:
        raise HTTPException(status_code=400, detail="User not authorized to modify this order.")
    else:
        orders = session.query(Order).all()
        return {
            "orders": orders
        }
    
@router_order.post("/order/add-item/{id_order}")
async def add_order_item(id_order: int, 
                         schema_order_item: Schema_Order_Item,
                         session: Session=Depends(get_session), 
                         user: Users = Depends(check_token)):
    order = session.query(Order).filter(Order.id==id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail="Order does not exists.")
    if not user.admin and user.id != order.customer:
        raise HTTPException(status_code=400, detail="User not authorized to do this operation.")
    order_item = OrderItem(schema_order_item.quantity, schema_order_item.topping, schema_order_item.size, schema_order_item.unit_price, id_order)
    session.add(order_item)
    order.calculate_price()
    session.commit()
    return {
        "message": "Item created successfully!",
        "id_item:": order_item.id,
        "order_price": order.price
    }

@router_order.post("/order/remove-item/{id_order_item}")
async def remove_order_item(
                        id_order_item: int, 
                        session: Session=Depends(get_session), 
                        user: Users = Depends(check_token)):
    order_item = session.query(OrderItem).filter(OrderItem.id==id_order_item).first()
    order = session.query(Order).filter(Order.id==order_item.order).first()
    if not order_item:
        raise HTTPException(status_code=400, detail="Item does not exists.")
    if not user.admin and user.id != order.user:
        raise HTTPException(status_code=400, detail="Access not authorized.")
    session.delete(order_item)
    order.calculate_price()
    session.commit()
    return {
        "message": "Item removed successfully!",
        "order_items": len(order.items),
        "order": order
    }

@router_order.post("/order/concluded/{id_order}")
async def order_conclude(id_order: int, session: Session=Depends(get_session), user: Users = Depends(check_token)):
    order = session.query(Order).filter(Order.id==id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail="Order not found.")
    if not user.admin and user.id != order.customer:
        raise HTTPException(status_code=400, detail="User not authorized to modify this order.")
    order.status = "CONCLUDED"
    session.commit()
    return {
        "messagem": f"Order {id_order} concluded successfully.",
        "order_price" : order.price
        }

@router_order.get("/order/{id_order}")
async def order_show(id_order: int, session: Session = Depends(get_session), user : Users = Depends(check_token)):
    order = session.query(Order).filter(Order.id==id_order).first()
    if not order:
        raise HTTPException(status_code=400, detail="Order not found")
    if not user.admin and user.id !=order.user:
        raise HTTPException(status_code=401, detail="User not authorized to modify this order.")
    return{
        "order_items_quantity": len(order.items),
        "order": order
    }

@router_order.get("/list/user-orders", response_model=list[Schema_Response_Order])
async def list_orders(session: Session=Depends(get_session), user: Users = Depends(check_token)):
    orders = session.query(Order).filter(Order.customer==user.id).all()
    return orders