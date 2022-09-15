from urllib import request
import Constants as keys
from telegram.ext import *
import Responses as R
import requests
import re
print("BOt Started")



# def get_url():
#     contents = requests.get('https://picsum.photos/id/237/200/300')
#     url = contents['url']
#     return url

def send(update,context):
    # url = get_url()
    chat_id = update.message.chat_id
    
    doc= open('lrb.png', 'rb')
    context.bot.send_document(chat_id, doc)


    # chat_id = update.message.chat_id
    # result_path = R.filename
    # doc= open(file=result_path)
    # context.bot.send_document(chat_id, doc)




def start_command(update, context):
    update.message.reply_text('Type something random to get started')
    
def help_command(update, context):
    update.message.reply_text(" Download Your BTEUP EVEN SEM result.........")
    update.message.reply_text("To downlaod your result...\n Please type your enrollment number like E1920303500004")

def handle_messages(update, context):
    text = str(update.message.text).lower()
    if text.startswith('e19'):

        update.message.reply_text('Please wait....')
        update.message.reply_text(f"Downloading your result {text} ")
        update.message.reply_text(f"Type /send to get result")

    response = R.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

def main():

    updater =  Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("send", send))
    dp.add_handler(MessageHandler(Filters.text, handle_messages))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()



main()