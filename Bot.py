import asyncio
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

# Токен бота (можно вставить прямо сюда для теста)
API_TOKEN = "8214877033:AAFMzwv1uMYQ5YB8HzQ1seHNhxx_59QrM_M"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# Стартовое меню с кнопками
router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я твой бот 🙌\nВыбери, что тебя интересует:",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🛍 Каталог", callback_data="catalog")],
            [InlineKeyboardButton(text="💰 Цены", callback_data="price")],
            [InlineKeyboardButton(text="📞 Контакты", callback_data="contact")],
        ])
    )

# Кнопка "Каталог"
router.callback_query(lambda c: c.data == "catalog")
async def catalog(callback):
    await callback.message.answer(
        "📦 Товар 1 — 500₽\n📦 Товар 2 — 1000₽\n📦 Товар 3 — 1500₽"
    )
    await callback.answer()

# Кнопка "Цены"
router.callback_query(lambda c: c.data == "price")
async def price(callback):
    await callback.message.answer(
        "💰 Товар 1 — 500₽\n💰 Товар 2 — 1000₽\n💰 Товар 3 — 1500₽\n\nДоставка — 300₽"
    )
    await callback.answer()

# Кнопка "Контакты"
router.callback_query(lambda c: c.data == "contact")
async def contact(callback):
    await callback.message.answer(
        "📞 Менеджер: username\n⏰ Работаем с 10:00 до 22:00\n📍 Доставка по городу"
    )
    await callback.answer()

# Запуск бота
async def main():
    dp.include_router(router)
    print("Бот запущен! 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
