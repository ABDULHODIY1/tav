from aiogram import Bot,types,Dispatcher,executor
from aiogram.types import ContentType
BOT_API = "7373197832:AAHqxn4mn9VpGcI7EoT76VyrurS8tgx21Yw"

bot = Bot(BOT_API)
dp = Dispatcher(bot=bot)
Teacher_id = 5640990557
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def upload(mes:types.message):
    document = mes.document
    # await mes.answer_document(document.file_id, caption="Here is your file!")
    await bot.send_document(chat_id=Teacher_id,document=document.file_id,caption=f"True!")


if __name__ == "__main__":
    executor.start_polling(dp)