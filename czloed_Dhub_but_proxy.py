from requests import post
from json import loads
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor
from flask import request, Flask
from logging import getLogger
from sys import modules
from string import ascii_lowercase, digits
from random import randint, choice

proxylist = open("socks4_2.txt").read().splitlines()
i = 0
# init threadpool
executor = ThreadPoolExecutor(max_workers=int(10000))
# init flask
app = Flask(__name__)
CORS(app)
# disable flask log
log = getLogger('werkzeug')
log.disabled = True
cli = modules['flask.cli']
cli.show_server_banner = lambda *x: None

def randomstr(n=10):
	return ''.join(choice(ascii_lowercase + digits) for _ in range(n))

def randomint(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def gen(name,invite,recapkey,proxy):
    print(f"[token gen] start gen | {proxy}")
    try :
        textres = loads(post("https://discord.com/api/v9/auth/register",timeout=10, proxies={'https': f"socks4://{proxy}"}, json={"fingerprint":"","email": randomstr(n=randint(3, 6)) + randomint(randint(2, 5)) + "@gmail.com","username":name,"password": "Czloed_Dhub@pass","invite":invite,"consent":True,"date_of_birth":"2000-07-12","gift_code_sku_id":"","captcha_key":recapkey}, headers={'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36'}).text)
        discord_token = textres["token"]
        print("[token gen] I Got token | " + discord_token)
        a = open('token.txt', 'a')
        a = a.write(f"{discord_token}\n")
        return True
    except :
        print("[token gen] fail | " + textres["message"])
        return False
        
@app.route('/', methods=['POST'])
def api_login():
    global i
    print("[api] got recap")
    for i in range(20):
        try :
            proxy = proxylist[i]
            i=i+1
        except:
            proxy = proxylist[0]
            i=0
        #executor.submit(gen,request.args['name'],request.args['invite'], request.args['recapkey'], proxy)
        if gen(request.args['name'],request.args['invite'], request.args['recapkey'], proxy):
            return "true"
    return "false"

@app.route('/', methods=['GET'])
def home():
    return "CZLOED Dhub By larinax999 | CZLOED PROJECT"

print("online")
app.run(host='0.0.0.0', port=8080, threaded=True)