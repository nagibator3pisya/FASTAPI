from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from coro.models import Base,db_help
from coro.product.views import product_router
from items_v import router_items
from users.views import router_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_help.bd_helps_exempl.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_items)
app.include_router(router_user)
app.include_router(product_router)
'''
get - получить
post - добавить
'''

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)

