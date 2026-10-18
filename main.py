import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Al-bayanat al-khasa bik
TOKEN = "8773982539:AAFqxba_0u5GMPDNrpRtQBo"
TARGET_GROUP_ID = "https://t.me/+AZqvBl6W014wZDI1"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def forward_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and (update.message.document or update.message.photo or update.message.video):
        # Irsal al-malaf ila al-majmu'a al-khasa
        await context.bot.send_document(
            chat_id=TARGET_GROUP_ID,
            document=update.message.document.file_id if update.message.document else update.message.photo[-1].file_id
        )
        await update.message.reply_text("Tam irsal al-malaf binajah!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Ilgha' al-webhook le-man' al-at'al
    app.bot.delete_webhook()
    
    # Mo'alejet al-malafat
    app.add_handler(MessageHandler(filters.ATTACHMENT, forward_files))
    
    print("Al-bot ya'mal alan...")
    app.run_polling()
