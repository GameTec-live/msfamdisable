import time
import subprocess
x = 2

print("""
@(((((((((//////((((((((///////((((((((###(((((//////((((((//(((#####(/////((((/
/(((((//////(((((/////((///((((((((####(//////(####(/////(((((((((((((((((//////
/((((((((((/////(((((((/////((((((//////(//////(((((((((((#%%%%(//////((((((((((
/(((((/(((((((((#####((((((///////(((((((((((((((((((((((((/////(#####(/////%%%%
///#((//////((((((##(((((((((((((/((((((/////((((((((#####(((((((/////(#%%%%%%%%
(//%%%///(////(%%###(((///(((((((//////(((((((######(//////((((((#%%%%%%%%%%%%%%
#%%##%///(((((#%%#((((((//((((@%((/////(/////(#((((######(((%%%%%%%%%%%%%%%%%%%%
((####%%%%%#((#%%&((#((###///(&(((((((//(#//////((((((#%%%%%%#%%%%%%%%%%%%%%%%%#
(((###(#%%%%((#%%%((%%%(((///#//((((((((%##(((((#%%%%%%%%%%#&&&%%%&&&#%%%%%%%%&&
###%##(((//(%(#%&%%%%%%((%///#//(&((#%%%###(((%%%%%%%%%%%%%#&&&%%#&&&%%%&&%%#&&%
/##%%%((((/(%%#(###%%%%##%%#%///&*(%#(((((((((%%%%%%%%%%%%%%&&&%%&&&&%%%&&&&&%%%
//(%%%#(((@&%##((###&##%%#%%&((#%/#%%#####((((%%%%&%%%%%%%%%&&&&&&&&%&&&&&&&&&&&
///%%%###%&&&##(%#%%%##%%%%@%#(&%%#&#%####%@@@%%%&&&%%&&&%%#&&%%%%%%%&&&%%%%%&&&
///###//(%#&@/(&&#%&%%%&%%%%%%%%#####%%%%%%#%%#%&%%%&&&&%&&&%%%%%&&&&&&&%%%#####
(%&&&%/(#%%%&%&@&&@@#(@@%&@###&###&###((%%%###&&&%%%%%%%#&&&%%%&&&&&&%#%%%%###%%
(((#####&&%%%%%%%%%%%%&%%@@&&@&%&@%###((%%%###%%%%%&%/*,,,,***,*#&%####%&&%%%%%%
((((((@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%&####%###%%%&&&%/,,,*.*,,,,,,,*,,,%&&%%%%%%
(#%%%&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%&#(####///%%%&&&%/*****/%&&&#/*,,*,,#%%%%%%%
((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@&&%%#((/%##&&&%/,.*,,/%&*,,**&#,*,#%%%%%%%
(((#####&@&&@@%&&&%%%%%%%%%%%%%%%%&@&%##(##(((&##&&%%/,,,,,,***,*,/&%**,%%%%%%%%
########&((##((@@((@@%&@&%&&%%%%%%%%####(#%&((###%%%%#((////**,****&#,,,#####%%%
###%%%(##((%(((&/(/%((#&%%@&#%@&&&%#####%%%#((##%%%%%%%%%%%%&&&&&&%%%&&%###%%%%%
@&%##%(&(#%#((#//(%#((%%%%&//#/###(/////%%&###%%%%%%&&&%%%%%&%%###%%%%%%%%%%%%%%
(##(((####&#((&((/%#(%(##&((/#/(###((///#@%((#%%%%%%&&%#####%%%#%%%%#*,,#%%%%%%%
(((###%##&##%&%#(%//#%###%((%(((###(((((//#(((%%%%%%%%%###%%###&&&&&#**,%%%%#%&&
(((###%%%#/(%&%##%((@###&###%#((##%%%#((///###%%%%%%&(*,,,(,,,,,,*,,*,**%&%##%&&
/%@%##//%//#@##%&#(&#((#%#%#####%&&&&#((###%##%%%%%&%/,,,**,**,,,*/%#,,,%&%%%&&&
@@@@##//((((((#%%###%%%##%&@&(/(########(##%%%%%%%&&&/**#%%&%%%%%%%%%#&&%%%%%%%%
@@@@@@@@@@(((#%%#(/(%%%######//(%%######//////%%%&&&%%%%%&&&%%%%%%&&&%%%%%%%%%%%
@@@@@@@@@@@@@@@(#(//(((((#######%%###(//(((///%%%%%%%%%%%%%%&&&%%%%%%%%%%%%##@@@
@@@@@@@@@@@@@@@@@@@@@((((((((###%%#####(((((((%%%%%%&&%##%%%&%%###%%%#(@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@(((######(####((((((%%%%%&&&%%%%%%%%%##(@@@@@@@@@@@@@@
""")

time.sleep (1)
print("Part 2! You, as an Adminestartor have to help the Maschine!")
time.sleep(1)
print("First Navigate to C:\Windows\System32")
time.sleep(1)
input("Press Enter to continue...")
print("Then Search in System32 for WpcMon.exe")
time.sleep(1)
input("Press Enter to continue...")
print("Rightclick WpcMon.exe and go to Properties")
input("Press Enter to continue...")
print("Click on the Securety TAB and then Advanced")
input("Press Enter to continue...")
print("On The top of the now open window it says Owner: Trusted Installer")
input("Press Enter to continue...")
print("Click on Change next to the Name")
input("Press Enter to continue...")
print("In the noe open window, is a fiel where it says: Enter the object name")
input("Press Enter to continue...")
print("type in there your Username. If you are unsure, Here it is! ")
subprocess.call([r'Username.bat'])
print("Got It?")
input("Press Enter to continue...")
print("Now press check names and okay!")
input("Press Enter to continue...")
print("Once again, press ok!")
input("Press Enter to continue...")
print("Now click once again click on Advanced")
input("Press Enter to continue...")
print("On the bottom left of the window klick on change permissons")
input("Press Enter to continue...")
print("Now doubleclick on Adminestrators")
input("Press Enter to continue...")
print("Tick the box for Full Control")
input("Press Enter to continue...")
print("Now press ok on every windows and we can modify the next file")
input("Press Enter to continue...")
time.sleep(1)
print("Search in System32 for WpcTok.exe")

while x == 2:

    i = input("Do you have a WpcTok.exe? Y/N")

    if i == 'Y':
        s = input("Are you sure? Y/N")
        if s == 'Y':
            x = 1
        elif s == 'N':
            print("Returning back")
        else:
            print("No Valid Input... Acceptet as No")



    elif  i == 'N':
        s = input("Are you sure? Y/N")
        if s == 'Y':
            x = 0
        elif s == 'N':
            print("Returning back")
        else:
            print("No Valid Input... Acceptet as No") 
    

    else:
        print("No Valid Input! Please Try Again!")
        x = 2




w = open("data.txt", 'w')
w.write(str(x))
w.close()


if x == 1:
    input("Press Enter to continue...")
    print("Rightclick WpcTok.exe and go to Properties")
    input("Press Enter to continue...")
    print("Click on the Securety TAB and then Advanced")
    input("Press Enter to continue...")
    print("On The top of the now open window it says Owner: Trusted Installer")
    input("Press Enter to continue...")
    print("Click on Change next to the Name")
    input("Press Enter to continue...")
    print("In the noe open window, is a fiel where it says: Enter the object name")
    input("Press Enter to continue...")
    print("type in there your Username. If you are unsure, Here it is! ")
    subprocess.call([r'Username.bat'])
    print("Got It?")
    input("Press Enter to continue...")
    print("Now press check names and okay!")
    input("Press Enter to continue...")
    print("Once again, press ok!")
    input("Press Enter to continue...")
    print("Now click once again click on Advanced")
    input("Press Enter to continue...")
    print("On the bottom left of the window klick on change permissons")
    input("Press Enter to continue...")
    print("Now doubleclick on Adminestrators")
    input("Press Enter to continue...")
    print("Tick the box for Full Control")
    input("Press Enter to continue...")
print("Press ok on every window and close Them!")
input("Press Enter to complete Setup!... You are done! Have fun :)")
print("Starting The Programm in 5sec.")
time.sleep(5)
subprocess.call([r'msfamdisable.bat'])