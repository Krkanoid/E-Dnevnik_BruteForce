import random
import pyautogui
import time
import socket
from colorama import init, Fore, Back, Style
init(convert=True)


print("""
██████╗░██████╗░██╗░░░██╗████████╗███████╗░░░░░░███████╗░█████╗░██████╗░░█████╗░███████╗
██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝░░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░█████╗█████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░
██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░╚════╝██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░
██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗░░░░░░██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗
""")


def bruteforce():
    print(Fore.GREEN + "[0] Izlaz iz programa.")
    print(Fore.GREEN + "[1] Kodovi samo od brojeva.")
    print(Fore.GREEN + "[2] Kodovi samo od slova.")
    print(Fore.GREEN + "[3] Kodovi i od slova i brojeva.")
    for krki in range(2):
        print("")
    unos = str(input(Fore.WHITE + "[+] Unesi odgovor: "+Fore.RED))
    if(unos == 0):
        quit()
    elif(unos == "1"):
        velicina = int(input(Fore.WHITE+"[+] Unesi koliko pokušaja želiš: "))
        print("")
        print("")
        x = range(5)
        for j in (x):
            print(j)
            time.sleep(1)
        for i in range(velicina):
            tabla_prva = random.choice(["1","2","3","4","5","6","7","8","9","0"])
            tabla_druga = random.choice(["1","2","3","4","5","6","7","8","9","0"])
            tabla_treca = random.choice(["1","2","3","4","5","6","7","8","9","0"])
            tabla_cetvrta = random.choice(["1","2","3","4","5","6","7","8","9","0"])
            tabla = tabla_prva+tabla_druga+tabla_treca+tabla_cetvrta
            pyautogui.write(tabla)
            pyautogui.press("enter")
            print(Fore.RED + "["+Fore.GREEN +"+"+Fore.RED+"]"+Fore.WHITE+ " Iskorišten je broj ---> "+Fore.BLUE+f"{tabla}")
    elif(unos == "2"):
        velicina = int(input(Fore.WHITE+"[+] Unesi koliko pokušaja želiš: "))
        z = range(5)
        for m in (z):
            print(m)
            time.sleep(1)
        for p in range(velicina):
            code = ["A","B","C","D","E","F","G","H",
                 "I","J","K","L","M","N","O","P",
                 "R","S","T","U","V","Z","Q","Y",
                 "X","a","b","c","d","e","f","g",
                 "h","j","k","l","m","n","o","p",
                 "r","s","t","u","v","z","q","x",
                 "y",
            ]
            k,l,r,p = random.choice(code),random.choice(code),random.choice(code),random.choice(code)
            slova = k+l+r+p
            pyautogui.write(slova)
            pyautogui.press("enter")
            print(Fore.RED + "["+Fore.GREEN +"+"+Fore.RED+"]"+Fore.WHITE+ " Iskorišten je broj ---> "+Fore.BLUE+f"{slova}")
    elif(unos == "3"):
        velicina = int(input(Fore.WHITE+"[+] Unesi koliko pokušaja želiš: "+Fore.RED))
        for krki in range(2):
            print("")
        z = range(5)
        for m in (z):
            print(Fore.WHITE + f"Pokretanje -------> {m} sec.")
            time.sleep(1)
        for krkil in range(2):
            print("")
        for gag in range(velicina):
            znakovi = [
                 "A","B","C","D","E","F","G","H",
                 "I","J","K","L","M","N","O","P",
                 "R","S","T","U","V","Z","Q","Y",
                 "X","a","b","c","d","e","f","g",
                 "h","j","k","l","m","n","o","p",
                 "r","s","t","u","v","z","q","x",
                 "1","2","3","4","5","6","7","8",
                 "9","0","8","9","0",
                 "y","1","2","3","4","5","6","7"
            ]
            k,l,r,p = random.choice(znakovi),random.choice(znakovi),random.choice(znakovi),random.choice(znakovi)
            s,f,u,q = random.choice(znakovi),random.choice(znakovi),random.choice(znakovi),random.choice(znakovi)
            sve_skupa = k+l+r+p+s+f+u+q
            pyautogui.write(sve_skupa)

            pyautogui.press("enter")
            pyautogui.click()
            ip = (socket.gethostbyname(socket.gethostname()))
            plus = "\033[1m"+Fore.WHITE + "["+Fore.RED +"+"+Fore.WHITE+"]"
            poruka = "\033[0m"+Fore.GREEN+ " Iskorišten je broj"+Fore.WHITE + "---> "
            kod_poruka = "\033[1m"+Fore.BLUE+f"{sve_skupa}"+"\033[0m"+Fore.WHITE
            razmak_crta = "    ||     "
            ip_address = Fore.GREEN+"IP-ADDRESS: "+"\033[1m"+Fore.BLUE+ip+Fore.WHITE
            iskoristeni_kodovi = Fore.GREEN+"Broj iskorištenih kodova ---> "+"\033[1m"+"\033[0m"+Fore.BLUE+f"{gag}"+"\033[0"
            print(plus+poruka+kod_poruka+razmak_crta+ip_address+razmak_crta+iskoristeni_kodovi)

bruteforce()
