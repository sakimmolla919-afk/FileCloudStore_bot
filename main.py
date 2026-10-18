import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8773982539:AAFqxba_Ou5GMPDNrpRtQBo7aIjymQhFKLY"
TARGET_GROUP_ID = "https://t.me/+AZqvBl6W014wZDI1"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def forward_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and (update.message.document or update.message.photo or update.message.video):
        await context.bot.send_document(
            chat_id=TARGET_GROUP_ID,
            document=update.message.document.file_id if update.message.document else update.message.photo[-1].file_id
        )
        await update.message.reply_text("File sent successfully!")

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    
    await app.initialize()
    await app.bot.delete_webhook(drop_pending_updates=True)
    
    app.add_handler(MessageHandler(filters.ATTACHMENT, forward_files))
    
    print("Bot is starting...")
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == '__main__':
    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")
