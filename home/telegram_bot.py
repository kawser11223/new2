from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from django.conf import settings
from .models import Telegram

# টেলিগ্রাম বট সেটআপ
application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

# বটের জন্য স্টার্ট কমান্ড
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    telegram_user, created = Telegram.objects.get_or_create(
        user_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
    )

    if created:
        update.message.reply_text("আপনার সাইনআপ সফল হয়েছে!")
    else:
        update.message.reply_text("আপনি ইতিমধ্যেই নিবন্ধিত আছেন।")

# হ্যান্ডলার যোগ করা
application.add_handler(CommandHandler("start", start))

# বট রান করার ফাংশন
def run_bot():
    application.run_polling()
