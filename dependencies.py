from models import db
from sqlalchemy.orm import sessionmaker, Session
from main import SECRET_KEY, ALGORITHM, oauth2_schema
from fastapi import Depends,HTTPException
from models import Users
from jose import jwt, JWTError

def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def check_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session)):
    try:
        dict_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_user = int(dict_info.get("sub"))
    except JWTError as error:
        raise HTTPException(status_code=401, detail="Access Denied.")
    user = session.query(Users).filter(Users.id==id_user).first()
    if not user:
        raise HTTPException(status_code=401, detail="Access Denied")
    return user
