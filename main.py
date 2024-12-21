from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import datetime
import os
from background import keep_alive


token = "Your"

bot = Bot(token=token)
dp = Dispatcher()

kb_builder1 = ReplyKeyboardBuilder()
kb_builder2 = ReplyKeyboardBuilder()
kb_builder3 = InlineKeyboardBuilder()

button_that_is_it_magic = KeyboardButton(text="Что такое it's magic?")
button_soc_seti = KeyboardButton(text='Социальные сети')
button_vopros = KeyboardButton(text='Вопросы по движку FAQ')
button_subskrib = InlineKeyboardButton(text="StandMir Private", url="Your adres")
button_subskrib_two = InlineKeyboardButton(text="Your adres", url="Your adres")

kb_builder1.row(button_that_is_it_magic, button_soc_seti, button_vopros, width=2)

kb_builder3.row(button_subskrib_two,button_subskrib)


@dp.message(Command(commands="start"))
async def process_start_command(message: CallbackQuery, ):
    #user_channel_status = await bot.get_chat_member(chat_id=Your adres, user_id=message.from_user.id)
    #if user_channel_status.status != 'left':
    await message.answer(
        'Здравствуйте, для использования бота, вам необходимо подписаться на данные каналы.После подписки воспользуйтесь командой /stat',
        reply_markup=kb_builder3.as_markup(resize_keyboard=True))

@dp.message(Command(commands="stat"))
async def process_start_command(message: CallbackQuery, ):
    await message.answer("Вы подписаны на все группы✅")
    await message.answer(
        'Здравствуйте! Вы попали в бота от "Вадима Алексеевича" здесь вы можете задать свой вопрос, а так же мы постараемся вам помочь чем сможем. Скажите что вас интересует👇',
        reply_markup=kb_builder1.as_markup(resize_keyboard=True)
        )

    @dp.message(F.text.lower().in_(["что такое it's magic?"]))
    async def process_that_is_it_magic_command(message: Message):
        await message.answer(
            "Its magic engine table - это платформа с ориентацией создания игр на телефоне. Программа поддерживает несколько языков программирования, одни из главных Java,Python,NodeScript. У языка Java имеется своя документалка (имеет свое значение)."
        )

    @dp.message(F.text.lower().in_(["социальные сети"]))
    async def process_soc_seti_command(message: Message):
        await message.answer(
            "Youtube - 'Your\nTelegram channel - Your "
        )

    @dp.message(F.text.lower().in_(["вопросы по движку faq"]))
    async def process_vopros_command(message: Message):
        await message.answer("Напишите что вас интересует и по какому поводу вам помочь⌨️")

        @dp.message()
        async def process_vopros_52_command(message: types.Message):
            if message.from_user.id == 'Your adres' :
                await message.answer("⛔️К сожалению вы получили бан на отправление сообщения в боте, чтобы подать апелляцию на разбан, пишите модератору: @ModersX_coders")
            else:
                if message.text == None:
                    await message.answer("Ваше сообщение не отправлено.\nПричина:попытка отправить фото видео голосовое сообщение и др. ")
                else:
                    await bot.send_message('Your adres',f'Пришло сообщение от @{message.from_user.username}\nAйди пользователя:{message.from_user.id}\nДата:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\nСообщение:\n{message.text}')
                    await bot.send_message('Your adres',f'Пришло сообщение от @{message.from_user.username}\nAйди пользователя:{message.from_user.id}\nДата:{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\nСообщение:\n{message.text}')
                    await message.answer("Хорошо, ваше сообщение передано модерации, ждите в течении 24 часов вам напишет модератор и поможет.👌")
  


    #else:
        #await message.answer('Здравствуйте, для использования бота, вам необходимо подписаться на данные каналы (Без подписок бот не будет работать). После подписки воспользуйтесь командой /start',reply_markup=kb_builder3.as_markup(resize_keyboard=True))




keep_alive()
if __name__ == '__main__':
    dp.run_polling(bot)