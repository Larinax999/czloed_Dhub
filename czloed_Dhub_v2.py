from requests import get, post, Session
from random import randint, choice
from re import findall, sub
from websocket import WebSocket
from string import ascii_lowercase, digits
#from concurrent.futures import ThreadPoolExecutor
from threading import Thread,active_count
from time import sleep
from json import loads,dumps,load
from flask import Flask, request
from flask_cors import CORS
#from os import system, name

# load config
config = load(open('config.json', encoding='utf-8'))
proxy_list = open(config['proxy_file_name'], encoding='utf-8').readlines()
proxy_num = 0
# init flask
app = Flask(__name__, static_url_path='/html')
CORS(app)
token_am = 0
ver_m = False
ver_p = False
online_tf = False
online_msg = "czloed Dhub"
livesteam_tf = False
livesteam_ch = None
livesteam_g = None
runn = False
# init threadpool
#executor = ThreadPoolExecutor(max_workers=int(10000))

def headers(token=None, fingerprint=None, mail=False,xsu=None,useragent=None, referrer="https://discord.com/channels/@me") :
    if token :
        if mail :
            return {'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36', 'authorization': "Bearer " + token}
        else :
            head = {'origin': 'https://discord.com', 'Accept': '*/*','Accept-Language': 'en-US', 'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.7 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36', 'authorization': token, 'x-super-properties': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS43Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTgzNjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODgxODEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
            if referrer :
                head["referrer"] = referrer
            if useragent :
                head["user-agent"] = useragent
            if xsu :
                head["x-super-properties"] = xsu
            return head
    else :
        head = {'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36'}
        if mail : 
            return head
        head['x-super-properties'] = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMTQgU2FmYXJpLzUzNy4zNiBFZGcvOTEuMC44NjQuNTQiLCJicm93c2VyX3ZlcnNpb24iOiI5MS4wLjQ0NzIuMTE0Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjg4MTgxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        if fingerprint :
            head['x-fingerprint'] = fingerprint
        return head
    
#def clear():
#    system('cls' if name=='nt' else 'clear')


def get_bal():
    return post('https://api.capmonster.cloud/getBalance',timeout=5,json={"clientKey": config['cap_key']}).json()['balance']

def randomstr(n):
	return ''.join(choice(ascii_lowercase + digits) for _ in range(n))

def randomint(n):
    return str(randint(10**(n-1), (10**n)-1))

def get_fingerprint():
    return get("https://discord.com/api/v9/experiments", headers=headers()).json()["fingerprint"]

def sendmsg(msg, chid, guild_id, token):
    post(f"https://discord.com/api/v9/channels/{chid}/messages", json={"content":msg,"nonce":randomint(18),"tts":False}, headers=headers(token, referrer=f"https://discord.com/channels/{guild_id}/{chid}"))

def get_proxy():
    global proxy_num,proxy_list
    try :
        proxy = proxy_list[proxy_num]
        proxy_num+=1
    except:
        proxy = proxy_list[0]
        proxy_num=0
    return proxy.replace('\n','')


def get_captcha_code():
    taskid = post('http://api.capmonster.cloud/createTask', json={"clientKey":config['cap_key'],"task":{"type":"HCaptchaTaskProxyless","websiteURL":"https://discord.com/register","websiteKey":"f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"}}).json()['taskId']
    sleep(1)
    while True:
        lest_res = post('http://api.capmonster.cloud/getTaskResult', json={"clientKey":config['cap_key'], 'taskId': taskid}).json()
        if lest_res['status'] == 'ready':
            return lest_res['solution']['gRecaptchaResponse']
            break
        sleep(2)

# create zone
def token_gen(username,invite=config["invite_link"], verify_mail=False, verify_phone=False, file_name="token"):
    global token_am
    password = "czloed_Dhub@"
    register_payload = {"fingerprint":"","email": randomstr(randint(3, 6)) + randomint(randint(3, 5)) + "@gmail.com","username":username,"password": password,"invite":invite,"consent":True,"date_of_birth":"1999-03-05","gift_code_sku_id":"","captcha_key":""}
    
    if verify_mail :
        mail_domain = get("https://api.mail.tm/domains", headers=headers(mail=True)).json()["hydra:member"][0]["domain"]
        mail = f"{username}@{mail_domain}"
        post("https://api.mail.tm/accounts",json={"address":mail,"password":password}, headers=headers(mail=True))
        register_payload["email"] = mail
        mail_token = post("https://api.mail.tm/token",json={"address":mail,"password":password}, headers=headers(mail=True)).json()["token"]
    fingerprint = get_fingerprint()
    register_payload["fingerprint"] = fingerprint
    register_payload["captcha_key"] = get_captcha_code()
    while True:
        proxy = {'https': f"socks4://{get_proxy()}"}
        try :
            textres = post("https://discord.com/api/v9/auth/register", timeout=5,proxies=proxy, json=register_payload, headers=headers(referrer="https://discord.com/register", fingerprint=fingerprint)).json()
            discord_token = textres["token"]
            print("[token gen] I Got token | " + discord_token)
            a = open(f'{file_name}.txt', 'a')
            a = a.write(f"{discord_token}\n")
            token_am += 1
            break
        except :
            try :
                print("[token gen] fail to gen token | "+ textres)
            except:
                print("[token gen] fail to gen token | i thing proxy")
            try:
                textres['captcha_key']
                break
            except:
                pass
        register_payload["email"] = randomstr(randint(1, 6)) + randomint(randint(1, 5)) + "@gmail.com"
        
    
    if verify_mail :
        print("[mail] Waiting for mail...")
        message=""
        msg_id=""
        while True :
            sleep(5)
            try :
                print("[mail] checking...")
                message = get("https://api.mail.tm/messages", headers=headers(mail_token, mail=True)).json()
                msg_id = message["hydra:member"][0]["id"]
                print("[mail] I Got Mail")
                break
            except :
                pass
        message = get(f"https://api.mail.tm/messages/{msg_id}", headers=headers(mail_token, mail=True)).json()["text"]
        link = findall(r'(https?://\S+)', message)[0]
        token_verify = get(link, headers=headers(discord_token)).url.partition("https://discord.com/verify#token=")[2]
        
        verify_payload = {"token": token_verify, "captcha_key": get_captcha_code()}
        post("https://discord.com/api/v9/auth/verify", headers=headers(discord_token, referrer="https://discord.com/verify", fingerprint=fingerprint), json=verify_payload)
        print("[mail] Done")
        
    if verify_phone :
        print("[token gen] wait for phone verify | " + discord_token)
        sms_auth = {'Authorization':config['sms_key'],'Accept': 'application/json'}
        sms_res = get('https://5sim.net/v1/user/buy/activation/cambodia/any/discord',headers=sms_auth).json()
        sms_id = sms_res['id']
        sms_num = sms_res['phone']
        print(f"[SMS] Got a number({sms_num})")
        sleep(2.5)
        response = post('https://discord.com/api/v9/users/@me/phone', headers=headers(discord_token, fingerprint=fingerprint,useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54",xsu="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMTQgU2FmYXJpLzUzNy4zNiBFZGcvOTEuMC44NjQuNTQiLCJicm93c2VyX3ZlcnNpb24iOiI5MS4wLjQ0NzIuMTE0Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2dpdmVhd2F5Ym90LnBhcnR5LyIsInJlZmVycmluZ19kb21haW4iOiJnaXZlYXdheWJvdC5wYXJ0eSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo4ODI5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="), json={"phone": sms_num})
        if response.status_code != 204:
            print(response.json()['message'])
            return False
        print("[SMS] Waiting for code...")
        sleep(2.5)
        maxAttempts = 30
        attempts = 0
        while 1:
            if attempts >= maxAttempts:
                break
            sleep(10)
            print("[SMS] checking...")
            response = get(f'https://5sim.net/v1/user/check/{sms_id}',headers=sms_auth).json()
            attempts += 1
            if response['sms'] != None:
                break
        
        if attempts >= maxAttempts:
            get(f'https://5sim.net/v1/user/ban/{sms_id}',headers=sms_auth)
            return False
        code = response['sms'][0]['code']
        print(f"[SMS] Found code: {str(code)}.")
        lastResponse = post('https://discord.com/api/v9/users/@me/phone/verify', headers=headers(discord_token, fingerprint=fingerprint,useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54",xsu="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMTQgU2FmYXJpLzUzNy4zNiBFZGcvOTEuMC44NjQuNTQiLCJicm93c2VyX3ZlcnNpb24iOiI5MS4wLjQ0NzIuMTE0Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2dpdmVhd2F5Ym90LnBhcnR5LyIsInJlZmVycmluZ19kb21haW4iOiJnaXZlYXdheWJvdC5wYXJ0eSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo4ODI5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="), json={'code': code})
        if lastResponse.status_code == 204:
            get(f'https://5sim.net/v1/user/finish/{sms_id}',headers=sms_auth)
            print("[SMS] Done")
        else:
            print(lastResponse.json()['message'])
            return False
    return discord_token
    
#bypass zone
def bypass_aria(token, msg, chid, guild_id): # fix
    sendmsg("-ind", chid, guild_id, token)
    for a in range(len(msg)):   
        sleep(0.5)
        sendmsg(msg[a], chid, guild_id, token)
    sendmsg("Yes", chid, guild_id, token)
    
def bypass_aria_verify(token, chid, guild_id): # fix
    from PIL import Image
    from pytesseract import pytesseract, image_to_string
    from io import BytesIO, StringIO
    from base64 import b64encode
    sendmsg("-verify", chid, guild_id, token)
    sleep(5)
    pytesseract.tesseract_cmd = config['pytessereact']
    msgimg = get(f"https://discord.com/api/v9/channels/{chid}/messages?limit=50", headers=headers(token, referrer=f"https://discord.com/channels/@me/{chid}")).json()
    url = msgimg[0]['embeds'][0]['image']['url']
    imgraw = get(url, headers=headers(mail=True))
    base64_raw = b64encode(imgraw.content).decode("utf-8")
    pic = StringIO()
    image_string = BytesIO(b64decode(base64_raw))
    image = Image.open(image_string)
    bg = Image.new("RGB", image.size, (255,255,255))
    bg.paste(image,image)
    string = sub(r'\W+', '', image_to_string(bg))
    sendmsg(string, chid, guild_id, token)

def bypass_server_cap(token, chid, guild_id): # fix
    from base64 import b64encode
    getchid = post("https://discord.com/api/v9/users/@me/channels", json={"recipients":["512333785338216465"]}, headers=headers(token)).json()
    msgimg = get(f"https://discord.com/api/v9/channels/{getchid['id']}/messages?limit=50", headers=headers(token, referrer=f"https://discord.com/channels/@me/getchid['id']")).json()
    print(msgimg[0]['embeds'][0]['image']['url'])
    imgraw = get(msgimg[0]['embeds'][0]['image']['url'], headers=headers())
    uri = ("data:" + imgraw.headers['Content-Type'] + ";" + "base64," + b64encode(imgraw.content).decode("utf-8"))
    result = solver.normal(uri, hintText='same picture')
    print(result['code'])
    sendmsg(result['code'], chid, guild_id, token)
    return "Done"
    
    
def bypass_fortune_invite(token, invite): # fix 
    from bs4 import BeautifulSoup
    session = Session()
    url = "https://discord.com/api/v9/oauth2/authorize?client_id=618441438564188196&response_type=code&redirect_uri=https%3A%2F%2Fftune.app%2Flogin&scope=identify%20guilds%20guilds.join"
    codeurl = session.post(url, json={"permissions":"0","authorize":True}, headers=headers(token,useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54",xsu="eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMTQgU2FmYXJpLzUzNy4zNiBFZGcvOTEuMC44NjQuNTQiLCJicm93c2VyX3ZlcnNpb24iOiI5MS4wLjQ0NzIuMTE0Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2dpdmVhd2F5Ym90LnBhcnR5LyIsInJlZmVycmluZ19kb21haW4iOiJnaXZlYXdheWJvdC5wYXJ0eSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo4ODI5NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=", referrer=url)).json()
    print(codeurl['location'])
    session.get(codeurl['location'], headers=headers())
    htmltoken = session.get('https://ftune.app/?logged=true', headers=headers()).text
    soup = BeautifulSoup(htmltoken, "html.parser")
    s = str(soup.find_all('script')[0])
    print(htmltoken)
    s = s.split('","')
    print(session.post("https://ftune.app/_go/" + invite, headers=headers(s[-2])).text)

def livestream(token, chid, guild_id):
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    hello = loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    
    ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
    ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    '''
    while runn:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except Exception:
            break
    '''
   #return post(f"http://127.0.0.1:8080/?token={token}&ch={ch_id}&guild={guild_id}")

def online(token,name,livesteam,loop, chid=None, guild_id=None):
    global runn
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    hello = loads(ws.recv())
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"},"presence": {"game": {"name": name,"type": randint(0,3)},"status": choice(['online', 'dnd', 'idle']),"since": 0,"afk": False}}}))
    if livesteam:
        print()
        ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
        ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    if loop:
        heartbeat_interval = hello['d']['heartbeat_interval']
        while runn:
            sleep(heartbeat_interval/1000)
            try:
                ws.send(dumps({"op": 1,"d": None}))
            except Exception:
                break

def start(username,invite):
    token = token_gen(username,invite,ver_m, ver_p)
    if online_tf:
        online(token,online_msg,livesteam_tf,runn,livesteam_ch,livesteam_g)

@app.route("/gen", methods=['POST'])
def api_gen():
    for aa in range(int(request.args['amount'])):
        Thread(target=start,args=(request.args['username'],request.args['invite'])).start()
        if active_count() > 500:
            print("[main] wait 5 sec")
            sleep(5)
        sleep(0.01)
        print(f"[main] Start Thread {aa}")
    return "true"

@app.route("/stats", methods=['GET'])
def api_stats():
    return f"{str(token_am)}|{str(get_bal())}"

@app.route("/update", methods=['POST'])
def api_update():
    global ver_m,ver_p,online_tf,online_msg,livesteam_tf,livesteam_ch,livesteam_g,runn
    method = request.args['method']
    tf = request.args['tf']
    if method == "l":
        if tf == "1":
            livesteam_tf = True
        else :
            livesteam_tf = False
        aaa = request.args['msg'].split("|")
        livesteam_ch = aaa[1]
        livesteam_g = aaa[0]
    elif method == "o":
        if tf == "1":
            online_tf = True
        else :
            online_tf = False
        online_msg = request.args['msg']
    return "true"

@app.route("/", methods=['GET'])
def index():
    return f"{ver_m} {ver_p} {online_tf} {online_msg} {livesteam_tf} {livesteam_ch} {livesteam_g} {runn}"

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=80)
    '''
    if empty():
        exit('capmonster balance empty')
    for aa in range(int(config['tokenc'])):
        aa +=1
        print(f'[main] start gen {aa}')
        #start()
        Thread(target=start).start()
        sleep(0.1)
    '''

# token_gen() 
# bypass_fortune_invite("ODY2NDQ2MzY1MjIzNTUwOTc2.YPSrUQ.RR6ZMXO3LNwxdRTJ9DKu6vnd-YA","aa") #free
# bypass_fortune_invite("<token>","<invite>") #free

# bypass_server_cap("<token>", "<channel_id>", "<guild_id>") #paid
# bypass_aria("<token>", ["a","a","a"], "<channel_id>", "<guild_id>") #free
# bypass_aria_verify("<token>","854917182172299274", "850027624918810624") #free

# livesteam("<token>", "<ch_id>", "<guild_id>") #free