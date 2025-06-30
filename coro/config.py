from os import getenv
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_url: str = 'mysql+aiomysql://root:root@localhost:3306/fast_api'


setting = Setting()
print(setting.db_url)