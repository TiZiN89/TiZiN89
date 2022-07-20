import settings
import telebot
from telebot import types  # для указание типов


bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "hi":
        bot.send_message(message.chat.id, "Fuck you!")  # посылает сообщение
        murkup_inline = types.InlineKeyboardMarkup()  # делается клавиатура
        item1 = types.InlineKeyboardButton(text='Да', callback_data='yes')  # первая кнопка
        item2 = types.InlineKeyboardButton(text='нет', callback_data='no')  # вторая кнопка
        murkup_inline.add(item1, item2)  #  кнопки добавляются в клавиатуру
        bot.send_message(message.chat.id, 'Do you wanna send me in the same way?', reply_markup=murkup_inline)
    else:
        bot.send_message(message.chat.id, "Try to print 'hi' , asshole!!!")



@bot.callback_query_handler(func=lambda call: True)
def second_level(call):
    if call.data == 'yes':  # callback_data c функции выше
        murkup_reply = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='First chance', callback_data='one')
        item2 = types.InlineKeyboardButton(text='Second chance', callback_data='to')
        murkup_reply.add(item1, item2)
        bot.send_message(call.message.chat.id, 'Choice your destiny:', reply_markup=murkup_reply)
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Good for you!!!')
        bot.answer_callback_query(callback_query_id=call.id, text="Good choice, mate.")

@bot.callback_query_handler(func=lambda call: True)
def second_answer(call):
    if call.data == 'First chance':
        bot.send_message(call.message.chat.id, "ooxdfhzdf")


bot.polling(none_stop=True)