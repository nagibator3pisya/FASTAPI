from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from asyncio import current_task
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
        # асинхронная сессия,фабрика

        self.session_factory = async_sessionmaker(
            bind= self.engine,
            autoflush= False,
            expire_on_commit = False

        )

    async def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc = current_task,
        )
        return session


    # async def session_dependency(self)-> AsyncSession:
    #     async with self.get_scoped_session() as sess:
    #         yield sess
    #         await sess.remove()

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as sess:
            yield sess
            await sess.close()

bd_helps_exempl = DatabaseHelper(url=setting.db_url, echo=setting.db_echo)















