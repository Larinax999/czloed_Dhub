from colorama import Fore, Style, init
from twocaptcha import TwoCaptcha
from time import sleep, strftime, localtime
from os import system, name
from concurrent.futures import ThreadPoolExecutor
from random import randint
from bs4 import BeautifulSoup, SoupStrainer
import sys, random, colorama, requests, string, flask, logging, json, urllib, base64
from flask import request
from flask_cors import CORS

texttime = (Fore.LIGHTBLUE_EX + strftime("%H:%M:%S ", localtime()) + Fore.RESET)
texterror = (Fore.LIGHTRED_EX + '[ERROR] ' + Fore.RESET)
textwait = (Fore.LIGHTYELLOW_EX + '[Waiting...] ' + Fore.RESET)
textpass = (Fore.LIGHTGREEN_EX + '[SUCCESS] ' + Fore.RESET)
textwarn = (Fore.LIGHTMAGENTA_EX + '[WARNING] ' + Fore.RESET)

def clear():
    system('cls' if name=='nt' else 'clear')
    
def title(text):
    if name == 'nt' :
        system(f'title [CZLOED Dhub By larinax999] - {text} ')
    else :
        pass

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print(texterror + "Try again.")
            input("Press Enter to continue...")
            continue
        else:
            return userInput
            break
            
def headers(token = "", mail = False) :
    if token :
        if mail :
            return {'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36', 'authorization': "Bearer " + token}
        else :
            return {'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36', 'authorization': token}
    else :
        return {'Content-Type': 'application/json','user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.122 Safari/537.36'}

def randomstr(chars = string.ascii_lowercase + string.digits, n=10):
	return ''.join(random.choice(chars) for _ in range(n))

def randomint(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

def logo():
    text = """
 ██████╗███████╗██╗      ██████╗ ███████╗██████╗     ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝╚══███╔╝██║     ██╔═══██╗██╔════╝██╔══██╗    ██╔══██╗██║  ██║██║   ██║██╔══██╗
██║       ███╔╝ ██║     ██║   ██║█████╗  ██║  ██║    ██║  ██║███████║██║   ██║██████╔╝
██║      ███╔╝  ██║     ██║   ██║██╔══╝  ██║  ██║    ██║  ██║██╔══██║██║   ██║██╔══██╗
╚██████╗███████╗███████╗╚██████╔╝███████╗██████╔╝    ██████╔╝██║  ██║╚██████╔╝██████╔╝
 ╚═════╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
    """
    bad_colors = ['LIGHTCYAN_EX', 'CYAN']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color in bad_colors]
    print(Fore.RED + "\t\t\t    BY. CZLOED PROJECT | Larinax999\n" + Fore.RESET)
    
clear()
logo()

config = json.load(open('config.json'))
app = flask.Flask(__name__)
app.config["DEBUG"] = False
solver = TwoCaptcha(config['2cap_key'])
log = logging.getLogger('werkzeug')
log.disabled = True
CORS(app)

def start() :
    try :
        title("Menu")
        menu()
    except : 
        print(textpass + "Bye")
        sleep(2)
 
def menu() : 
    while True:
        try :
            print(Fore.LIGHTMAGENTA_EX + """
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    [0] exit [1] token generator [2] token generator with 2cap [3] Discord Raid Tool (Soon...) [3] settings
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""")
            choose = inputNumber(textwait + "> ")
            if choose == 0 :
                print(textpass + "Bye")
                sleep(2)
                break
            elif choose == 1 : 
                clear()
                logo()
                token_gen()
            elif choose == 2 :
                clear()
                logo()
                token_gen_with_2cap()
            elif choose == 3 :
                clear()
                logo()
                Raid_tool()
        except :
            print(texterror + "Try again.")
            input("Press Enter to continue...")
            continue
        else:
            break
            

# cloudflare
def bypass_manybaht_invite(token, invite):
    session = requests.Session()
    codeurl = json.loads(session.post("https://discord.com/api/v9/oauth2/authorize?client_id=757580084830797874&response_type=code&redirect_uri=https%3A%2F%2Fvanguard.manybahtpage.com%2Fapi%2Fauth%2Fdiscord%2Fcallback&scope=identify%20email%20guilds%20guilds.join", json={"permissions":"0","authorize":True}, headers=headers(token)).text)
    print(codeurl['location'])
    print(session.get(codeurl['location'], headers=headers()).text)
    print(session.get('https://vanguard.manybahtpage.com/success', headers=headers()).text)
    result = solver.hcaptcha(sitekey='f0f298e4-dd6a-464e-968e-3e7dda393810',url='https://vanguard.manybahtpage.com/verify/')
    print(session.post("https://vanguard.manybahtpage.com/api/discord/join", json={"code": invite, "htoken": result['code']}, headers=headers()).text)

def bypass_fortune_invite(token, invite):
    session = requests.Session()
    codeurl = json.loads(session.post("https://discord.com/api/v9/oauth2/authorize?client_id=618441438564188196&response_type=code&redirect_uri=https%3A%2F%2Fftune.app%2Flogin&scope=identify%20guilds%20guilds.join", json={"permissions":"0","authorize":True}, headers=headers(token)).text)
    print(codeurl['location'])
    session.get(codeurl['location'], headers=headers())
    htmltoken = session.get('https://ftune.app/?logged=true', headers=headers()).text
    #print(htmltoken)
    soup = BeautifulSoup(htmltoken, "html.parser")
    s = str(soup.find_all('script')[0])
    s = s.split('","')
    print(session.post("https://ftune.app/_go/" + invite, headers=headers(s[-2])).text)
    
def bypass_aria(msg, chid, guild_id): # check in v2
    def sendmsg():
        requests.post(f"https://discord.com/api/v9/channels/{chid}/messages", json=data, headers=headers(token)).text
    for a in len(msg):
        data = {"content":msg[a],"nonce":randomint(18),"tts":False}
        print(requests.post(f"https://discord.com/api/v9/channels/{chid}/messages", json=data, headers=headers(token)).text) #, referrer=f"https://discord.com/channels/{guild_id}/{chid}"

def bypass_server_cap(token):
    send_livesteam_api(token, config['ch'], config['guild'])
    getchid = json.loads(requests.post("https://discord.com/api/v9/users/@me/channels", json={"recipients":["512333785338216465"]}, headers=headers(token)).text)
    #print(getchid)
    msgimg = json.loads(requests.get(f"https://discord.com/api/v9/channels/{getchid['id']}/messages?limit=50", headers=headers(token)).text)
    #print(msgimg)
    print(msgimg[0]['embeds'][0]['image']['url'])
    imgraw = requests.get(msgimg[0]['embeds'][0]['image']['url'], headers=headers())
    uri = ("data:" + imgraw.headers['Content-Type'] + ";" + "base64," + base64.b64encode(imgraw.content).decode("utf-8"))
    result = solver.normal(uri, hintText='same picture')
    print(result['code'])
    data = {"content":result['code'],"nonce":randomint(18),"tts":False}
    print(requests.post(f"https://discord.com/api/v9/channels/{getchid['id']}/messages", json=data, headers=headers(token)).text)
    return "Done"
    
def send_livesteam_api(token, ch, guild) :
    return requests.post(f"http://43.228.86.64:8080/?token={token}&ch={ch}&guild={guild}").text


def allzone_bypass(token):
    print(requests.post("https://discord.com/api/v9/guilds/780017655595008011/requests/@me",json={"version":"2021-03-19T02:35:32.908000+00:00","form_fields":[{"field_type":"TERMS","label":"อ่านและยอมรับกฎของเซิร์ฟเวอร์","values":["เข้ามาแล้วอย่าลืมยืนยันตัวตน ✅","อย่าลืมอ่านกฎของเซิร์ฟเวอร์ 📝","ขอให้สนุกกับ AllZone Community  ✨"],"required":True,"response":True}]},headers=headers(token)))
    data = {"content":"!สมัคร","nonce":randomint(18),"tts":False}
    print(requests.post(f"https://discord.com/api/v9/channels/790070470606979102/messages", json=data, headers=headers(token)).text)
    getchid = json.loads(requests.post("https://discord.com/api/v9/users/@me/channels", json={"recipients":["798813313349713921"]}, headers=headers(token)).text)
    #print(getchid)
    msg = json.loads(requests.get(f"https://discord.com/api/v9/channels/{getchid['id']}/messages?limit=50", headers=headers(token)).text)
    print(msg)
    #request.post(msg[], data="g-recaptcha-response=")

def token_gen():
    global config
    print(textwarn + f"username : {config['username']} | invite : {config['invite_link']}")
    @app.route('/', methods=['POST'])
    def api_login():
        print("Start gen token")
        register_data = {"fingerprint":"","email": randomstr(n=randint(1, 6)) + randomint(randint(1, 5)) + "@gmail.com","username":config['username'],"password": randomstr(n=randint(4, 6)) + randomint(randint(3, 6)),"invite":config['invite_link'],"consent":True,"date_of_birth":"1998-04-10","gift_code_sku_id":"","captcha_key":request.args['recapkey']}
        textres = json.loads(requests.post("https://discord.com/api/v8/auth/register", json=register_data, headers=headers()).text)
        print(textres)
        print(f"{textpass}| {textres['token']}")
        sleep(1)
        #print(bypass_server_cap(textres['token']))
        #print(bypass_fortune_invite(textres['token'], ""))
        allzone_bypass(textres['token'])
        #print(send_livesteam_api(textres['token'], config['ch'], config['guild']))
        a = open('token.txt', 'a')
        a = a.write(f"{textres['token']}\n")
        return {"message": "DONE", "token": textres['token']}
        '''
        except :
            try :
                print(f"{texterror}| {textres['message']} | {textres['retry_after']}")
                return {"message": textres['message'], "cooldown": textres['retry_after']}
            except :
                return {"message": "Fail Try Again"}
        '''
        #print(textpass + "token : " + textres['token'])

    @app.route('/', methods=['GET'])
    def home():
        return "CZLOED Dhub By larinax999 | CZLOED PROJECT"

    app.run(host='localhost', port=80, threaded=True)
    
def token_gen_with_2cap():
    global config
    for x in range(int(config['tokenc'])) :
        print(textwarn + f"username : {config['username']} | invite : {config['invite_link']}")
        result = solver.hcaptcha(sitekey='f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34',url='https://discord.com/register')
        register_data = {"fingerprint":"","email": randomstr(n=randint(2, 6)) + randomint(randint(2, 5)) + "@gmail.com","username":config['username'],"password": randomstr(n=randint(4, 6)) + randomint(randint(3, 6)),"invite":config['invite_link'],"consent":True,"date_of_birth":"1998-04-10","gift_code_sku_id":"","captcha_key":result['code']}
        print(textpass + "Captcha Solved")
        textres = json.loads(requests.post("https://discord.com/api/v8/auth/register", json=register_data, headers=headers()).text)
        print(textres)
        try :
            print(f"{textpass}| {textres['token']}")
            a = open('token.txt', 'a')
            a = a.write(f"{textres['token']}\n")
        except :
            try :
                register_data = {"fingerprint":"","email": randomstr(n=randint(1, 7)) + randomint(randint(1, 6)) + "@gmail.com","username":config['username'],"password": randomstr(n=randint(4, 6)) + randomint(randint(3, 6)),"invite":config['invite_link'],"consent":True,"date_of_birth":"1998-04-10","gift_code_sku_id":"","captcha_key":result['code']}
                texstres =requests.post("https://discord.com/api/v8/auth/register", json=register_data, headers=headers())
                print(f"{textpass}| {textres['token']}")
                a = open('token.txt', 'a')
                a = a.write(f"{textres['token']}\n")
            except :
                print(f"{texterror}| {texstres}")
        sleep(122)
        
def token_gen_test(token_captcha):
    global config
    print(textwarn + f"username : {config['username']} | invite : {config['invite_link']}")
    register_data = {"fingerprint":"","email": randomstr(n=randint(2, 6)) + randomint(randint(2, 5)) + "@gmail.com","username":config['username'],"password": randomstr(n=randint(4, 6)) + randomint(randint(3, 6)),"invite":config['invite_link'],"consent":True,"date_of_birth":"1998-04-10","gift_code_sku_id":"","captcha_key":token_captcha}
    textres = json.loads(requests.post("https://discord.com/api/v8/auth/register", json=register_data, headers=headers()).text)
    print(textres)

def Raid_tool(): 
    print("Soon...")
    input("Press Enter to continue...")
    
def verify_mail(token_discord) :
    domain = json.loads(requests.get("https://api.mail.tm/domains", headers=headers()).text)
    email = domain["hydra:member"][0]["domain"]
    print(domain["hydra:member"][0])
    email = f"{randomstr(n=randint(2, 6)) + randomint(randint(2, 5))}@{email}"
    password = randomstr(n=randint(4, 6)) + randomint(randint(3, 6))
    print(email)
    print(password)
    requests.post("https://api.mail.tm/accounts",json={"address":email,"password":password}, headers=headers())
    token = json.loads(requests.post("https://api.mail.tm/token",json={"address":email,"password":password}, headers=headers()).text)["token"]
    message = json.loads(requests.get("https://api.mail.tm/messages", headers=headers(token, 1)).text)
    msg_id = message["hydra:member"][0]["id"]
    message = json.loads(requests.get(f"https://api.mail.tm/messages/{msg_id}", headers=headers(token, 1)).text)["text"]
 
def verify_phone(token_discord) :
    pass
    
#fingerprint_json = ss.get("https://discordapp.com/api/v6/experiments", timeout=conf['timeout'], headers=headers, verify=False).text
#fingerprint = json.loads(fingerprint_json)["fingerprint"]
#def __get_super_properties(self):
        # Create X-Super-Properties
        #super_properties = {
        #    "os": "Windows",
        #    "browser": "Firefox",
        #    "browser_user_agent": self.user_agent,
        #    "browser_version": 85.0,
        #    "os_version": 10.0,
        #    "release_channel": "stable",
         #   "client_build_number": 75603,
        #    "client_event_source": None,
        #    "referrer": "",
        #    "referring_domain": "",
        #    "referring_domain_current": ""
        #}
        #{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"0.1.7","os_version":"10.0.18363","os_arch":"x64","system_locale":"en-US","client_build_number":88181,"client_event_source":null}
        #Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.7 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36
        #b64_sp = base64.b64encode((str(super_properties).encode()))
        #self.super_properties = b64_sp.decode()
        #return self.super_properties
#smsResponse = requests.get('http://smspva.com/priemnik.php?metod=get_number&country=' + conf['smspva_region'] + '&service=opt45&apikey=' + conf['smspva_api_key'], timeout=conf['timeout'])
#number = None
#try:
    #smsResponsJSON = json.loads(smsResponse.text)
    #if smsResponsJSON['response'] == 2:
        #print("[SMSPVA] No number found in the region chosen. Will retry in one minute.")
    #number = smsResponsJSON['CountryCode'] + smsResponsJSON['number']
#except:
    #print(smsResponse.text)
    #time.sleep(3)

    
    
#token_gen()
token_gen_test("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzIjoyLCJ0IjoiaiIsImQiOiJVQnhEVnFuRnl2cGlnSXJRTkx1NHNwS1E0NzZIcVI4UzhwZmRFVGtWU21WRXA4cEFmY0dOclZZdEQ2UkxNMG5kTEl1NFd0dDhveWhQY1BkOWpQMTZwdlVaaERQeWdJeVovQzA5OW1ubXNXc1BYbTBUTTVMeWxaL3FvZzJ5ZGpzN1FhZFF0UGo0ZFZXRHdubDVqRjBUZml4dGpjdklnVTIvVXI5ejlsc2NISTkyWExHZGl2dzh0bVFjcGc9PWFhdk5wenZmUmZySzhZY1IiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvNjYzMWVjNTIiLCJlIjoxNjI0MzgwMjM0fQ.7V3bmpGRq1D76efQ4YdMEaTHptpfHUZX1bnAnmQLxV0")
#token_gen_with_2cap()
#bypass_fortune_invite("NzY5ODU0NjU1ODY1ODE1MDgw.YFt5Rg.UaDF6Q8Qm4S5_9i1ewLG5fAX4t8", "Ayee")
#bypass_server_cap("NzY5ODU0NjU1ODY1ODE1MDgw.YFt5Rg.UaDF6Q8Qm4S5_9i1ewLG5fAX4t8")
#send_livesteam_api("NzY5ODU0NjU1ODY1ODE1MDgw.YFt5Rg.UaDF6Q8Qm4S5_9i1ewLG5fAX4t8", config['ch'], config['guild'])
#allzone_bypass("NzY5ODU0NjU1ODY1ODE1MDgw.YFt5Rg.UaDF6Q8Qm4S5_9i1ewLG5fAX4t8")
#verify_mail("token")
#verify_phone("token")
#start()