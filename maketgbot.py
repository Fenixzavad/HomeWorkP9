import telebot

import random

bot = telebot.TeleBot("5810447925:AAHByckNwb6h0rT-e73ZU44wceTP-_a9VGg")

candies = 35
max_col_candies = 21
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    bot.send_message(message.chat.id, "Игра началась!")
    bot.send_message(message.chat.id, f"Всего на столе кофет {candies}" )
    flag = random.choice(["user", "bot"])
    
    if flag == "user":
            bot.send_message(message.chat.id, f"Ваш первый шаг" )
            controller(message)
    else:
        bot.send_message(message.chat.id, f"Шаг делает Бот")
        controller(message)
        
        
def controller(message):
    global flag
    
    if candies > 0:
        if flag == "user":
            bot.send_message(message.chat.id, f"Сделайте ваш ход и введите количество конфет от 0 до: {max_col_candies}")
            bot.register_next_step_handler(message.user_input)
        else:
            bot.send_message(message.chat.id, f"Ходит Бот")
            bot_input(message)             
    else:
        bot.send_message(message.chat.id, f"Победа в игре {flag}!")
    
def user_input(message):
    global flag, candies, user_turn
    user_turn = int(message.text)
    candies -= user_turn
    
    bot.send_message(message.chat.id, f"Вы взяли конфет: {user_turn}") 
    
    bot.send_message(message.chat.id, f"Осталось конфет: {candies}")    
    flag = "user" if flag == "bot" else "bot"
    controller(message, flag)
    
    

def bot_input(message):
    global flag, candies, bot_turn
    if candies <= max_col_candies:
        bot_turn = candies
    elif candies % max_col_candies == 0:
        bot_turn = max_col_candies -1
    else:
        candies % max_col_candies -1
    candies -= bot_turn
    
    bot.send_message(message.chat.id, f"Бот взял конфет: {bot_turn}") 
    
    bot.send_message(message.chat.id, f"Осталось конфет: {candies}")    
    flag = "user" if flag == "bot" else "bot"
    controller(message, flag)
    
    
    bot.infinity_polling()