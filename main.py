import os
from flask import Flask, request
from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

app = Flask(__name__)
bot = Bot(token=TOKEN)

keyboard = ReplyKeyboardMarkup(
    [["💰 Баланс", "🚀 Купить хешрейт"], ["👥 Пригласить друга", "ℹ️ Помощь"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать в облачный майнинг бот!", reply_markup=keyboard
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💰 Баланс":
        await update.message.reply_text("Ваш баланс: 0 USDT")
    elif text == "🚀 Купить хешрейт":
        await update.message.reply_text("Функция покупки в разработке.")
    elif text == "👥 Пригласить друга":
        await update.message.reply_text("Ваша реферальная ссылка: https://t.me/your_bot?start=ref123")
    elif text == "ℹ️ Помощь":
        await update.message.reply_text("Задайте интересующий вас вопрос.")
    else:
        await update.message.reply_text("Я не понял сообщение.")

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)
    await application.process_update(update)
    return "OK"

async def set_webhook():
    await bot.set_webhook(url=f"{WEBHOOK_URL}/webhook/{TOKEN}")

if __name__ == "__main__":
    import asyncio

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhook())
    app.run(host="0.0.0.0", port=10000)

from flask import request

# Webhook для CryptoBot
@app.route('/cryptobot', methods=['POST'])
def cryptobot_webhook():
    data = request.json
    if data and 'invoice_id' in data:
        print("💸 Получено уведомление от CryptoBot:", data)
        # Тут можно добавить обработку: начисление хешрейта, обновление баланса и т.д.
    return 'ok'
