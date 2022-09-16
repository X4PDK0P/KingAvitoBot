from KingParserAvitobot import bot, dp
from Parser import *

from config import admin_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Запуск")


@dp.message_handler()
async def input_(message):
    recive = message.text.split(", ")
    print("data", recive)
    if len(recive) != 2:
        await message.answer('Город, запрос')
    else:
        await message.answer('Process...')
        dn = main(recive[0], recive[1])
        #nnom = dn.pop(-1)
        ads = dn
        print("ads***********************",ads)
        print('*' * 20)
        #print("nnom**************", nnom)

        for i in range(len(ads)):
            try:
                ad = '\n'.join(ads[i])
                print(ad)
                await message.answer(ad)
            except:
                await message.answer('ERROR №' + str(i))
