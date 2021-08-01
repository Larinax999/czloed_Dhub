import json,requests

token = input("token : ") # ODU2ODAzNDkzNTIwMDgwOTI3.YNGWcg.Sba9CB9pMu7vDNshf2edjqWJHfg
headers = {'origin': 'https://discord.com','referer': 'https://discord.com/login', 'Accept': '*/*','Accept-Language': 'en-US','Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.7 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36', 'authorization': token, 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMS43Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTgzNjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODgxODEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}
acc_info = json.loads(requests.get("https://discord.com/api/v9/users/@me", headers=headers).text)
acc_lock = requests.get("https://discord.com/api/v9/users/@me/library", headers=headers).status_code

try :
    print(f"""id : {acc_info["id"]}\nusername : {acc_info["username"]}\ndiscriminator : {acc_info["discriminator"]}\nmail verify : {acc_info["email"] if acc_info["verified"] else "False"}\nphone verify : {acc_info["phone"] if acc_info["phone"] else "False"}\nphone lock : {"True" if acc_lock == 403 else "False"}\n2fa : {acc_info["mfa_enabled"]}\nnsfw : {acc_info["nsfw_allowed"]}""")
except :
    print("token?")