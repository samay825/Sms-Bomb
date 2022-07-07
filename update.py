#----------------modules
from os import system,name
from time import sleep
from colorama import *

# -----clear 
system('cls' if name=='nt' else 'clear')

#-------update
system('mv main.py old_main.py')
system('wget https://raw.githubusercontent.com/samay825/Sms-Bomb/main/main.py')
print(Fore.RED+"[+] Script Updated! ")

# ---------return to main.py file 
system('python main.py' if name=='nt' else 'python3 main.py')

