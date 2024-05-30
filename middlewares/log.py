from datetime import datetime

from typing import Callable, Dict, Any, Awaitable
from aiogram.types import TelegramObject
from aiogram import types, BaseMiddleware


class logMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: types.Message,
            data: Dict[str, Any]
    ) -> Any:
        """ Логирование команд

        - Выводит в консоль логи при каждой команде.
        - Формат: {time} - {id} - {name} - {ms}.
        """
        name = event.from_user.first_name
        id = event.from_user.id
        time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        ms = event.text
        if ms is None:
            ms = event.web_app_data.data
        print(f"{time} - {id} - {name} - {ms}")
        result = await handler(event, data)
        return result
