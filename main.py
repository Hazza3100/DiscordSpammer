import requests
import threading
import random
import json


channel = input("Enter channel id: ")
message = input("Enter message to spam: ")




with open('config.json', 'r') as f:
    cfg = json.load(f)


use_proxy = cfg['use_proxy']



readproxy = open('proxies.txt','r')
readproxy2 = readproxy.readlines()
workproxy = []
for proxy3 in readproxy2:
    proxystrip = proxy3.strip('\n')
    workproxy.append(proxystrip)



def spammer():

    proxy1 = random.choice(workproxy)
    proxies = {'http': f'http://{proxy1}','https':f'http://{proxy1}'}

    tokens = open('tokens.txt')
    token = random.choice(tokens.read().splitlines())
    tokens.close()

    headers = {
        "authorization": token
    }

    json = {
        "content": message,
        "tts": False
    }
    if use_proxy == True:
        r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json, proxies=proxies)
    else:
        r = requests.post("https://discord.com/api/v9/channels/"+str(channel)+"/messages", headers=headers, json=json)




def start():
    r = input("Enter amount of messages to spam: ")
    for i in range(int(r)):
        threading.Thread(target=spammer).start()


start()