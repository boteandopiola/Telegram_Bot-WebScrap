import requests

def telegram_bot_sendtext(bot_message):

    bot_token = '1876624034:AAGzIvnkUmp-DriuSPS3ioMeHRFS6PggNSQ'
    bot_chatID = '@gcanaletede2050'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("reenvia a grupos")
#print(test)
