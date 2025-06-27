from fastapi import APIRouter

# /items будет указан везде где мы вызываем, группа для items
router_items = APIRouter(prefix='/items', tags=['Items'])


@router_items.get('/')
def items():
    return [
        'items1',
        'items2',
        'items2',
        'items3'
    ]


@router_items.get('/{items2_id}/')
def items_id(item_id: int):
    return {
        'item': {
            'id': item_id,
        }
    }
