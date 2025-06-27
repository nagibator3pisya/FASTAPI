from users.schemas import CreatUser


def creat_user(usert_in:CreatUser) -> dict:
    user = usert_in.model_dump()
    """
    ДАННЫЕ юзера -> в словарь
    """
    return {
        'success': True,
        'user': user,
    }