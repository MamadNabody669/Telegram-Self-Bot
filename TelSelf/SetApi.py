import colorama
from colorama import Back , Fore
colorama.init(autoreset=True)

apiHash = input(Fore.GREEN+"Enter Your api Hash : ")

apiid = input(Fore.GREEN+"Enter Your api ID: ")

license = input(Fore.RED+"Enter Lincens : ")
if(license=="mamadnabody90901"):
    print(Fore.YELLOW+"Lincense Current")
else:
    print(Fore.YELLOW+"wrong")
    exit()