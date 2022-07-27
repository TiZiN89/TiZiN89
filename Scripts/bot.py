import settings
import telebot
from telebot import types  # для указание типов


bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "hi":
        bot.send_message(message.chat.id, "Fuck you!")  # посылает сообщение
        first_level_button(message)

    else:
        bot.send_message(message.chat.id, "Try to print 'hi' , asshole!!!")

def first_level_button(message):
    murkup_inline = types.InlineKeyboardMarkup()  # делается клавиатура
    item1 = types.InlineKeyboardButton(text='Да', callback_data='yes')  # первая кнопка
    item2 = types.InlineKeyboardButton(text='нет', callback_data='no')  # вторая кнопка
    murkup_inline.add(item1, item2)  # кнопки добавляются в клавиатуру
    bot.send_message(message.chat.id, 'Do you wanna send me in the same way?', reply_markup=murkup_inline)


@bot.callback_query_handler(func=lambda call: call.data == "yes")
def second_level_yes(call):
    if call.data == 'yes':  # callback_data c функции выше
        second_level_button(call)

@bot.callback_query_handler(func=lambda call: call.data == "no")
def second_level_no(call):
    if call.data == 'no':
        bot.send_message(call.message.chat.id, 'Good for you!!!')
        bot.answer_callback_query(callback_query_id=call.id, text="Good choice, mate.")

def second_level_button(call):
    murkup_reply = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='First chance', callback_data='es')
    item2 = types.InlineKeyboardButton(text='Second chance', callback_data='o')
    murkup_reply.add(item1, item2)
    bot.send_message(call.message.chat.id, 'Choice your destiny:', reply_markup=murkup_reply)
    return True

@bot.callback_query_handler(func=lambda call: call.data == 'es')
def second_answer1(call):
    if call.data == 'es':
        bot.send_message(call.message.chat.id, "Fuck you again!!!))))")

@bot.callback_query_handler(func=lambda call: call.data == 'o')
def second_answer2(call):
    if call.data == 'o':
        bot.send_message(call.message.chat.id, 'You are shrimp')


bot.polling(none_stop=True)