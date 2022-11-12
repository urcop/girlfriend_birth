from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("who_is_best", "Показать кто лучшая"),
            types.BotCommand("description", "Краткое описание лучшей"),
            types.BotCommand("congratulations", "Поздравления для заечки"),
            types.BotCommand("quest", "Квест чтобы получить подарок"),
        ]
    )
