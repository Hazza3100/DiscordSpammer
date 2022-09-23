import os
import time
import random
import requests
import threading




def spam(channel_id, message):
    token = random.choice(open('tokens.txt', 'r').read().splitlines())

    headers = {
        'authority': 'discord.com','accept': '*/*','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','authorization': token,'origin': 'https://discord.com','referer': f'https://discord.com/channels/@me/{channel_id}','sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','x-debug-options': 'bugReporterEnabled','x-discord-locale': 'en-GB','x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTQ4ODg4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',}

    json = {
        'content': message,
        'tts': False,
    }

    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=json)
    if r.status_code == 200:
        print("Sent message")
    else:
        print("Error")





def menu():
    os.system('cls')
    print("[1] Spammer")

    choice = int(input("Enter choice > "))

    if choice == 1:
        threads = int(input("Amount of messages to spam > "))
        channel_id = input("Enter channel id > ")
        message = input("Enter message > ")
        for _ in range(threads):
            x = threading.Thread(target=spam, args=(channel_id, message))
            x.start()
        for _ in range(threads):
            x.join()
            time.sleep(2)
            menu()


menu()
