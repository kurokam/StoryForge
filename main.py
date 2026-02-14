from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ai import generate_story
from collections import defaultdict
import time

USER_LIMIT = defaultdict(lambda: {"count": 0, "date": time.strftime("%Y-%m-%d")})
DAILY_LIMIT = 5

TOKEN = os.getenv("BOT_TOKEN")

async def story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kind = "horror"
    if context.args:
        kind = " ".join(context.args)

    await update.message.reply_text("🧠 Hikaye hazırlanıyor...")
    text = await generate_story(kind)
    await update.message.reply_text(text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("story", story))
    app.run_polling()

if __name__ == "__main__":
    import os
    main()