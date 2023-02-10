import logging


from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5925222028:AAFHa0Q4dVlDDUpVT864setEpQ5syMqzAh8'


logging.basicConfig(level=logging.INFO)


help_command = ""


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("This TESTING BOT")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=help_command)
    await message.delete()


#Эхо сообщения.
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

