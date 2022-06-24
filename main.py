import json
import pyrogram
from pyrogram import Client
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl import types, functions

from telethon import TelegramClient
from random import randint

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
        chat = '+KCIdtzGg2zw5MGZi'
        number = '+79951124199'
        api_id = 15380649
        api_hash = '7450fdbb2e7e1ab1ff093dc6ab4d42e2'
        message = config["message"]
except:
    config = {'chat':'+6K98TKwda5xjYzBi', 'number': '+79951124199', 'api_id': 15380649, 'api_hash': '7450fdbb2e7e1ab1ff093dc6ab4d42e2', 'message': 'Ку'}
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
    input("Заполните конфиг файл!: ")
    exit()

proxy = {
    "scheme": "socks5",
    "hostname": "192.111.139.165",
    "port": 4145,
}

def start_comment():
    print('Номер')
    number1 = input()
    print('Api_id')
    api_id1 = input()
    print('Api_hash')
    api_hash1 = input()
    # proxy = {
    #     "scheme": "socks5",  # "socks4", "socks5" and "http" are supported
    #     "hostname": "85.87.49.212",
    #     "port": 1010,
    #     "username": "eac479",
    #     "password": "acc9df"
    # }



    # app = Client("app+6281349942483", proxy=proxy)
    #
    # app.run()
    with Client(f"app+{number1.replace('+', '')}", phone_number=number1, api_id=api_id1, api_hash=api_hash1) as app1:
        try:
            # chat = 'https://t.me/+KCIdtzGg2zw5MGZi'
            # app1.join_chat(chat)
            with open('numbers.txt', 'r+') as f:
                f.seek(0, 2)
                f.write(f"app{number1}")
        except Exception as e:
            print(e)

def start_subs():
    with open('numbers.txt', 'r') as f:
        nums = f.read().splitlines()
    print('Введите кол-во номеров ')
    numbs = int(input())

    for i in range(numbs):
        with Client(f"{nums[i]}") as app1:
            sleep(randint(15, 25))
            try:
                chat = 'https://t.me/+zJLluw1vPiVkZWQ6'
                app1.join_chat(chat)
            except Exception as e:
                print(e)





if __name__ == "__main__":
    start_comment()
