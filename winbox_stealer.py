import os

APPDATA = os.environ['APPDATA']
Winbox = APPDATA + '\\Mikrotik\Winbox\\'

def WinboxSettings():
    try:
        settings = open(Winbox + "settings.cfg.viw", 'r', encoding="utf-8", errors="ignore").read()
        
        addr_pos = settings.find("addr")
        login_pos = settings.find("login")
        
        pwd_pos1 = settings.find("pwd")
        pwd_pos2 = settings.find("pwd", pwd_pos1 + 1)

        if (addr_pos != -1):
            print("Host:", settings[addr_pos + 4:].split("\x05\x00\x03")[0])
            
        if (login_pos != -1):
            print("Login:", settings[login_pos + 5:].split("\x08\x00\x03man")[0])

        if (pwd_pos2 != -1):
            print("Password:", settings[pwd_pos2 + 3:].split("\x0b\x00\x06rneigh")[0])  
            
        open(Winbox + "settings.cfg.viw", 'r').close() 

    except Exception as e:
        print("File not found!")
        print(e)

WinboxSettings()
