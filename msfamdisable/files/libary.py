import os
import subprocess


def login():

    prot = 1
    usr = 'none'
    pswd = 'none'
    try:
        r = open("login.txt", 'r')
        raw1 = r.readline().rstrip('\n')
        raw2 = r.readline().rstrip('\n')
        raw3 = r.readline().rstrip('\n')
        r.close()
        usr = str(raw1)
        pswd = str(raw2)
        prot = int(raw3)


    except:
        print("Error! No login.txt file Found!")
        subprocess.call([r'major.bat'])




    if prot == 1:
        print("You have to login!")
        in1 = input("Enter your Username: ")
        in2 = input("Enter your Password: ")
        if in1 == usr:
            if in2 == pswd:
                logindone()
            else:
                wrong(usr,pswd)
        else:
            subprocess.call([r'wrong.bat'])
            login()

def logindone():
    print("Login was Sucsessfull!")


def change():
    subprocess.call([r'login.bat'])

