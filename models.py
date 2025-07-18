from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm  import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///database.db")

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    active = Column("active", Boolean, nullable=False, default=True)
    admin =  Column("admin", Boolean, nullable=False, default=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Order(Base):
    __tablename__ = "orders"

    """
    ORDER_STATUS = (
        ("PENDING", "PENDING"),
        ("CANCELED", "CANCELED"),
        ("FINISHED", "FINISHED")
    )
    """

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, nullable=False)
    customer = Column("customer", ForeignKey("users.id"))
    price = Column("price", Float, nullable=False)
    items = relationship("OrderItem", cascade="all, delete") 

    def __init__(self, customer, status="PENDING", price=0):
        self.customer = customer
        self.status = status
        self.price = price
    
    def calculate_price(self):
        self.price = sum(item.unit_price * item.quantity for item in self.items)

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer, nullable=False)
    topping = Column("topping", String, nullable=False)
    size = Column("size", String, nullable=False)
    unit_price = Column("unit_price", Float, nullable=False)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, topping, size, unit_price, order):
        self.quantity = quantity
        self.topping = topping
        self.size = size
        self.unit_price = unit_price
        self.order = order
        