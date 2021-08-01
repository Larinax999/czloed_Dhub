import websocket, json, time, random
from concurrent.futures import ThreadPoolExecutor

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc
    
type = "Playing"
status = "random"
i = 0
executor = ThreadPoolExecutor(max_workers=int(100000000000))
tokenlist = open("token_mama.txt").read().splitlines()

def changegame(token, game, type, status):
    ws = websocket.WebSocket()
    if status == "random":
        stat = ['online', 'dnd', 'idle']
        status = random.choice(stat)
    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    if type == "Playing":
        gamejson = {
            "name": game,
            "type": 0
        }
    elif type == 'Streaming':
        gamejson = {
            "name": game,
            "type": 1,
            "url": "https://www.twitch.tv/DEADBREAD'S_RAID_TOOLBOX"
        }
    elif type == "Listening to":
        gamejson = {
            "name": game,
            "type": 2
        }
    elif type == "Watching":
        gamejson = {
            "name": game,
            "type": 3
        }
    auth = {
        "op": 2,
        "d": {
            "token": token,
            "properties": {
                "$os": "windows",
                "$browser": "Discord",
                "$device": "desktop"
            },
            "presence": {
                "game": gamejson,
                "status": status,
                "since": 0,
                "afk": False
            }
        },
        "s": None,
        "t": None
        }
    ws.send(json.dumps(auth))
    ack = {
                "op": 1,
                "d": None
            }
    while True:
        time.sleep(heartbeat_interval/1000)
        try:
            ws.send(json.dumps(ack))
        except Exception:
            break

#changegame("ODM4ODY5NDg3NTgyMzE0NTU2.YJBYGQ.qgolxwLqS7GXM3JvuBIhLVBbyYc", asciigen(30), type, status)
'''
def thread(i) :
    time.sleep(5)
    while True :
        try : 
            changegame(token, asciigen(30), type, status)
            print(f"thread {i} changed status")
        except :
            print(f"thread {i} cannot connect ws")

for token in tokenlist:
    i+=1
    executor.submit(thread, i)
    print(f"start {i} threaded")
'''
for token in tokenlist:
    executor.submit(changegame, token, "0x99a", type, status) #asciigen(40)
    i+=1
    print(f"connected ws : {i}")



