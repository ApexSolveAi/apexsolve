# Minimal ApexSolve bot (starter)
from __future__ import annotations
import os, time, textwrap, asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN in .env")

WELCOME = textwrap.dedent("""
👋 Welcome to **ApexSolve AI** — speed + precision.
Commands:
/help — quick guide
/balance — credits (stub)
/buy — purchase (stub)
Send a CAPTCHA image to test the flow.
""")

HELP = "Send a CAPTCHA image or try /buy (stub) — full flow coming next."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, parse_mode=ParseMode.MARKDOWN)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💼 Balance: (stub) – credits system enabling next.")

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💳 /buy (stub) – crypto/Stars checkout enabling next.")

async def on_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Just demonstrate receipt + fake solve
    t0 = time.time()
    await asyncio.sleep(1.0)
    took = time.time() - t0
    await update.message.reply_text(
        f"✅ (demo) Solved: `abc123` (confidence 0.93, {took:.2f}s)",
        parse_mode=ParseMode.MARKDOWN)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(MessageHandler(filters.PHOTO | filters.Document.IMAGE, on_photo))
    app.add_handler(MessageHandler(filters.COMMAND, help_cmd))
    app.run_polling()

if __name__ == "__main__":
    main()
