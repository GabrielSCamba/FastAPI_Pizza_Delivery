from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from models import Users
from dependencies import get_session, check_token
from main import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from schemas import Schema_Users
from sqlalchemy.orm import Session
from schemas import Schema_Login
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

router_auth = APIRouter(prefix="/auth", tags=["auth"])

def create_token(id_user, token_duration=timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)):
    expriration_date = datetime.now(timezone.utc) + token_duration
    dict_info = {"sub": str(id_user), "exp": expriration_date}
    encoded_jwt = jwt.encode(dict_info, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def login_authentication(email, password, session):
    user = session.query(Users).filter(Users.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user

@router_auth.get("/")
async def home():
    return {"message": "Page: Auth"}

@router_auth.post("/create_account")
async def create_account(Schema_Users: Schema_Users, session:Session = Depends(get_session)):
    crypted_password = bcrypt_context.hash(Schema_Users.password)
    new_user = Users(Schema_Users.name, Schema_Users.email, crypted_password)
    try:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return {"message": "Account created successfully!"}
    except IntegrityError as e:
        session.rollback()
        if "UNIQUE constraint failed: users.email" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email is already registered."
            )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the account."
        )

@router_auth.post("/login")
async def login(Schema_Login: Schema_Login, session: Session = Depends(get_session)): 
    user = login_authentication(Schema_Login.email, Schema_Login.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="User not found or password is incorrect.")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, token_duration=timedelta(days=7))
        return{
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }

@router_auth.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)): 
    user = login_authentication(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="User not found or password is incorrect.")
    else:
        access_token = create_token(user.id)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
        }


@router_auth.get("/refresh")
async def use_refresh_token(user: Users = Depends(check_token)):
    access_token = create_token(user.id)
    return{
            "access_token": access_token,
            "token_type": "Bearer"
        }