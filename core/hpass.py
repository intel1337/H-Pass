import os
import sys
import base64
import msvcrt
import time 

def freeze():
    print("Press Enter to continue..")
    msvcrt.getch()

def register():
    global username
    username = input("Username : ")
    os.system("cls && title H-Pass - " + username)
    main()

def main():
    print(f"""
    
         __      __ __ 
    |__||__) /\ (_ (_  
    |  ||   /--\__)__) 
                   
    Welcome to H-Pass Again !
        [h] - help
    
    """)
    cmd = input("H-Pass@" + username + ">")
    if cmd == "h":
        print("""command list :
        encode
        exit
        access""")
        freeze()
        boot()
    elif cmd == "encode":
        enc = input("Enter path to the file you want to encode :")
        file_path = enc
        with open(file_path, "rb") as file:
            file_content = file.read()
            encoded_content = base64.b64encode(file_content)
        with open(file_path, "wb") as file:
            file.write(encoded_content)
        boot()
    elif cmd == "exit":
        sys.exit()
    else:
        print("Invalid command")
        time.sleep(1)
        boot()

def boot():
    os.system("cls && title HPASS - " + username)
    main()

register()


