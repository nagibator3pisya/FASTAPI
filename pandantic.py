from pydantic import BaseModel,EmailStr

class CreatUser(BaseModel):
    email: EmailStr