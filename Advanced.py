import telebot
import time
import urllib
import schedule

TOKEN = '##TOKEN##'

def report():
    tb = telebot.TeleBot('##TOKEN##')
    url='http://www.bcra.gov.ar/Pdfs/PublicacionesEstadisticas/infomondiae.pdf'
    f = open('out.pdf','wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()
    tb.send_document('CHAT-ID', url)
    tb.send_message('CHAT-ID', 'Su informe señor')

schedule.every().day.at("20:02").do(report)
schedule.every().day.at("20:04").do(report)
while True:
    schedule.run_pending()
    time.sleep(1)  
