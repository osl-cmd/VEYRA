
import os
import requests
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello. I am VEYRA.\n"
        "Sharp mind. Subtle sarcasm. Always one step ahead."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start VEYRA\n"
        "/help - Show commands\n"
        "/ask - Talk to VEYRA"
    )


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("You have my attention. Ask me something.")
        return

    question = " ".join(context.args)
    await update.message.reply_text(
        f"You asked: {question}\n\n"
        "My intelligence module is not connected yet."
    )


async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I would explain the joke, but I prefer intelligent company."
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("joke", joke))

    app.run_polling()


if __name__ == "__main__":
    main()
  
