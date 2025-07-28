import os
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://four-ffl1.onrender.com"

app = Flask(__name__)
bot = Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я живой и работаю через Webhook.")

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
async def webhook_handler():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        await application.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Бот работает!"

async def main():
    global application
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await bot.set_webhook(url=f"{WEBHOOK_URL}/webhook/{TOKEN}")
    await application.initialize()
    await application.start()
    print("✅ Бот запущен с Webhook")

if __name__ == "__main__":
    asyncio.run(main())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
