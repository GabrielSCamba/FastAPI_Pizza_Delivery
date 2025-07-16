# 🍕 FastAPI Pizza Delivery

This is a **RESTful API** project built with **FastAPI** that simulates a pizza delivery system. The application allows user registration and authentication, order creation, item addition/removal, and permission control for admin users.

---

## 🚀 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [Python-Jose](https://python-jose.readthedocs.io/)

---

## ⚙️ Features

- 🔐 JWT Authentication
- 👤 Account creation with unique email constraint
- ✅ User permission checks (admin vs regular)
- 📦 Order creation
- ➕ Add items to an order
- ➖ Remove items from an order
- 🧾 Automatic total order price calculation
- 🧩 Input validation using Pydantic
- 🔄 Database migrations using Alembic

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/FastAPI_Pizza_Delivery.git
cd FastAPI_Pizza_Delivery
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```bash
alembic upgrade head
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

---

## 📬 Main Endpoints

- `POST /create_account`: Create a new user
- `POST /login`: Generate JWT token
- `POST /order`: Create a new order
- `POST /order/add-item`: Add item to order
- `POST /order/remove-item/{id}`: Remove item from order
- `POST /order/conclude/{id}`: Conclude order

---

## 🧑‍💻 Author

**Gabriel Camba**  
[LinkedIn](https://www.linkedin.com/in/gabriel-camba-153b5b131/)