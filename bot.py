import telebot

TOKEN = '8791327298:AAHKEEWGKE8VL9WYUCrSI09QwVrKzsnoALM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! بوت إشارات Pocket Option يعمل بنجاح 🚀")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "تم تلقي رسالتك بنجاح.")

print("البوت يعمل...")
bot.infinity_polling()
