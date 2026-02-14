import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from ai import generate_story

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👻 Korku", callback_data="korku")],
        [InlineKeyboardButton("🕵️ Gizem", callback_data="gizem")],
        [InlineKeyboardButton("😱 Gercek Olay", callback_data="gercek")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 Storyforge Bot'a hos geldin!\n\nBir hikaye turu sec:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    category = query.data
    await query.edit_message_text("⏳ Hikaye hazirlaniyor...")

    try:
        story = generate_story(category)
        await query.edit_message_text(f"🎥 **Hazir!**\n\n{story}", parse_mode="Markdown")
    except Exception as e:
        await query.edit_message_text(f"❌ AI hata verdi:\n{str(e)}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot calisiyor...")
    app.run_polling()

if __name__ == "__main__":
    main()