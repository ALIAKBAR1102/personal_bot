from telegram.ext import Updater, CommandHandler

TOKEN = '7267259073:AAE7Q3XIj7iDmXr2hE4DjbHev_aFEAxlcW8'

def start(update, context):
    message = ('меня зовут алиакбар добро пожаловать в мой бот.'
               '\n\n /contact - отправить вам мои контакты. \n'
               '/talk - сомной пообщтся.')
    
    with open('photo.jpg', 'rb') as file:
        update.message.reply_photo(file, message)
 
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()