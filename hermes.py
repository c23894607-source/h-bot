from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # از محیط متغیر می‌گیریم

async def start(update: Update, context):
    await update.message.reply_text("سلام! من هرمس هستم. چطور می‌تونم کمکت کنم؟")

async def echo(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"گفتی: {text}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # استفاده از Polling (مناسب برای Render)
    app.run_polling()

if name == "main":
    main()
