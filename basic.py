import telebot
import time
import urllib

TOKEN = '##TOKEN##'

tb = telebot.TeleBot('##TOKEN##')
url='http://www.bcra.gov.ar/Pdfs/PublicacionesEstadisticas/infomondiae.pdf'
f = open('out.pdf','wb')
f.write(urllib.request.urlopen(url).read())
f.close()
tb.send_document('CHAT_ID', url) # Si es un grupo antecede "-" al ID, si es BOT directo, sin el "-" / Canal: @
tb.send_message('CHAT_ID', 'Te dejo el informe actualizado Rey ;)')
