from fastapi import APIRouter,HTTPException,status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Product,ProductCreate
from coro.models import db_help, bd_helps_exempl

product_router = APIRouter(tags=['Products'],prefix='/products')
"""
response_model - аннотация, модель ответа
"""


@product_router.get('/',response_model=list[Product])
async def get_products(session: AsyncSession = Depends(bd_helps_exempl.get_scoped_session)):
    # обычное чтение
    return await crud.get_products(session=session)



@product_router.post('/',response_model=Product)
async def create_product(
        product_in:ProductCreate,
        session: AsyncSession = Depends(bd_helps_exempl.get_scoped_session)):
    # создание
    return await crud.create_product(session=session,product_in=product_in)




@product_router.get('/{product_id}/',response_model=Product)
async def get_product(product_id:int,session: AsyncSession = Depends(bd_helps_exempl.get_scoped_session)):
    # чтение по id
    product = await crud.get_product(session=session,product_id=product_id)
    # если он пришел то возвращаем его
    return product



@product_router.put('/{product_id}/')
async def update_product()