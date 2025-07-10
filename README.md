# 🍕 FastAPI Pizza Delivery

Este é um projeto de API RESTful desenvolvido com **FastAPI** que simula um sistema de delivery de pizza. O sistema permite o cadastro e autenticação de usuários, criação de pedidos, adição/remoção de itens, e controle de permissões para usuários admin.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [Python-Jose](https://python-jose.readthedocs.io/)

---

## ⚙️ Funcionalidades

- 🔐 Autenticação com JWT
- 👤 Criação de conta com e-mail único
- ✅ Verificação de permissões de usuário (admin vs. comum)
- 📦 Criação de pedidos
- ➕ Adição de itens ao pedido
- ➖ Remoção de itens do pedido
- 🧾 Cálculo automático do preço total do pedido
- 🧩 Validação de entradas via Pydantic
- 🔄 Migrações de banco de dados com Alembic

---

## 🛠️ Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/FastAPI_Pizza_Delivery.git
cd FastAPI_Pizza_Delivery
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

```bash
alembic upgrade head
```

### 5. Rode a aplicação

```bash
uvicorn main:app --reload
```

📬 Endpoints principais

- POST /create_account: Cria novo usuário

- POST /login: Gera token JWT

- POST /order: Cria novo pedido

- POST /order/add-item: Adiciona item a um pedido

- POST /order/remove-item/{id}: Remove item

- POST /order/conclude/{id}: Conclui pedido

🧑‍💻 Autor
Gabriel Camba
[LinkedIn](https://www.linkedin.com/in/gabriel-camba-153b5b131/)
