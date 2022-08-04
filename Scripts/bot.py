import settings
import telebot
from telebot import types  # для указание типов


bot = telebot.TeleBot(settings.TOKEN)
buttons_inline = list
push = {}


@bot.message_handler(content_types=['text'])
def start(message):
    """ Приеетствует пользователя,если пользователь напишет "hi" """
    if message.text == "hi":
        bot.send_message(message.chat.id, "HI,I'm cat,my name is Tom!")  # посылает сообщение
        first_level_button(message)
        print(push)
    else:
        bot.send_message(message.chat.id, "Try to print 'hi' , human!!!")

def first_level_button(message):
    """Создается первый уровень клавиатуры """
    buttons_inline = types.InlineKeyboardMarkup()  # делается клавиатура
    item1 = types.InlineKeyboardButton(text='Give some food', callback_data='yes')  # первая кнопка
    item2 = types.InlineKeyboardButton(text='Scratch my belly', callback_data='no')  # вторая кнопка
    buttons_inline.add(item1, item2)  # кнопки добавляются в клавиатуру
    bot.send_message(message.chat.id, 'What do you do for me?', reply_markup=buttons_inline)
    push[1] = 0


@bot.callback_query_handler(func=lambda call: call.data == "yes")
def second_level_yes(call):
    """ Если пользователь нажал "Give some food"""

    if call.data == 'yes':  # callback_data c функции выше
        for i in push.keys():
            if i == 1:

                second_level_button(call)



@bot.callback_query_handler(func=lambda call: call.data == "no")
def second_level_no(call):
    """ Если пользователь нажал "Scratch my belly"""
    if call.data == 'no':

        bot.send_message(call.message.chat.id, 'Good decision!!!')
        bot.answer_callback_query(callback_query_id=call.id, text="You are my favorite human!!!")

def second_level_button(call):
    murkup_reply = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Meat', callback_data='es')
    item2 = types.InlineKeyboardButton(text='boones', callback_data='o')
    murkup_reply.add(item1, item2)
    bot.send_message(call.message.chat.id, 'which your prefer for me?:', reply_markup=murkup_reply)
    push[3] = 0

@bot.callback_query_handler(func=lambda call: call.data == 'es')
def second_answer1(call):
    """ Если пользователь нажал "Meat"""
    if call.data == 'es':
        bot.send_message(call.message.chat.id, "Thanks,how do you know my taiste???))))")


@bot.callback_query_handler(func=lambda call: call.data == 'o')
def second_answer2(call):
    """ Если пользователь нажал "boones"""
    if call.data == 'o':
        bot.send_message(call.message.chat.id, 'Bad choice, Im not a dog!!!')


bot.polling(none_stop=True)