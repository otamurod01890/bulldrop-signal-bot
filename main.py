# main.py
import telebot
import requests
import time

# === Telegram ma’lumotlari ===
TELEGRAM_TOKEN = '7615761765:AAEv9xVo1Bx1KOXs0Z0LUoVtdHlaHU0CypI'
CHAT_ID = '7494712896'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# === Crash o‘yini uchun oddiy signal sharti ===
def get_crash_data():
    url = 'https://bulldrop.vip/pubg/games/crash'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.text
        # Bu yerda real parsing qilish kerak bo‘ladi (hozircha soxta qiymat)
        crash_values = [1.03, 1.15, 1.07, 2.01, 1.11]  # Soxta data
        return crash_values
    else:
        return []

def analyze_crash(values):
    low_count = sum(1 for v in values[:5] if v < 1.2)
    if low_count >= 3:
        return True
    return False

def send_signal():
    bot.send_message(CHAT_ID, "📈 Oxirgi 5 crash ichida 3 tadan ko'prog'i 1.2x dan past! Yaxshi moment bo'lishi mumkin!")

# === Botni ishga tushurish ===
if __name__ == '__main__':
    while True:
        data = get_crash_data()
        if analyze_crash(data):
            send_signal()
        time.sleep(20)  # 20 soniyada bir tekshiradi
