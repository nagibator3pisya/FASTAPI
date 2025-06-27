from fastapi import FastAPI
import uvicorn

from items_v import router_items
from users.views import router_user

app = FastAPI()
app.include_router(router_items)
app.include_router(router_user)
'''
get - получить
post - добавить
'''

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)

