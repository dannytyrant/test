import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot("6062732335:AAHWYFwLNsTJwEucUrv3rRa5W0ZTiRWXbKU")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        "💄 Перейти на веб сайт компании",
        "📞 Узнать контакт (адрес и номер) представителя в вашем городе",
        "👨‍💼 Стать партнером",
        "❓️ Задать вопрос",
        "📅 Расписание обучения",
        "🏥 Алгоритмы процедур",
        "📖 Каталог товаров",
    ]
    markup.add(*(types.KeyboardButton(button) for button in buttons))
    bot.send_message(
        message.chat.id,
        "Привет! Я информационный бот компании 'INKI'.\n Чтобы воспользоваться мной, выберите одну из кнопок, представленных ниже.",
        reply_markup=markup
    )

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "📞 Узнать контакт (адрес и номер) представителя в вашем городе":
            bot.send_message(message.chat.id, "Напишите название вашего города")
        elif message.text == "👨‍💼 Стать партнером":
            url = "https://inkiltd.com/stat-partnerom/"
            keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Стать партнером", url=url))
            bot.send_message(
                message.chat.id,
                "Чтобы стать нашим партнером вам необходимо оставить заявку на сайте по ссылке, указанной ниже 👇",
                reply_markup=keyboard
            )


        elif message.text == "💄 Перейти на веб сайт компании":
            url = "https://inkiltd.com"
            keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="INKI", url=url))
            bot.send_message(
                message.chat.id,
                "Нажми на кнопку ниже 👇 и перейди на сайт компании.",
                reply_markup=keyboard
            )


        elif message.text == "❓️ Задать вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            buttons2 = [
                "Да",
                "Нет",
                "◀️ Назад",
            ]
            markup.add(*(types.KeyboardButton(button) for button in buttons2))
            bot.send_message(
                message.chat.id,
                "Ваш запрос по заказу?",
                reply_markup=markup
            )
        if message.text == "Нет":
               bot.send_message(
                    message.chat.id,
                    "По другим вопросам рекомендуем обратиться на электронную почту: info.inki@yandex.ru",

                )
        elif message.text == "Да":
                bot.send_message(
                    message.chat.id,
                    "Напишите ваш вопрос: "
                )
        elif message.text == "Да":
            bot.send_message(
                message.chat.id,
                "Напишите ваш вопрос: "
            )




        elif message.text == "🏥 Алгоритмы процедур":
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("Препаратный (необрезной) маникюр"),
                types.InlineKeyboardButton("Аппаратный маникюр"),
                types.InlineKeyboardButton("Классический обрезной маникюр"),
                types.InlineKeyboardButton("Процедура экоглянцевания"),
                types.InlineKeyboardButton("Холодная парафинотерапия INKI DETOX CARE"),
                types.InlineKeyboardButton("Педикюр/маникюр при онихолизисе"),
                types.InlineKeyboardButton("Педикюр при стержневой мозоли"),
                types.InlineKeyboardButton("Классический педикюр"),
                types.InlineKeyboardButton("Педикюр при наличии натоптышей"),
                types.InlineKeyboardButton("Педикюр при диабетической стопе"),
                types.InlineKeyboardButton("Процедура при грибковом поражении стоп"),
                types.InlineKeyboardButton("Процедура при грибковом поражении ногтей"),
                types.InlineKeyboardButton("Работа при вросшем ногте"),
                types.InlineKeyboardButton("Педикюр при гипергидрозе стоп"),
            )
            bot.send_message(
                message.chat.id,
                "Выберите интересующую вас процедуру.",
                reply_markup=markup
            )
        if message.text=="Препаратный (необрезной) маникюр":
            doc = open("Алгоритм проведения процедуры препаратного (необрезного) маникюра.pdf", "rb")
            bot.send_document(
                message.chat.id,
                doc
            )

        elif message.text=="Аппаратный маникюр":
                doc=open("Алгоритм проведения процедуры аппаратного маникюра.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Классический обрезной маникюр":
                doc=open("Алгоритм проведения процедуры классического обрезного маникюра.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Процедура экоглянцевания":
                doc=open("Алгоритм проведения процедуры Экоглянцевания.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Холодная парафинотерапия INKI DETOX CARE":
                doc=open("Алгоритм проведения процедуры холодной парафинотерапии INKI DETOX CARE.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Педикюр/маникюр при онихолизисе":
                doc=open("Алгоритм проведения процедуры педикюра_маникюра при онихолизисе.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Педикюр при стержневой мозоли":
                doc=open("Алгоритм проведения процедуры педикюра при стержневой мозоли.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Классический педикюр":
                doc=open("Алгоритм проведения процедуры классического педикюра.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Педикюр при наличии натоптышей":
                doc=open("Алгоритм проведения процедуры педикюра при наличии натоптышей.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Педикюр при диабетической стопе":
                doc=open("Алгоритм проведения процедуры педикюра при диабетической стопе.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Процедура при грибковом поражении стоп":
                doc=open("Алгоритм проведения процедуры при грибковом поражении стоп.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Работа при вросшем ногте":
                doc=open("Алгоритм работы при вросшем ногте.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )
        elif message.text=="Педикюр при гипергидрозе стоп":
                doc=open("Алгоритм проведения процедуры педикюра при гиперкератозе.pdf","rb")
                bot.send_document(
                    message.chat.id,
                    doc
                )


        elif message.text == "◀️ Назад":
            start(message)






bot.polling(none_stop=True)
