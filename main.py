import threading
import time
import os
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask

# === Finta app Flask solo per tenere vivo Render ===
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot attivo'

def run_fake_web_server():
    app.run(host='0.0.0.0', port=10000)  # porta finta

# === Bot Telegram ===
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("✅ Bot avviato!")

def start_bot():
    app_telegram = ApplicationBuilder().token(BOT_TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    print("Bot Telegram avviato")
    app_telegram.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_fake_web_server).start()
    start_bot()
