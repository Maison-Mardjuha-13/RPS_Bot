from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# Keyboard with Builder
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

kb_builder.row(button_yes, button_no, width=2)

yes_no_kb: ReplyKeyboardMarkup = kb_builder.as_markup(one_time_keyboard=True, resize_keyboard=True)

# Without Builder
button_r: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_p: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])
button_s: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])

game_kb : ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_r],
                                                              [button_s],
                                                              [button_p]],
                                                    resize_keyboard= True)

