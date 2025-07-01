from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

from coro.config import setting


class DatabaseHelper:

    """
    что бы указать одно подключение
       def __init__(self):
        # асинхронный движок,
        self.engine = create_async_engine(
            url=setting.db_url
            echo= setting.bd_echo
        )
        )
    """
    def __init__(self,url: str, echo: bool = False):

        # асинхронный движок,множественное подключение
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        # асинхронная сессия

        self.session_factory = async_sessionmaker(
            bind= self.engine,
            autoflush= False,
            expire_on_commit = False

        )

bd_helps = DatabaseHelper(url=setting.db_url, echo=setting.db_echo)