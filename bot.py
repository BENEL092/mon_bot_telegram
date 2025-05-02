import asyncio
import nest_asyncio
nest_asyncio.apply()

from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram import Update
from ia import repondre_ia  # ton module IA

# Fonction asynchrone pour gérer les messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text("🤖 Réflexion...")
    response = repondre_ia(user_text)
    await update.message.reply_text(response)

# Point d'entrée principal
async def main():
    app = ApplicationBuilder().token("7990049069:AAGgoww_bdQoed8u6k5qAYFr5RXbfbSZe00").build()

    # Ajout du gestionnaire de messages texte
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot IA en ligne avec Telegram v22+")
    await app.run_polling()

# Démarrer le bot
if __name__ == "__main__":
    asyncio.run(main())
