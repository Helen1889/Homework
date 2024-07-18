import telebot
from configs import keys, TOKEN
from extensions import ConvertionException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def info(message: telebot.types.Message):
    text= ("Добрый день. Для того, чтобы провести конвертацию валюты введите команду в формате:\n \
<имя переводимой валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\n \
/values- узнать список доступных для конвертации валют" )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text= "Доступные валюты: "
    for key in keys.keys():
        text ="\n".join((text, key, ))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=["text",])
def converty(message: telebot.types.Message):
    try:
        valuess= message.text.lower()
        valuess = valuess.split(" ")
        if len(valuess) != 3:
            raise ConvertionException("Неверный ввод параметров.")
        quote, base, amount = valuess
        total = Converter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя\n {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        teext= f"{amount} {quote}= {total} {base} "
        bot.send_message(message.chat.id, teext)

bot.polling()