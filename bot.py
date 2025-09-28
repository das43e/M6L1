import telebot
from main import FusionBrainAPI
from config import TOKEN,API_KEY,SECRET_KEY

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Отправьте мне фото, и я замаскирую лица на нем.")









@bot.message_handler(func=lambda message: True)
def echo_message(message):
    promt = message.text
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', API_KEY, SECRET_KEY)
    pipeline_id = api.get_pipeline()
    uuid = api.generate(promt, pipeline_id)
    files = api.check_generation(uuid)[0]
    api.save_image(files,"files.jpg")
    with open("files.jpg","rb") as photo:
        bot.send_photo(message.chat.id,photo)

    








bot.polling()
