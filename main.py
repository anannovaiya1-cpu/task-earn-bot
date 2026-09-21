import os
import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

USER_DATA = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in USER_DATA:
        USER_DATA[user_id] = {"coins": 10, "links": [], "auto_ad": False}
        
    keyboard = [
        ["📋 Browse Tasks", "👁️ Watch Ad"],
        ["💰 My Coins", "👥 Referrals"],
        ["➕ Add Campaign", "🏧 Withdraw"],
        ["⚡ Start Auto Ad"],
        ["✅ My Claimed Tasks"],
        ["ℹ️ Help"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, persistent=True)
    
    await update.message.reply_text(
        "👋 Welcome to Task Earn Bot!\nSelect an option below to earn coins or promote your links:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

