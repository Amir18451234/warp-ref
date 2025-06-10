import telebot

TOKEN = "7711749890:AAHO7EaM6uSRUgnuQ087mrrrIkQD8voM0hM"

bot = telebot.TeleBot(TOKEN)

ADMINS = [8115109143]  # آیدی عددی سازنده

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "سلام! من ربات مدیریت گروه هستم.")

@bot.message_handler(commands=["ban"])
def ban_user(message):
    if message.from_user.id in ADMINS:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            bot.ban_chat_member(message.chat.id, user_id)
            bot.reply_to(message, "کاربر بن شد.")
        else:
            bot.reply_to(message, "روی پیام کاربر ریپلای کن تا بنش کنم.")
    else:
        bot.reply_to(message, "شما ادمین نیستید.")

bot.infinity_polling()
