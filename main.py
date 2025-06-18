import threading
import time
from telegram import Bot
from telegram.ext import ApplicationBuilder, CommandHandler

# === CONFIGURAZIONE ===
BOT_TOKEN = "inserisci_il_tuo_token"

# === FUNZIONE DI AVVIO BOT ===
def start(update, context):
    update.message.reply_text("Bot attivo!")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot avviato!")
    app.run_polling()

# === FINTA WEB SERVER PER RENDER ===
def fake_web_server():
    while True:
        time.sleep(60)

# === AVVIO PARALLELO ===
if __name__ == "__main__":
    threading.Thread(target=fake_web_server).start()
    start_bot()
