from requests import post
from json import loads
from random import randint

def randomint(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

chid = loads(post("https://discord.com/api/v9/users/@me/channels", json={"recipients":["487238612056932368"]}, headers={"authorization": "Bot ODYzNzU0NDU5NjAzNzk1OTg5.YOrgBg.3ai2vXbRupi-O0oU1lW73K9By1M"}).text)['id']
print(chid)
for i in range(10000):
    post(f"https://discord.com/api/v9/channels/{chid}/messages",json={"content":"Hello","nonce":randomint(18),"tts":False},headers={"authorization": "Bot ODYzNzU0NDU5NjAzNzk1OTg5.YOrgBg.3ai2vXbRupi-O0oU1lW73K9By1M"})