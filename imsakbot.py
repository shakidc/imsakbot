from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import json
import re
from datetime import datetime

def imsak(bot, update):
    chat_id = update.message.chat_id
    chat_message = update.message.text
    cm = chat_message.split(' ')
    base_url = "http://api.aladhan.com/v1/calendarByCity?"
    city = cm[1]
    date = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    url = base_url+"city="+str(city)+"&country=Indonesia&method=11&month="+str(month)+"&year="+str(year)
    req = requests.get(url)
    data = json.loads(req.text)
    imsak = data["data"][int(date)-1]["timings"]["Imsak"]
    subuh = data["data"][int(date)-1]["timings"]["Fajr"]
    syuruq = data["data"][int(date)-1]["timings"]["Sunrise"]
    zuhur = data["data"][int(date)-1]["timings"]["Dhuhr"]
    ashar = data["data"][int(date)-1]["timings"]["Asr"]
    maghrib = data["data"][int(date)-1]["timings"]["Maghrib"]
    isya = data["data"][int(date)-1]["timings"]["Isha"]
    mess = "Jadwal Imsak untuk daerah "+city+ " hari ini tanggal "+str(date)+"-"+str(month)+"-"+str(year)+"\n"+"Imsak: "+str(imsak)+"\nSubuh: "+str(subuh)+"\nSyuruq: "+str(syuruq)+"\nZuhur: "+str(zuhur)+"\nAshar: "+str(ashar)+"\nMaghrib: "+str(maghrib)+"\nIsya: "+str(isya)
    bot.send_message(chat_id=chat_id, text=mess)

def main():
    updater = Updater('')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('imsak',imsak))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()