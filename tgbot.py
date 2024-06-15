import telebot
from telebot import types

bot = telebot.TeleBot("6833228857:AAHTe1Xu64DmF4-HTSlGE0Jt48vpKIfYxRw")


@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}")
    bot.send_message(message.chat.id, [f"ELLEON — КОМПЛЕКСНАЯ КОСМЕТОЛОГИЯ В ЧЕЛЯБИНСКЕ\n1) Адрес: г.Челябинск, ул.Энгельса д.77\n2) Номер телефона для записи: +7 (351) 217-03-03"])

@bot.message_handler(commands=["info"])
def info(message):
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text="Официальный сайт", url="https://elleon-clinic.ru/")
    btn2 = types.InlineKeyboardButton(text="Акции", url="https://elleon-clinic.ru/product/")
    btn3 = types.InlineKeyboardButton(text="Отзывы", url="https://elleon-clinic.ru/company/reviews/")
    btn4 = types.InlineKeyboardButton(text="Прайс-лист", url="https://elleon-clinic.ru/price/")
    btn5 = types.InlineKeyboardButton(text="Перечень услуг", url="https://elleon-clinic.ru/price/")
    btn6 = types.InlineKeyboardButton(text="Сведения о салоне", url="https://elleon-clinic.ru/")
    btn7 = types.InlineKeyboardButton(text="Фото салона", url="https://elleon-clinic.ru/company/photocentr/")
    btn8 = types.InlineKeyboardButton(text="Бренды косметики", url="https://elleon-clinic.ru/company/manufacturers/")
    btn9 = types.InlineKeyboardButton(text="Лицензии", url="https://elleon-clinic.ru/company/licenses/")
    btn10 = types.InlineKeyboardButton(text="Наши соц.сети", url="https://vk.com/elleon_clinic")

    kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, "Информация о салоне", reply_markup=kb)


from config import TO_CHAT_ID

@bot.message_handler(commands=["help"])
def help(m, res=False):
   global help_user_id
   help_user_id = m.from_user.id
   markup = types.InlineKeyboardMarkup()
   button1 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
   markup.add(button1)
   msg = bot.send_message(m.chat.id, 'Задайте вопрос боту.', reply_markup=markup)
   bot.register_next_step_handler(msg, helpBot)


def helpBot(m):
     bot.forward_message(TO_CHAT_ID, m.chat.id, m.message_id)


@bot.message_handler(content_types=["text"])
def handle_text(m):

   if int(m.chat.id) == int(TO_CHAT_ID):
      bot.send_message(help_user_id, m.text)


@bot.message_handler(content_types=["text"])
def handle_text(m):

   if int(m.chat.id) == int(TO_CHAT_ID):
      bot.send_message(help_user_id, m.text)



@bot.message_handler(commands=['question'])
def question(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Задать вопрос")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Здравствуйте, {0.first_name}! Задайте свой вопрос".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):

    if (message.text == "Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как проходит консультация?")
        btn2 = types.KeyboardButton("Как отменить запись?")
        btn3 = types.KeyboardButton("Какие есть противопоказания?")
        btn4 = types.KeyboardButton("Как подготовиться к процедурам?")
        btn5 = types.KeyboardButton("С какими проблемами обращаются к врачу-косметологу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "С какими проблемами обращаются к врачу-косметологу?"):
        bot.send_message(message.chat.id, "Победить акне и постакне, удалить пигментные пятна, вылечить угревую болезнь, получить здоровую сияющую ухоженную кожу")


    elif (message.text == "Как подготовиться к процедурам?"):
        bot.send_message(message.chat.id, "Предварительная подготовка не требуется. Лицо очищается от косметических средств, и с помощью лампы-лупы и дерматоскопа оценивается качество кожи")


    elif (message.text == "Как проходит консультация?"):
        bot.send_message(message.chat.id, "На первом этапе заполняется анкета клиента и подписываются необходимые документы. Врач узнает о том, что вас беспокоит в настоящий момент, какой результат вы хотите видеть после процедур.Опираясь на полученную информацию врач диагностирует точную проблему, при необходимости направит на обследование к другим профильным специалистам, таким как эндокринолог или хирург. Разрабатывается комплекс процедур, направленный на достижение вашей цели с учетом ваших анатомических особенностей и противопоказаний. Объясняется последовательность процедур и стойкость эффекта (например, срок рассасывания нитей и филлеров), подбирается лечебная и уходовая косметика")

    elif message.text == "Как отменить запись?":
        bot.send_message(message.chat.id, text="Для отмены записи позвоните по телефону +7 (351) 217-03-03")


    elif message.text == "Какие есть противопоказания?":
        bot.send_message(message.chat.id, text="Для выявления противопоказаний необходима консультация специалиста, который поможет выявить какие процедуры нельзя применять в конкретном случае")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Задать вопрос")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


bot.polling(none_stop=True)
