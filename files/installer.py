import time
import subprocess
import os

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
print("Part 2! ")

time.sleep(1)
print("Scanning files")

if os.path.exists('C:\Windows\System32\WpcTok.exe'):
    print ("WpcTok.exe found")
    x = 1



else:
    print ("WpcTok.exe not found")
    x = 0

w = open("data.txt", 'w')
w.write(str(x))
w.close()
subprocess.call([r'start.bat'])