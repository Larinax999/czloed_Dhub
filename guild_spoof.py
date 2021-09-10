from websocket import WebSocket
from json import dumps
from random import randint,randrange,choice
from concurrent.futures import ThreadPoolExecutor

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = randrange(13000)
        asc = asc + chr(num)
    return asc
    
type = "Playing"
status = "random"
i = 0
executor = ThreadPoolExecutor(max_workers=int(1000000000))
tokenlist = open("token_se.txt").read().splitlines()

def changegame(token):
    for a in range(1000):
        ws = WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        auth = {"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}},"s": None, "t": None}
        ws.send(dumps(auth))
        for _ in range(5):
            aa = []
            for _ in range(30):
                aa.append({"name": asciigen(40),"type": 0})
            ws.send(dumps({"op": 3,"d": {"since": 0,"activities": aa,"status": choice(['online', 'dnd', 'idle']),"afk": False}}))

#changegame("ODM4ODY5NDg3NTgyMzE0NTU2.YJBYGQ.qgolxwLqS7GXM3JvuBIhLVBbyYc", asciigen(30), type, status)
#changegame(tokenlist[0],type)
for token in tokenlist:
    executor.submit(changegame, token)
    i+=1
    print(f"connected ws : {i}")



