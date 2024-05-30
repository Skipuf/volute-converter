from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from extensions import Values, get_text, is_float
from error import Not_Found_Exception, Сount_Exception, Syntax_Exception

router = Router()
Values = Values()


@router.message(Command("start", "help"))
async def start(message: Message) -> None:
    if message.text == "/start":
        await message.answer(get_text("start", "start"))
    await message.answer(get_text("start", "help"))


@router.message(Command("values"))
async def values(message: Message) -> None:
    await message.answer(str(Values))


@router.message(Command("about"))
async def values(message: Message) -> None:
    await message.answer(get_text("about", "about"))


@router.message()
async def start(message: Message) -> None:
    try:
        ms = message.text.split(" ")
        print(ms)
        if len(ms) != 3:
            raise Syntax_Exception
        if not (Values.check_str(ms[0]) and Values.check_str(ms[1]) and is_float(ms[2])):
            raise Not_Found_Exception
        if float(ms[2]) < 0:
            raise Сount_Exception
        await message.answer(str(Values.get_price(ms[0], ms[1], float(ms[2]))))
    except BaseException as e:
        await message.answer(str(e))
        await message.answer(get_text("start", "help"))
