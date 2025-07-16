import requests

headers = {
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4IiwiZXhwIjoxNzUyNTg2ODQ3fQ.K4TxYw4NQjV8AH5U8NBsrF-d2WOMaaAXf-si9bjIcz4"
}

requisition = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(requisition)
print(requisition.json())