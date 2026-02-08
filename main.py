import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from users import inc_use
from ads import get_ad

TOKEN = os.getenv("BOT_TOKEN")

HORROR_HOOKS = [
    "Kimse o kapıyı açmamam gerektiğini söylemedi...",
    "Gece 03:17'de telefonum titredi.",
    "O video silinmişti… ama bana tekrar gönderildi."
]

MYSTERY_HOOKS = [
    "Bu dosya 20 yıldır gizleniyordu.",
    "Kayıtlara göre bu kişi hiç var olmamış.",
    "Bu görüntüler resmi kayıtlardan silindi."
]

SCAM_HOOKS = [
    "Bu mesajı açan herkes parasını kaybetti.",
    "Bu linke tıklayan 1 günde dolandırıldı.",
    "Bu numara yüzünden binlerce kişi mağdur oldu."
]

def build_story(kind):
    if kind == "horror":
        hook = random.choice(HORROR_HOOKS)
        return f"""🎬 Anime Horror Shorts

HOOK:
{hook}

SAHNE:
Karanlık bir odada yalnız kalan karakter, arkasında nefes alındığını hisseder.

TWIST:
Gölge aslında onun gelecekteki halidir.

CAPCUT PROMPT:
dark anime room, glowing eyes, cinematic lighting, horror mood

ETİKET:
#anime #horror #shorts #korku #hikaye
"""
    if kind == "mystery":
        hook = random.choice(MYSTERY_HOOKS)
        return f"""🕵️ Gizem Shorts

HOOK:
{hook}

SAHNE:
Tozlu bir klasör açılır, içinden tek bir fotoğraf düşer.

TWIST:
Fotoğraftaki kişi videoyu izleyen kişinin kendisidir.

CAPCUT PROMPT:
secret files, dark room, cinematic light, mystery mood

ETİKET:
#gizem #shorts #mystery #karanlık
"""
    if kind == "scam":
        hook = random.choice(SCAM_HOOKS)
        return f"""⚠️ Scam Hikâyesi Shorts

HOOK:
{hook}

SAHNE:
Telefonuna gelen bir mesaj: “Hesabın askıya alındı.”

TWIST:
Link sahte, tıklayan herkesin hesabı boşaltılıyor.

CAPCUT PROMPT:
dark phone screen, warning text, cinematic style

ETİKET:
#scam #dolandırıcılık #shorts #uyarı
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 StoryForge AI\n\n"
        "İçerik türü seç:\n"
        "/horror → Anime Horror\n"
        "/mystery → Gizem Dosyası\n"
        "/scam → Dolandırıcılık Hikâyesi\n"
    )

async def horror(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_content(update, "horror")

async def mystery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_content(update, "mystery")

async def scam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_content(update, "scam")

async def send_content(update: Update, kind):
    user_id = update.message.from_user.id
    count = inc_use(user_id)

    content = build_story(kind)
    await update.message.reply_text(content)

    if count % 3 == 0:
        ad = get_ad(count)
        await update.message.reply_text(f"📢 Sponsor:\n{ad}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("horror", horror))
    app.add_handler(CommandHandler("mystery", mystery))
    app.add_handler(CommandHandler("scam", scam))
    app.run_polling()

if __name__ == "__main__":
    main()
