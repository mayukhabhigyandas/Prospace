from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from myproject import SessionLocal, engine
from myproject import Base
import crud, schemas

import asyncio
from admin import init_admin

app = FastAPI()

# Call the init_admin function to start the admin panel
@app.on_event("startup")
async def on_startup():
    await init_admin()
    
# Create tables
Base.metadata.create_all(bind=engine)

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /admin/users/ - Retrieve a list of users
@app.get("/admin/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# POST /admin/users/ - Create a new user
@app.post("/admin/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# PUT /admin/users/{user_id} - Update user details
@app.put("/admin/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# DELETE /admin/users/{user_id} - Delete a user
@app.delete("/admin/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}