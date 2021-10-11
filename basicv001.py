import telebot
import time
import urllib
import schedule

TOKEN = '2094252378:AAHrWLPNeAc6fPriFBxbvDMdSe_JbzLq79I'

def report():
    tb = telebot.TeleBot('2094252378:AAHrWLPNeAc6fPriFBxbvDMdSe_JbzLq79I')
    url='http://www.bcra.gov.ar/Pdfs/PublicacionesEstadisticas/infomondiae.pdf'
    f = open('out.pdf','wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()
    tb.send_document('843423661', url)

schedule.every().day.at("12:30").do(report)
while True:
    schedule.run_pending()
    time.sleep(1)
