from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

til = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🇺🇸 English",callback_data='en'),
			InlineKeyboardButton("🇷🇺 Русский",callback_data='ru'),
		],



	]
)