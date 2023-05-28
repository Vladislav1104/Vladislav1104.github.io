import config 
import telebot
import requests
import webbrowser as wb
from telebot import types
import search

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):
    # sti = open(path + 'stiker.tgs', 'rb')
    # bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Поиск по HTML тегам и свойствам CSS")
    item2 = types.KeyboardButton("Создание/Редактирование HTML")
    item3 = types.KeyboardButton("Предпросмотр")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\n\nЯ - <b>{1.first_name}</b>, бот NexT2K, студента ЮГУ, "
                     "создан для того, "
                     "чтобы Верстать сайты, "
                     "нажмите кнопку Верстка для создания страницы HTML и ее последующей редакции.\n\n"
                     "<i>Удачного программирования</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['stop'])  # Обработка команды для выхода
def bye(message):
    #bye_Sti = open(path+'byeMorty.tgs', 'rb')

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо провел(а) время \n\n"
                     "Присоединяйся к нашей команде в <a href='https://vk.com/projector_neti'>vk</a>\n"
                     "Наш <a href='https://instagram.com/projector_neti'>inst</a>\n\n"
                     "Напиши Координатору проектов (<a href='https://vk.com/nikyats'>Никите Яцию</a>) и задай интересующие тебя вопросы по <i>проектной деятельности</i>\n\n"
                     "Надеемся, что тебе ответят очень скоро \n\n"
                     "<u>Don't be ill and have a nice day</u> \n\n\n"
                     "P.S.: Если есть какие-то пожелания или вопросы по боту, то напиши <a href='https://vk.com/setmyaddresspls'>мне</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    exit()

@bot.message_handler(content_types=["text"])
def search(message):
     if message.chat.type == 'private':
         if message.text == 'Поиск по HTML тегам и свойствам CSS':
            msg = bot.send_message(message.chat.id, 'Введите ключевые слова для поиска по справочнику')
            bot.register_next_step_handler(msg, search_2)
          
         elif message.text == 'Создание/Редактирование HTML':
                go_send_messages(message)
         elif message.text == 'Предпросмотр':
                go_send_url(message)

def search_2(msg):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    itemboo = types.InlineKeyboardButton(text="Тыщ на кнопку и ты уже в справочнике", url="https://htmlbase.ru/search?q=" + msg.text)
    keyboard.add(itemboo)

    bot.send_message(msg.chat.id,
                             "{0.first_name}, ссылка для вашего запроса:\n".format(msg.from_user),
                             reply_markup=keyboard)
    
def go_send_messages(message):
            one_markup = types.InlineKeyboardMarkup(row_width=1)
            ite1 = types.InlineKeyboardButton(text="Добавить приветствие", callback_data="one")
            one_markup.add(ite1)
            bot.send_message(message.chat.id, "{0.first_name}, Создана страница HTML <u>ссылка</u> и добавлено приветствие:".format(
                message.from_user), parse_mode="html", reply_markup=one_markup)

@bot.callback_query_handler(func=lambda call: call.data in ['one'])  # Мероприятия
def callback_inline_one(call):
    try:
        if call.message:
            if call.data == 'one':  # Ближайшие мероприятия
                with open('templates/index.html', 'a+') as file:
                    file.write('<p>Hello, world!</p>')
                    bot.send_message(call.message.chat.id,"Приветствие добавлено\n\n", parse_mode="html")
    except:  call.data == "other"

def go_send_url(message):

    bot.send_message(message.chat.id, "{0.first_name}, Создана страница HTML <a href='http://127.0.0.1:5000'>ссылка на сайт</a> и добавлено приветствие:".format(
                message.from_user), parse_mode="html")

# RUN
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")


