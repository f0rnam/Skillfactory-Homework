import telebot
from config import TOKEN
from extensions import APIException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    """Инструкции для пользователя."""
    text = (
        "Добро пожаловать в валютный бот!\n"
        "Используйте формат: <валюта> <в какую валюту перевести> <количество>\n"
        "Пример: USD EUR 100\n"
        "Для просмотра списка доступных валют используйте команду /values."
    )
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message):
    """Вывод списка доступных валют."""
    try:
        currencies = Converter.get_currencies()
        text = "Доступные валюты:\n" + "\n".join(currencies)
        bot.reply_to(message, text)
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e}")

@bot.message_handler(content_types=['text'])
def convert(message):
    """Обработка запросов на конвертацию валют."""
    try:
        params = message.text.split()
        if len(params) != 3:
            raise APIException("Неверное количество параметров. Формат: <валюта> <в какую> <количество>.")

        base, quote, amount = params
        result = Converter.get_price(base.upper(), quote.upper(), amount)
        bot.reply_to(message, f"Цена {amount} {base.upper()} в {quote.upper()} = {result}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка: {e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка: {e}")

bot.polling(none_stop=True)
