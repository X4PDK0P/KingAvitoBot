import config
import logging
from Parser import *


from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO) # задаем уровень логов
global region, search
# инициализируем бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ Avitobot!\nВведите город и следующим сообщением запрос.")


@dp.message_handler(commands=['s'])
async def send_welcome(message: types.Message):
    global region, search
    recive = message.text.split(" ")
    print("Good", message.text.split(", "))
    # main(recive[1], recive[2])
    await message.reply(main(recive[1], recive[2])[1])

@dp.message_handler()
async def send_welcome(message: types.Message):
    global region, search
    #await message.reply(f"Ваш запрос {message.text}!")
    input_ = message.text
    print()
    if input_[0] == "!":
        search = input_.replace("!", "")
        print(search)
        await message.reply(f"Ваш запрос {search}!")
    elif input_[0] != "!":
        region = input_
        print(region)
        await message.reply(f"Ваш город {region}!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)