from pydantic import BaseModel, EmailStr, Field


class CreatUser(BaseModel):
    username: str = Field(...,min_length=3,max_length=10)
    email: EmailStr
