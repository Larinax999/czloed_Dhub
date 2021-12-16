from httpx import Client
from requests import post
from concurrent.futures import ThreadPoolExecutor 
from time import time,sleep
from secrets import token_hex
from sys import exit
from random import randint

_i = "discord-testers" # invite code
_n = "luv discord" # name bot
_co= 100 # count bot
_d = 25 # add wait here

auth_proxy = "nah:nahpass@" 
_key="CaPMonsTER_KeY" # capmonster key
exec=ThreadPoolExecutor(max_workers=100000) # init thread
proxy=open("proxy.txt","r", encoding='utf-8').read().splitlines() # read proxy.txt
f=open(f"token_{_i}.txt", "a") # open token.txt
proxyn=0
tc=0
cc=0


def get_p():
    global proxy,proxyn
    try:
        p=proxy[proxyn].replace("\n","")
        proxyn+=1
    except:
        p=proxy[0].replace("\n","")
        proxyn=0
    return f"{auth_proxy}{p}"
'''
def mon_captcha():
    taskid = post('http://api.capmonster.cloud/createTask', json={"clientKey":_key,"task":{"type":"HCaptchaTaskProxyless","websiteURL":"https://discord.com/register","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()['taskId']
    sleep(1)
    while True:
        lest_res = post('http://api.capmonster.cloud/getTaskResult', json={"clientKey":_key, 'taskId': taskid}).json()
        if lest_res['status'] == 'ready':
            return lest_res['solution']['gRecaptchaResponse']
        sleep(2)
'''

def mon_captcha():
    global _key
    taki = post("https://api.anycaptcha.com/createTask",json={"clientKey": _key,"task": {"type": "HCaptchaTaskProxyless","websiteURL":"https://discord.com/register","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()["taskId"]
    while True:
        _ = post("https://api.anycaptcha.com/getTaskResult",json={"clientKey": _key,"taskId":taki}).json()
        if _["errorId"] == 0 and _["status"] == "ready":
            return _["solution"]["gRecaptchaResponse"]
        elif _["errorId"] > 0:
            print(_)
            exit()
        sleep(2)


def gen(name,_c,_p):
    for x in range(50):
        try:
            c = Client(base_url='https://discord.com',proxies={"https://": f"http://{_p}"},headers={"user-agent":"Discord-Android/101009","accept-encoding":"gzip","accept-language":"en-US","x-super-properties":"eyJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiRGlzY29yZC1BbmRyb2lkLzEwMTAwOSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMTAwOSwiY2xpZW50X3ZlcnNpb24iOiIxMDEuOSAtIFN0YWJsZSIsImRldmljZSI6IlNNLUc5MzVGRCwgU00tRzkzNUZEIiwib3MiOiJBbmRyb2lkIiwib3Nfc2RrX3ZlcnNpb24iOiIyNSIsIm9zX3ZlcnNpb24iOiI3LjEuMiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImFjY2Vzc2liaWxpdHlfc3VwcG9ydF9lbmFibGVkIjpmYWxzZSwiYWNjZXNzaWJpbGl0eV9mZWF0dXJlcyI6MTI4LCJjbGllbnRfcGVyZm9ybWFuY2VfY3B1Ijo0MCwiY2xpZW50X3BlcmZvcm1hbmNlX21lbW9yeSI6MTkwMTAwLCJjcHVfY29yZV9jb3VudCI6NCwicmVmZXJyZXIiOiJ1dG1fc291cmNlXHUwMDNkZ29vZ2xlLXBsYXlcdTAwMjZ1dG1fbWVkaXVtXHUwMDNkb3JnYW5pYyIsInV0bV9zb3VyY2UiOiJnb29nbGUtcGxheSIsInV0bV9tZWRpdW0iOiJvcmdhbmljIn0="})
            fp = c.get("/api/v9/experiments",timeout=18).json()["fingerprint"]
            _ = c.post("/api/v9/auth/register",timeout=19,headers={"content-type":"application/json; charset=UTF-8","x-fingerprint":fp,"x-super-properties":"eyJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiRGlzY29yZC1BbmRyb2lkLzEwMTAwOSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwMTAwOSwiY2xpZW50X3ZlcnNpb24iOiIxMDEuOSAtIFN0YWJsZSIsImRldmljZSI6IlNNLUc5MzVGRCwgU00tRzkzNUZEIiwib3MiOiJBbmRyb2lkIiwib3Nfc2RrX3ZlcnNpb24iOiIyNSIsIm9zX3ZlcnNpb24iOiI3LjEuMiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImFjY2Vzc2liaWxpdHlfc3VwcG9ydF9lbmFibGVkIjpmYWxzZSwiYWNjZXNzaWJpbGl0eV9mZWF0dXJlcyI6MTI4LCJjbGllbnRfcGVyZm9ybWFuY2VfY3B1IjoxLCJjbGllbnRfcGVyZm9ybWFuY2VfbWVtb3J5IjoyMTI3MTIsImNwdV9jb3JlX2NvdW50Ijo0LCJkZXZpY2VfYWR2ZXJ0aXNlcl9pZCI6IjYxYTlkMTkxLThjZDAtNDNlOS1iYjljLTg1YmIyMzA3ODU1NCJ9"},json={"consent":True,"captcha_key": _c,"date_of_birth":f"{randint(2003,2005)}-{randint(1,12)}-{randint(1,28)}","email":f"{token_hex(5)}@gmail.com","fingerprint":fp,"invite":_i,"password":token_hex(3),"username":name}).json()
            print(_)
            if _.get("captcha_key",False):
                break
            elif _.get("retry_after",False):
                pass
            else :
                return _["token"]
        except:pass #except Exception as e:print(e) #

def main(_o,i):
    global cc,tc,_n
    _c = mon_captcha()
    #_c = my_captcha()
    _p = get_p()
    #_c,_p = Bypass()
    if _c == None: return
    cc+=1
    print(f"[*] thread : {i} | i got captcha")
    name = f"{token_hex(2)} {_n}"
    
    while True:
        if _o<=time():break
        sleep(0.5)
    
    _ = gen(name,_c,_p)
    f.write(f"{_}\n")
    f.flush()
    print(f"[*] thread : {i} | token : {_[:35]}...")
    tc+=1

if __name__ == "__main__":
    _o = int(time()+_d)
    main(_o,str(1).zfill(2))
    #for x in range(_co): exec.submit(main,_o,str(x+1).zfill(2)) #main(_o,str(x+1).zfill(2))
    print("[!] started all thread")
    while True:
        if _o<=time():break
        sleep(0.5)
    print("[!] start gen")
    exec.shutdown(wait=True)
    #f.close()
    print(f"[*] gen complete | captcha : {cc} | token : {tc}")