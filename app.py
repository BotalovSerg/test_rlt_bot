from aiogram import Bot, Dispatcher, executor, types
import json
from config.config import load_config
from main import main_app


conf = load_config('.env')


bot = Bot(token=conf.tg_bot.token)
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Hello")
    
@dp.message_handler(content_types=['text'])
async def msg(message: types.Message):
    msg = json.loads(message.text)    
    dt_from = msg['dt_from']
    dt_upto = msg['dt_upto']
    group_type = msg['group_type']
    print(msg)
    result = main_app(dt_from, dt_upto, group_type)
            
    await bot.send_message(message.chat.id, result)
    


executor.start_polling(dp)