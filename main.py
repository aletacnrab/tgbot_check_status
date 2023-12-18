import requests
import time
from telegram import Bot

URL = ''
TOKEN = ''

bot = Bot(token=TOKEN)

url_update = f"https://api.telegram.org/bot{TOKEN}/getUpdates"


def all_chats():
    update = requests.get(url_update).json()
    return {item['message']['chat']['id'] for item in update['result']}


def multy_send(chats, message):
    for chat in chats:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat}&text={message}")
        time.sleep(0.1)


try:
    while True:
        response = requests.get(URL)
        status_code = response.status_code
        message = f'{URL} - {status_code}' if status_code != 404 else f'{URL} - status code: {status_code}'

        chats = all_chats()
        multy_send(chats, message)

        print(message)
        time.sleep(5)

except Exception as e:
    error_message = 'ERROR! Run stopped'
    print(error_message)
    chats = all_chats()
    multy_send(chats, error_message)
    time.sleep(0.5)
