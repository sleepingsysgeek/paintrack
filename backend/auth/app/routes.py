# app/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.session import get_db
from auth.app.models import User
from auth.app.schemas import UserCreate, UserLogin
from auth.app.auth import verify_password, get_password_hash, create_access_token, get_current_user
from datetime import timedelta

#fake_db = {}

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()

    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.username}, expires_delta=timedelta(minutes=30))
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected")
async def protected(user: User = Depends(get_current_user)):
    return {"msg": f"Welcome {user.username}, you are authenticated!",
            "user_id": user.id}