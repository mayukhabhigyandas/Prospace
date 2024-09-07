from pydantic import BaseModel

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str
    role: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

