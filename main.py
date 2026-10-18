import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging to monitor bot performance and track errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot initialization token from BotFather
BOT_TOKEN = "8773982539:AAFqxba_Ou5GMPDNrpRtQBo7aIjymQhFKLY"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command and welcomes the user professionally."""
    user = update.effective_user
    welcome_message = (
        f"Hello, {user.first_name}! Welcome to FileCloudStore Bot.\n\n"
        "Send me your files or links, and I will process and store them for you."
    )
    await update.message.reply_text(welcome_message)

def main() -> None:
    """Start the bot and set up command handlers."""
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Registering handlers
    application.add_handler(CommandHandler("start", start_command))

    print("Bot is up and running smoothly...")
    application.run_polling()

if __name__ == '__main__':
    main()
