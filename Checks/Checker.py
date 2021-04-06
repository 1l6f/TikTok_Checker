import requests
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)
r = requests.session()
c = 0
z = 0
g = Fore.LIGHTGREEN_EX
y = Fore.BLUE
w = Fore.LIGHTWHITE_EX
re = Fore.RED
num = 0
logo ='''
                            ███╗   ███╗███████╗
                            ████╗ ████║██╔════╝
                            ██╔████╔██║███████╗
                            ██║╚██╔╝██║╚════██║
                            ██║ ╚═╝ ██║███████║
                            ╚═╝     ╚═╝╚══════╝
                            |
                            └  TikTok Checker       
                            └  Developer py MS            
                            └  Insta-> @m.1jv
                            └  For Help ↽↽↵  
'''
print(f"{Fore.CYAN}{logo}")
print(Fore.RED+"                            Dont Try To Sell It")


aa = '==========================================================================='
print(f'{Fore.LIGHTCYAN_EX}{aa}')

mq ='''
1 - List Maker User
2 - TikTok-Checker - with sessionid'''
print(f"{Fore.BLUE}{mq}")
ms = input('   └──> ')

if ms =="1":
    print(f"{Fore.BLUE}{'         1 - List Maker User (Mix)'}")
    print(f"{Fore.BLUE}{'         2 - List Maker User (Letters Without { _ . })'}")
    print(f"{Fore.BLUE}{'         3 - List Maker User (Letters Just -> Without { Numbers })'}")
    print(f"{Fore.BLUE}{'         4 - List Maker User (Letters Just -> Without { Numbers and _ . })'}")
    ms1 = input("            └──> ")
    if ms1 == '1':
        # List Maker User (Mix)
        Count = input('               └──> Enter Count -> ')
        Count = int(Count)
        length = input('                  └──> Enter Length -> ')
        length = int(length)
        le = '_.qwertyuiopasdfghjklzxcvbnm123456789'
        for userlist in range(Count):
            userlist = ''
            for userlist2 in range(length):
                userlist += random.choice(le)
            with open('userlist.txt', 'a') as x:
                x.write(userlist + '\n')
                x.close()
        aa = '==========================================================================='
        qq = '                                {DONE}'
        print(f'{Fore.LIGHTCYAN_EX}{aa}')
        print(Fore.LIGHTWHITE_EX + qq + '\n')

    if ms1 == '2':
        # List Maker User (Letters Without { _ . })
        Count = input('               └──> Enter Count -> ')
        Count = int(Count)
        length = input('                  └──> Enter Length -> ')
        length = int(length)
        le = 'qwertyuiopasdfghjklzxcvbnm123456789'
        for userlist in range(Count):
            userlist = ''
            for userlist2 in range(length):
                userlist += random.choice(le)
            with open('userlist.txt', 'a') as x:
                x.write(userlist + '\n')
                x.close()
        aa = '==========================================================================='
        qq = '                                {DONE}'
        print(f'{Fore.LIGHTCYAN_EX}{aa}')
        print(Fore.LIGHTWHITE_EX + qq + '\n')

    if ms1 == '3':
        # List Maker User (Letters Just -> Without { Numbers })
        Count = input('               └──> Enter Count -> ')
        Count = int(Count)
        length = input('                  └──> Enter Length -> ')
        length = int(length)
        le = '_.qwertyuiopasdfghjklzxcvbnm'
        for userlist in range(Count):
            userlist = ''
            for userlist2 in range(length):
                userlist += random.choice(le)
            with open('userlist.txt', 'a') as x:
                x.write(userlist + '\n')
                x.close()
        aa = '==========================================================================='
        qq = '                                {DONE}'
        print(f'{Fore.LIGHTCYAN_EX}{aa}')
        print(Fore.LIGHTWHITE_EX + qq + '\n')

    if ms1 == '4':
        # List Maker User (Letters Just -> Without { Numbers and _ . })
        Count = input('               └──> Enter Count -> ')
        Count = int(Count)
        length = input('                  └──> Enter Length -> ')
        length = int(length)
        le = 'qwertyuiopasdfghjklzxcvbnm'
        for userlist in range(Count):
            userlist = ''
            for userlist2 in range(length):
                userlist += random.choice(le)
            with open('userlist.txt', 'a') as x:
                x.write(userlist + '\n')
                x.close()
        aa = '==========================================================================='
        qq = '                                {DONE}'
    else:
        print(f"{Fore.BLUE}{'         TikTok-Checker - with sessionid'}")
        print(f"{Fore.BLUE}{'         |----------- sessionid'}")
        si = input("                     └──> ")
        a1a = '==========================================================================='
        print(f'{Fore.LIGHTCYAN_EX}{a1a}')
        mma = 'userlist.txt'
        sessionId = si
        user = open(mma).read().splitlines()
        for user in user:
            url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + user + "&app_language=ar"
            payload = ""
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"

            }
            cook = {'sessionid': sessionId}
            res = requests.request("GET", url, data=payload, headers=headers, cookies=cook)
            post = str(res.json()["status_msg"])
            if '"status_code":8,"status_msg"' in res.text:
                print(f'{Fore.RED}{"                                  Sessionid Bad"}')
                print(f'{Fore.RED}{"                     Please try again with another Sessionid"}')
            else:
                if post == "" or "":
                    num += 1
                    print(f'{Fore.GREEN}{"{}: {}".format(num, user.strip())}{Fore.LIGHTCYAN_EX}{" |  Available"}')
                    with open('accountfound.txt', 'a') as x:
                        x.write(user + '\n')
                else:
                    num += 1
                    print(f'{Fore.GREEN}{"{}: {}".format(num, user.strip())}{Fore.RED}{" |  Unavailable"}')
if ms =="2":
    print(f"{Fore.BLUE}{'         | - sessionid'}")
    si = input("            └──> ")
    aa = '==========================================================================='
    print(f'{Fore.LIGHTCYAN_EX}{aa}')
    mma = 'userlist.txt'
    sessionId = si
    user = open(mma).read().splitlines()
    for user in user:
        url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + user + "&app_language=ar"
        payload = ""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"

        }
        cook = {'sessionid': sessionId}
        res = requests.request("GET", url, data=payload, headers=headers, cookies=cook)
        post = str(res.json()["status_msg"])
        if '"status_code":8,"status_msg"' in res.text:
            print(f'{Fore.RED}{"                                  Sessionid Bad"}')
            print(f'{Fore.RED}{"                     Please try again with another Sessionid"}')
        else:
            if post == "" or "":
                num += 1
                print(f'{Fore.GREEN}{"{}: {}".format(num, user.strip())}{Fore.LIGHTCYAN_EX}{" |  Available"}')
                with open('accountfound.txt', 'a') as x:
                    x.write(user + '\n')
            else:
                num += 1
                print(f'{Fore.GREEN}{"{}: {}".format(num, user.strip())}{Fore.RED}{" |  Unavailable"}')
exit()