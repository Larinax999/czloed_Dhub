from concurrent.futures import ThreadPoolExecutor as tp
from time import sleep as sp
from time import time
from random import randint,choice
from string import ascii_lowercase, digits
from requests import post,get,Session

ec=tp(max_workers=int(10000))
proxy_list= list()
#proxy_list.extend(open("socks4_buy_100.txt", encoding='utf-8').readlines())
proxy_name=["socks4_100ms_1k.txt","socks4_nice.txt"]
for pn in proxy_name:
    proxy_list.extend(open(pn, encoding='utf-8').readlines())
#print(len(proxy_list))
proxy_num=0
x=open('token_fff.txt', 'a')
def a(u,i):
    global proxy_num,proxy_list,x
    session=Session()
    xsuper = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMzEgU2FmYXJpLzUzNy4zNiBFZGcvOTIuMC45MDIuNzMiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk0Mjk0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
    fingerprint = session.get("https://discord.com/api/v9/experiments", headers={'x-context-properties': 'eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=','authorization':'undefined','x-debug-options': 'bugReporterEnabled','x-super-properties': xsuper,'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}).json()["fingerprint"]
    c=post('http://api.capmonster.cloud/createTask', json={"clientKey":"a0a5a61b5c2e6de308e667e9f641c0e9","task":{"type":"HCaptchaTaskProxyless","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78","websiteURL":f"https://discord.com/invite/{i}","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()['taskId']
    sp(0.5)
    while True:
        d = post('http://api.capmonster.cloud/getTaskResult', json={"clientKey":"a0a5a61b5c2e6de308e667e9f641c0e9", 'taskId': c}).json()
        if d['status'] == 'ready':
            while True:
                if tt <= time():
                    break
                sleep(0.5)
            cap = ""
            while True:
                try :
                    p = proxy_list[proxy_num].replace('\n','')
                    proxy_num+=1
                except:
                    p = proxy_list[0].replace('\n','')
                    proxy_num=0
                n=randint(3,5)
                try:
                    if u == "random":
                        u=''.join(choice(ascii_lowercase + digits) for _ in range(13))
                    tr = session.post("https://discord.com/api/v9/auth/register",timeout=3,proxies={'https': f"socks4://{p}"}, json={"fingerprint":fingerprint,"username":u,"invite":i,"consent":True,"gift_code_sku_id":None,"captcha_key":cap}, headers={
                "cookie": "OptanonConsent=datestamp=Mon+Aug+16+2021+06%3A51%3A50+GMT-0700+(Pacific+Daylight+Time)&version=6.17.0; locale=th",
                "x-fingerprint": fingerprint,
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkyLjAuNDUxNS4xMzEgU2FmYXJpLzUzNy4zNiBFZGcvOTIuMC45MDIuNzMiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTQyOTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
                "referrer": "https://discord.com/register",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
            }).json()
                    dt = tr['token']
                    try :
                        print(f"[token gen] {dt}")
                    except:
                        print("[token gen] err print token")
                    try :
                        x.write(f"{dt}\n")
                    except:
                        print("[token gen] error save file")
                        z=open('token_fast.txt', 'a')
                        z.write(f"{dt}\n")
                        
                except Exception as e:
                    print(e)
                    try:
                        tr['token']
                        break
                    except:
                        pass
                    try:
                        if cap :
                            tr['captcha_key']
                            break
                        else :
                            cap = d['solution']['gRecaptchaResponse']
                    except:
                        pass
                    try :
                        print(f"[token gen] fail to gen token | {tr}")
                    except:
                        print("[token gen] fail to gen token | i thing proxy")
                
            break
        sp(1)
'''
u=input("username : ")
i=input("invite : ")
j=input("amount of bot : ")
t=input("join in (sec) : ")
'''
u="adsfgewgsdv"
i="faCStgST"
j="1"
t="0"
tt=time()+int(t)
for b in range(int(j)):
    a(u,i)
    #ec.submit(a,u,i)
    if b > 500 or b > 1000 or b > 1500 or b > 2000 or b > 2500 or b > 3000:
        print("[main] sleep 5 sec")
        sleep(5)
input("enter to save token\n")