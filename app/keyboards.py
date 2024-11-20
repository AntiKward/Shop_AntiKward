from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[
  [KeyboardButton(text ="Товары")]
])

setting = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text="Футболка", callback_data="t_shirt")],[InlineKeyboardButton(text="Кроссовки", callback_data="sneakers")],
  [InlineKeyboardButton(text="Штаны", callback_data="pants")],[InlineKeyboardButton(text="Свитер", callback_data="sweater")]
])