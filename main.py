import telebot

bot = telebot.TeleBot('6428377135:AAH9mjdG5LNb5ewkHFNaHmL3fay3HFooJ6o')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Наверняка ты хочешь *узнать по-подробнее о задании* и *посмотреть идеи* для вдохновения, ведь работа довольно непростая. Поэтому лови _список команд_, которые могут тебе пригодиться: \n/figury - расскажет о допустимых фигурах \n/vidy - расскажет о том, что должно быть на работе \n/primer1 - пример вертикальной работы \n/primer2 - пример горизонтальной работы \n/primer3 - пример кубической работы',
                     parse_mode='Markdown')


@bot.message_handler(commands=['figury'])
def main(message):
    bot.send_message(message.chat.id,
                     'Список разрешённых фигур:\nкуб \nпараллелепипед \nсфера \nцилиндр \nпризма треугольная \nпластина квадратная \nпластина прямоугольная \nпластина треугольная \nпластина круглая \nкаркасные конструкции',
                     parse_mode='Markdown')


@bot.message_handler(commands=['vidy'])
def main(message):
    bot.send_message(message.chat.id,
                     'В твоей работе должны присутствовать: \nдва фасада \nплан \nаксонометрия или перспектива \nуказание масштаба \nнадпись "Арт-объект" или "Декоративная композиция',
                     parse_mode='Markdown')


@bot.message_handler(commands=['primer1'])
def main(message):
    bot.send_message(message.chat.id,
                     'Это одна из [вертикальных работ](https://ru.pinterest.com/pin/584201382941452100/) прошлых лет, которая может *натолкнуть вас на идею* для своей работы',
                     parse_mode='Markdown')


@bot.message_handler(commands=['primer2'])
def main(message):
    bot.send_message(message.chat.id,
                     'Это одна из [горизонтальных работ](https://ru.pinterest.com/pin/74027987618049849/) прошлых лет, которая может *натолкнуть вас на идею* для своей работы',
                     parse_mode='Markdown')


@bot.message_handler(commands=['primer3'])
def main(message):
    bot.send_message(message.chat.id,
                     'Это одна из [кубических работ](https://ru.pinterest.com/pin/39476934226340512/) прошлых лет, которая может *натолкнуть вас на идею* для своей работы',
                     parse_mode='Markdown')


bot.infinity_polling()