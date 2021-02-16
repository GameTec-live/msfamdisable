import pygame
import pygame_gui
import os
import time
import subprocess


#Error Sheet:
#Error 1 = File not found
#
#Code by GameTec_live
#

i = 0


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
pygame.init()

pygame.display.set_caption('Family Control')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ff0000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 155), (100, 50)),
                                            text='disable',
                                           manager=manager)

button_four = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 155), (100, 50)),
                                            text='disable',
                                           manager=manager)

button_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 95), (100, 50)),
                                            text='enable',
                                           manager=manager)

button_three = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 95), (100, 50)),
                                            text='enable',
                                           manager=manager)

text_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((340, 5), (120, 50)),
                                            text='WpcMon.exe',
                                           manager=manager)

text_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 5), (120, 50)),
                                            text='WpcTok.exe',
                                           manager=manager)

button_rst = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 5), (120, 50)),
                                            text='Restart',
                                           manager=manager)



clock = pygame.time.Clock()
is_running = True

while is_running:
    try:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        print('Off!')
                        i = 1
                        os.rename(r'C:/Windows/System32/WpcMon.exe',r'C:/Windows/System32/WpcMonnot.exe')

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_two:
                        print('On!')
                        i = 1
                        os.rename(r'C:/Windows/System32/WpcMonnot.exe',r'C:/Windows/System32/WpcMon.exe')
                                        
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_four:
                        print('Off!')
                        i = 1
                        os.rename(r'C:/Windows/System32/WpcTok.exe',r'C:/Windows/System32/WpcToknot.exe')


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_three:
                        print('On!')
                        i = 1
                        os.rename(r'C:/Windows/System32/WpcToknot.exe',r'C:/Windows/System32/WpcTok.exe')


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_rst:
                        if i == 1:
                            print('restarting!')
                            i = 0
                            time.sleep(1)
                            subprocess.call([r'restart.bat'])
                        else:
                            print("You have to make changes!")



            manager.process_events(event)

    except:
        print("Error 1")
        print("Continuing on!")



    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()