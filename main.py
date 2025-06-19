import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# === BOT: comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot attivo!")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot Telegram avviato")
    app.run_polling()

# === Finto web server per Render
fake_app = Flask(__name__)

@fake_app.route("/")
def home():
    return "Bot attivo (finta porta viva)"

def run_fake_web():
    fake_app.run(host="0.0.0.0", port=10000)

# === Avvio parallelo
if __name__ == "__main__":
    threading.Thread(target=run_fake_web).start()
    start_bot()
