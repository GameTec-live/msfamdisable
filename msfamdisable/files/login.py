import os
import time
import subprocess
import libary



prot2 = 'Off'
prot = 0
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














def change():
    yn = input("Do you want to change these settings? Y/N")
    if yn == 'Y':
        print("Changing")
    elif yn == 'N':
        print("Aborting...")
        exit(0)
    else:
        change()


    


print("Launching the Editor...")
input("Press Enter to continue...")
print("")
libary.login()

print("The current Infos are:")
print(usr)
print(pswd)
print("Protection:",prot)
change()
print("Please enter the new settings...")
print("Username: ",usr)
usr = str(input("New Username: "))
print("Password: ",pswd)
pswd = str(input("New Password: "))
print("Password On/Off",prot)
prot2 = input("Passwordprotektion? On/Off ")
if prot2 == 'On':
    prot = 1
elif prot2 == 'Off':
    prot = 0
else:
 exit(0)
print("confuguring done!",usr,pswd,prot)
input("Press enter to write and continue")

w = open("login.txt", 'w')
w.write(str(usr)+"\n")
w.write(str(pswd)+"\n")
w.write(str(prot)+"\n")
w.close
