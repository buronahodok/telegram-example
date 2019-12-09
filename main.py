import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from config import TG_TOKEN, BASE_URL

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

start_keyboard = [['Пример клавиатуры']]


def start(update, context):
    text = "Тут какая-то приветсвенная информация"
    update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(start_keyboard, resize_keyboard=True))


def sendinfo(update, context):
    text = "Ваше сообщение:\n{0}".format(update.message.text)
    update.message.reply_text(text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def startBot(url=''):
    if url == '':
        updater = Updater(token=TG_TOKEN, use_context=True)
    else:
        updater = Updater(token=TG_TOKEN, base_url=url, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, sendinfo))

    # log all errors
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


def main():
    logger.info("Bot started")

    try:
        logger.info("Start bot with BASE_URL")
        startBot(BASE_URL)
    except Exception:
        logger.info("Start bot without BASE_URL")
        startBot()

    logger.info("Bot finished")


if __name__ == '__main__':
    main()
