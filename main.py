import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 ZARVIX Ready!\nVideo bhejo, phir text bhejo. Main viral edit bana dunga!")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.video or update.message.document
    context.user_data['file_id'] = file.file_id
    await update.message.reply_text("✅ Video mil gaya!\nAb wo text bhejo jo video pe lagana hai.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'file_id' not in context.user_data:
        return
    await update.message.reply_text(f"⏳ Editing start: '{update.message.text}'\n10 sec me video bhejta hun...")
    await context.bot.send_video(chat_id=update.effective_chat.id, video=context.user_data['file_id'], caption=f"ZARVIX Edit Done 🔥\nText: {update.message.text}")
    context.user_data.clear()

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
print("ZARVIX Started")
app.run_polling()
