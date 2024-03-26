import time
import os
import shutil

os_path = ""
username = ""
password = ""
changeConfig = False

def confirmConfig():
    global changeConfig
    global os_path
    global username
    global password
    
    print("Writed info:")
    print("[1] {}".format(os_path))
    print("[2] {}".format(username))
    print("[3] {}".format(password))
    confirm = input("Do you confirm the information? If not, write the configuration number to change it, if you do not want to change, press Enter: ")
    if confirm == "":
        install()
    elif confirm == "1":
        changeConfig = True
        setOsPath()
    elif confirm == "2":
        changeConfig = True
        setUsername()
    elif confirm == "3":
        changeConfig = True
        setPasssword()

def setOsPath():
    global changeConfig
    global os_path 
    os_path = input("Write path to install os(if you want install to default path, press enter): ")
    if os_path == "":
            os_path = "C:/Program Files (x86)"
    if  changeConfig == True:
        changeConfig = False
        confirmConfig()
def setUsername():
    global changeConfig
    global username
    username = input("Write the username for the OS: ")
    if username == "":
        setUsername()
    if changeConfig == True:
        changeConfig = False
        confirmConfig()
def setPasssword():
    global changeConfig
    global password
    password = input("Write a password for your user: ")
    if password == "":
        setPasssword()
    if changeConfig == True:
        changeConfig = False
        confirmConfig()
    
def install():
    global os_path
    global username
    global password
    
    print("Create os directory...")
    if(os.path.exists(os_path)):
        print("Directory exists")
    else:
        os.mkdir(os_path)
    time.sleep(1)
    print("Copy files to os directory...")
    installer_path = "./"
    shutil.copytree(installer_path, os_path + "/DevOS")
    shutil.rmtree(os_path + "/DevOS/.git")
    print("Install complete.")

def startInstall():
    print("Load installer...")
    time.sleep(3)
    print("Welcome to DevOS installer!")

    setOsPath()
    setUsername()
    setPasssword()
    confirmConfig()
    
#Start install
startInstall()