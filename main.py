from fastapi import FastAPI
import uvicorn

from pandantic import CreatUser

app = FastAPI()


'''
get - получить
post - добавить
'''








@app.get('/')
def hello_index():
    return {
        'message':'hello'
    }


@app.get('/items/')
def items():
    return [
        'items1',
        'items2',
        'items2',
        'items3'
    ]
@app.get('/hello/')
def hello(name:str):
    return {
        'message':f"Привет {name}"
    }

@app.post('/user/')
def create(user: CreatUser):
    return {
        'message':'True',
        'email': user.email
    }



@app.get('/items2/{items2_id}/')
def items_id(item_id:int):
    return {
        'item': {
            'id' : item_id,
        }
    }

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True)

