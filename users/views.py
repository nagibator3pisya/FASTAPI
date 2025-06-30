from fastapi import APIRouter

from users import crud
from users.schemas import CreatUser

router_user = APIRouter(prefix='/users',tags=['users'])



@router_user.get('/hello/')
def hello(name:str):
    return {
        'message':f"Привет {name}"
    }


@router_user.post('/')
def create(user: CreatUser):
    return crud.creat_user(usert_in=user)
