import os
import sys
import random
import time
import colorama
from colorama import Fore
import msvcrt

def freeze():
    msvcrt.getch()

def register():      
    rgstu = input("Username :")
    verif = input("Is this your username ? Y/N :")
    global username
    username = rgstu
    if verif == "Y":
        captcha()
    if verif == "y":
        captcha()
def captcha():
    global cmd
    os.system("cls && title H-Pass - " + username)
    print(f"""
    
         __      __ __ 
    |__||__) /\ (_ (_  
    |  ||   /--\__)__) 
                   
    Welcome to H-Pass !
        Type "start"
    
    """)
    cmd = input(f"H-Pass@" + username + ">")
    if cmd == "start":
        cmd = input("CAPTCHA : a  n  s  w  e  r     f  a  l  s  e    t  o : 500 + 510 >")
    else:
        print("Invalid Command")
        time.sleep(1)
        captcha()

    if cmd == "1010":
        sys.exit(0)
    else:
        import core.hpass

register()

