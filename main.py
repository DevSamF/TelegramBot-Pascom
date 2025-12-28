import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
from liturgia import liturgia

load_dotenv()

TOKEN = os.getenv("Telegram_Token")
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia uma mensagem quando o comando /start é usado."""
    user = update.effective_user
    await update.message.reply_text(
        f'Olá {user.first_name}! 👋\n\n'
        'Comandos disponíveis:\n'
        '/start - Iniciar o bot\n'
        '/liturgia - Ver a liturgia do dia\n'
    )


async def liturgia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostra a liturgia do dia."""
    resposta = liturgia.get_liturgia()
    await update.message.reply_text(resposta, parse_mode='HTML')
    

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde às mensagens de texto."""
    text = update.message.text.lower()
    await update.message.reply_text(
        f'Você disse: "{update.message.text}"\n\n'
        'Use /help para ver os comandos disponíveis.'
    )

def main():

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("liturgia", liturgia_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Bot iniciado...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()