import telebot
import time
import urllib

TOKEN = '2094252378:AAHrWLPNeAc6fPriFBxbvDMdSe_JbzLq79I' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot('2094252378:AAHrWLPNeAc6fPriFBxbvDMdSe_JbzLq79I')
url='http://www.bcra.gov.ar/Pdfs/PublicacionesEstadisticas/infomondiae.pdf'
f = open('out.pdf','wb')
f.write(urllib.request.urlopen(url).read())
f.close()
tb.send_document('843423661', url)
tb.send_message('843423661', 'Te dejo el informe actualizado Rey ;)')
