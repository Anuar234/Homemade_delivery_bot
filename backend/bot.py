from telegram.ext import Application, CommandHandler
from telegram import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "YOUR_BOT_TOKEN"
WEBAPP_URL = "https://yourdomain.com"  # Ваш домен после деплоя

async def start(update, context):
    keyboard = [[
        InlineKeyboardButton(
            "Открыть приложение", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Добро пожаловать! Нажмите кнопку ниже, чтобы открыть мини-приложение.',
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()