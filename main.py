from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import BotCommand

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = 'BOT TOKEN HERE'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Хэндлер на команду /help
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("Это тестовый бот для отработки методов платежей и интерактива в телеграмме")

# Хэндлер на команду /support
@dp.message(Command("support"))
async def cmd_start(message: types.Message):
    await message.answer("Место для контактов поддержки")

# Хэндлер на команду /contacts
@dp.message(Command("contacts"))
async def cmd_start(message: types.Message):
    await message.answer("Напишите мне на почту: <какая-то почта>")

# Хэндлер на команду /payments
@dp.message(Command("payments"))
async def cmd_start(message: types.Message):
    await message.answer("Здесь должен быть запрос на сервер с платежами")

# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')
    ]

    await bot.set_my_commands(main_menu_commands)

# Регистрируем асинхронную функцию в диспетчере,
# которая будет выполняться на старте бота,
dp.startup.register(set_main_menu)
# Запускаем поллинг
dp.run_polling(bot)

