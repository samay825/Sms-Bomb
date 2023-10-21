# colors 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

#----------------modules
from os import system,name
from time import sleep


# -----clear 
system('cls' if name=='nt' else 'clear')

#-------update

system('rm -rf main.py')
sleep(0.1)

system('wget https://raw.githubusercontent.com/samay825/Sms-Bomb/main/main.py')
print(r+"└─ "+w+"\033[1;37m>> Script Updated <<")
sleep(0.5)

# ---------return to main.py file 
system('python main.py' if name=='nt' else 'python3 main.py')

