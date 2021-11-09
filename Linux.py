#!/usr/bin/env python3
import os
print("searching save wifi in system.....")
path = "/etc/NetworkManager/system-connections"
os.chdir(path)
wifiname = os.listdir()
print(f"Geting {len(wifiname)} wifi in system")
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("----------------------------------------------")

for wifi in wifiname:
    try:
        files=open(wifi,"r")
        files=files.read()
        files=files.split('\n')
        wifiname=[b.split("=")[1] for b in files if "id=" in b][0]
        password=[b.split("=")[1] for b in files if "psk=" in b][0]
        #print(wifiname)
        #print(password)
        print("{:<30}| {:<}".format(wifiname , password))
    except PermissionError:    
        print("this files need an root permission to read acces \n just use sudo before name")
        exit()
    except IndexError:
            print("{:<30}| {:<}".format(wifiname , ''))
