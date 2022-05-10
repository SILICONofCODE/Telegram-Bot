from asyncore import dispatcher
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import requests

updater=Updater("*****own_bot_code_here_from_telegram",use_context=True)
dispatcher = updater.dispatcher

def hello(update,context):
    context.bot.send_message(chad_id = update.effective_chat.id, text = 'Hello, How are you.')
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

def hi(update,context):
    context.bot.send_message(chad_id = update.effective_chat.id, text = 'Hello, Hope you are doing well.')
hi_handler = CommandHandler('hi', hi)
dispatcher.add_handler(hi_handler)

def unknown(update,context):
    context.bot.send_message(chad_id = update.effective_chat.id, text = "Sorry, I did't understand the command.")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

def summary(update,context):
    response = requests.get('https://api.covid19api.com/summary')
    if (response.status_code == 200):
        data = response.json
        date = data['Date'][:10]
        ans = f"Covid 19 summary(as of{date}) \n"

        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed','NewDeaths', 'NewRecoverd']:
                ans+= 'Total' + attribute[5::].lower() +" : " + str(value) + "\n"

        print(ans)
        context.bot.send_message(chat_id = update.effective_chat.id, text = ans)

    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Error, something went wrong.")

corona_summary_handler =  CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)

updater.start_polling()
