import telebot
import config
import pytz
import json
import traceback
import requests
from telebot import types

bot = telebot.TeleBot('1547331745:AAHRNuvghRJyRWHeCoNhEjAPVl2NIQBOkcE')

response = json.loads(requests.get(config.url).text)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Greetings! I can show you exchange rates.\n' +
        'To get the exchange rates press /exchange.\n' +
        'To get help press /help.'
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/aleks'
        )
    )
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' +
        '2) Click on the currency you are interested in.\n' +
        '3) You will receive a message containing information regarding the source and the target currencies, ' +
        'buying rates to base currens USD.\n',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    if message.text == '/exchange':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        itembtn1 = types.KeyboardButton('CAD')
        itembtn2 = types.KeyboardButton('HKD')
        itembtn3 = types.KeyboardButton('ISK')
        itembtn4 = types.KeyboardButton('PHP')
        itembtn5 = types.KeyboardButton('DKK')
        itembtn6 = types.KeyboardButton('HUF')
        itembtn7 = types.KeyboardButton('CZK')
        itembtn8 = types.KeyboardButton('AUD')
        itembtn9 = types.KeyboardButton('RON')
        itembtn10 = types.KeyboardButton('SEK')
        itembtn11 = types.KeyboardButton('IDR')
        itembtn12 = types.KeyboardButton('INR')
        itembtn13 = types.KeyboardButton('BRL')
        itembtn14 = types.KeyboardButton('RUB')
        itembtn15 = types.KeyboardButton('HKR')
        itembtn16 = types.KeyboardButton('JPY')
        itembtn17 = types.KeyboardButton('THB')
        itembtn18 = types.KeyboardButton('CHF')
        itembtn19 = types.KeyboardButton('SGD')
        itembtn20 = types.KeyboardButton('PLN')
        itembtn21 = types.KeyboardButton('BGN')
        itembtn22 = types.KeyboardButton('TRY')
        itembtn23 = types.KeyboardButton('CNY')
        itembtn24 = types.KeyboardButton('NOK')
        itembtn17 = types.KeyboardButton('NZD')
        itembtn18 = types.KeyboardButton('ZAR')
        itembtn19 = types.KeyboardButton('USD')
        itembtn20 = types.KeyboardButton('MXN')
        itembtn21 = types.KeyboardButton('ILS')
        itembtn22 = types.KeyboardButton('GBP')
        itembtn23 = types.KeyboardButton('KRW')
        itembtn24 = types.KeyboardButton('MYR')

        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10,
                   itembtn11, itembtn12, itembtn13, itembtn14, itembtn15, itembtn16, itembtn17, itembtn18, itembtn19,
                   itembtn20, itembtn21, itembtn22, itembtn23, itembtn24)
        msg = bot.send_message(message.chat.id,
                               "Click on the currency of choice:", reply_markup=markup)
        bot.register_next_step_handler(msg, process_coin_step)


def process_coin_step(message):
    try:
        markup = types.ReplyKeyboardRemove(selective=False)

        for k, v in response['rates'].items():
            if (message.text == k):
                bot.send_message(message.chat.id, ("%.2f" % v),
                                 reply_markup=markup, parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!')


bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
