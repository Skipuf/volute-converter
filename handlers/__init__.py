from aiogram import Router


def setup_message_routers() -> Router:
    from . import handlers

    router = Router()
    router.include_router(handlers.router)
    return router