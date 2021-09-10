from os import system
from concurrent.futures import ThreadPoolExecutor
from time import sleep
executor = ThreadPoolExecutor(max_workers=int(1000000))

chid = input("voice id: ")

tokenlist = open("token_pYf8YXtt.txt", encoding='utf-8').readlines()
for token in tokenlist:#["ODcyNDk3OTc0NDMxODYyODU0.YQrQGA.Zw4Wop9uTCX51SfDxtAAtaRf6gc"]
    token = token.replace("\n","")
    print(token)
    executor.submit(system,f'python play.py {token} {chid}')
    sleep(1)