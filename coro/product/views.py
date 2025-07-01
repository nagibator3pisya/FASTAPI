from fastapi import APIRouter,HTTPException,status
from . import crud
from .schemas import Product,ProductCreate
product_router = APIRouter(tags=['Products'])
"""
response_model - аннотация, модель ответа
"""

@product_router.get('/',response_model=list[Product])
async def get_products(session):
    # обычное чтение
    return await crud.get_products(session=session)

@product_router.post('/',response_model=Product)
async def create_product(session, product_in:ProductCreate):
    # создание
    return await crud.create_product(session=session,product_in=product_in)




@product_router.get('/{product_id}',response_model=Product)
async def get_product(product_id:int,session):
    # чтение по id
    product = await crud.get_product(session=session,product_id=product_id)
    # если он пришел то возвращаем его
    if product not in None:
        return product
    # если нет то 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Продукт {product_id} не найден'
    )
