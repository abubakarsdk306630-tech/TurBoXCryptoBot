import os
import telebot
from telebot import types

# Load BOT_TOKEN from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("⚠️ BOT_TOKEN is missing! Please set it in environment variables.")

bot = telebot.TeleBot(BOT_TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📊 Copy Trade")
    btn2 = types.KeyboardButton("💰 Withdraw")
    btn3 = types.KeyboardButton("👥 Referrals")
    btn4 = types.KeyboardButton("💱 Buy & Sell")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "👋 Welcome to TurboX Crypto Bot!\n\nChoose an option below:", reply_markup=markup)

# Handling button presses
@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "📊 Copy Trade":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("▶️ Start Copy")
        btn2 = types.KeyboardButton("⏹ Stop Copy")
        btn3 = types.KeyboardButton("📑 My Trades")
        btn_back = types.KeyboardButton("🔙 Back to Main Menu")
        markup.add(btn1, btn2, btn3, btn_back)
        bot.send_message(message.chat.id, "📊 Copy Trade Options:", reply_markup=markup)

    elif message.text == "💰 Withdraw":
        bot.send_message(message.chat.id, "💸 Withdraw section — set up your wallet address.")

    elif message.text == "👥 Referrals":
        bot.send_message(message.chat.id, "👥 Invite your friends and earn rewards!")

    elif message.text == "💱 Buy & Sell":
        bot.send_message(message.chat.id, "💱 Trading section is under development.")

    elif message.text == "🔙 Back to Main Menu":
        start(message)  # Return to main menu

print("Bot is running...")

# Keep polling
bot.polling()
