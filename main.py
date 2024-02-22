import os
import telebot
from config import Config
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

png = open("cactus.png", "rb")

cfg = Config()

bot = telebot.TeleBot(token=cfg.get("TgBot", "token"))
bot.send_photo(cfg.getint("user", "uid"), photo=png, caption="Полей меня! 💧🌵")
bot.send_message(cfg.getint("admin", "uid"),
                 f'Доставлено к uid: {cfg.getint("user", "uid")} в {datetime.now()}')

