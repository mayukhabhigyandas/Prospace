from sqlalchemy.orm import Session
from myproject import User
from schemas import UserCreate, UserUpdate

# Create user
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Retrieve users
def get_users(db: Session):
    return db.query(User).all()

# Update user
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.role = user.role
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete user
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user