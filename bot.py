import telebot
import os
from dotenv import load_dotenv
from db import init_table, create_record
from datetime import datetime
import re


load_dotenv()

init_table()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot (BOT_TOKEN)


@bot.message_handler(func=lambda message: True)  # Capture all messages sent to the bot
def create_message(message):
    if '-' in message.text and len(message.text.split('-')) == 2:
        dist, time = message.text.split('-')
        
        # Validation for integer and float formats
        if re.match(r'^\d+$', dist) and re.match(r'^\d+(\.\d+)?$', time):
            current_date = datetime.now().strftime("%Y-%m-%d")
            response = f"Date: {current_date}\nDistance-Time: {dist} km-{time} min"
            bot.send_message(message.chat.id, response)
            create_record(dist, time, current_date)
        else:
            bot.send_message(message.chat.id, "Please provide the distance as an integer and time as float (e.g., '1-30.5').")
    else:
        bot.send_message(message.chat.id, "Please provide the distance and time in the format '1-30'.")



bot.polling()