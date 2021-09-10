from json import dumps
from websocket import WebSocket
from flask import Flask, request
from concurrent.futures import ThreadPoolExecutor
from random import choice,randint
from time import time

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=int(1000000))

def run(token,guild_id,chid) :
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    #ws.recv()
    #heartbeat_interval = hello['d']['heartbeat_interval']
    josn = {
       "op":2,
       "d":{
            "token":token,
            "properties":{
                "$os":"win32",
                "$browser":"Discord",
                "$device":"desktop"
            },
            "presence":{
                "game":{
                    "name":"czloed Dhub | livestream server",
                    "type":0,
                    "application_id":"882908942227873802",
                    "details":"server by larina#9999",
                    "state":"discord.gg/UrZfmKvcus",
                    "timestamps":{
                        "start": time()
                    },
                    "assets":{
                        "large_image":"882919005394984991",
                        "large_text":"0x99a"
                    },
                    "instance": True
                },
                "status":choice(['online', 'dnd', 'idle']),
                "afk":False
            }
        }
    }
    ws.send(dumps(josn))
    if not guild_id == "0":
        ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
        ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    '''
    while True:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except Exception:
            break
    '''
    
@app.route("/", methods=['POST'])
def token():
    token = request.args['token']
    executor.submit(run, token, request.args['guild'], request.args['chid'])
    #print(f"connected ws : {token[:35]}")
    return "ok"

@app.route("/", methods=['GET'])
def index():
    return f"czloed Dhub livestream server"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4378)
    #run("ODcyNDk3OTc0NDMxODYyODU0.YSp4zQ.k1dQFnIeUEltb46XEoVk15bepAA",0,0)