from fastapi import APIRouter
# /items будет указан везде где мы вызываем
router_items = APIRouter(prefix='/items')


@router_items.get('/')
def items():
    return [
        'items1',
        'items2',
        'items2',
        'items3'
    ]

@router_items.get('/{items2_id}/')
def items_id(item_id:int):
    return {
        'item': {
            'id' : item_id,
        }
    }
