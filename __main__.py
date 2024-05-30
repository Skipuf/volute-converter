import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from middlewares import logMiddleware

from handlers import setup_message_routers
from config_reader import config


async def main() -> None:
    bot = Bot(config.BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.message.middleware(logMiddleware())

    dp.include_router(setup_message_routers())

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
