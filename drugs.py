import os
import telebot
from config import Config
from datetime import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))

png = open("drugs.png", "rb")

cfg = Config()

bot = telebot.TeleBot(token=cfg.get("TgBot", "token"))
bot.send_photo(cfg.getint("user", "uid"), photo=png, caption="Время витаминок! :3  💊🍄☕️")
bot.send_message(cfg.getint("admin", "uid"),
                 f'Доставлены "витамины" к uid: {cfg.getint("user", "uid")} в {datetime.now()}')

