'''
Создание
Чтение
Обновить
Удалить
'''
from sqlalchemy import select
from sqlalchemy.engine import Result
from  sqlalchemy.ext.asyncio import AsyncSession

from coro.models import Product
from coro.product.schemas import ProductCreate


async  def get_products(session:AsyncSession)-> list[Product]:
    """
    Чтение
    :param session:
    :return:
    """
    srmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(srmt)
    product = result.scalars().all()
    return list(product)




async def get_product(session:AsyncSession,product_id:int)-> Product | None:
    """
    Чтение по id
    :param session:
    :param product_id:
    :return:
    """
    return await session.get(Product,product_id)



async def create_product(session:AsyncSession,product_in:ProductCreate) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product



















