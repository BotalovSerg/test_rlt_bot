from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и
# возвращать экземпляр класса Config с заполненными полями token
def load_config(path: str):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))