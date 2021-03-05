import pygame
import pygame_gui
import os
import time
import subprocess

#
#Debug codes:
#User007
#AT642
#
#Error Sheet:
#Error 1 = File not found
#
#Code by GameTec_live
#

i = 0
data = 2



try:
    r = open("data.txt", 'r')
    variable = r.readline()
    r.close()
    data = int(variable)

except:
    print("Error! No data.txt file Found! Please execute setup!")
    time.sleep(2)
    subprocess.call([r'debugconsole.bat'])














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
background.fill(pygame.Color('#0000ff'))

manager = pygame_gui.UIManager((800, 600))

myfont = pygame.font.SysFont('Arial', 28)


textsurface1 = myfont.render('WpcMon.exe', False, (0, 0, 0))



button_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 155), (100, 50)),
                                            text='disable',
                                           manager=manager)

button_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 95), (100, 50)),
                                            text='enable',
                                           manager=manager)



button_rst = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 5), (120, 50)),
                                            text='Restart',
                                           manager=manager)

button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 155), (120, 50)),
                                            text='Help',
                                           manager=manager)

button_settings = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 255), (120, 50)),
                                            text='Settings',
                                           manager=manager)

button_Done = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 355), (120, 50)),
                                            text='Done',
                                           manager=manager)


if data == 1:
    button_four = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 155), (100, 50)),
                                            text='disable',
                                           manager=manager)

    button_three = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 95), (100, 50)),
                                            text='enable',
                                           manager=manager)
    

    textsurface2 = myfont.render('WpcTok.exe', False, (0, 0, 0))

elif data == 2:
    print('Error By reading file: data.txt')
    







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
                    if event.ui_element == button_one:
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
                    if event.ui_element == button_help:
                        print('Starting Help')
                        subprocess.call([r'info.bat'])
            
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_settings:
                        print('Starting settings')
                        subprocess.call([r'settings.bat'])
                       
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_Done:
                        is_running = False   


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_rst:
                        if i == 1:
                            print('restarting!')
                            i = 0
                            time.sleep(3)
                            subprocess.call([r'restart.bat'])
                        else:
                            subprocess.call([r'restarterror.bat'])



            manager.process_events(event)

    except:
        print("Error 1")
        print("Continuing on!")
        subprocess.call([r'minor.bat'])
    if i == 1:
        background.fill(pygame.Color('#ff0000'))
    else:
        background.fill(pygame.Color('#00e600'))


    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)


    window_surface.blit(textsurface1,(340,5))
    

    if data == 1:
        window_surface.blit(textsurface2,(500,5))

    

    if os.path.exists("C:/Windows/System32/WpcMon.exe"):
        textsurface3 = myfont.render('Aktive', False, (0, 0, 0))
        window_surface.blit(textsurface3,(270,155))
    
    if os.path.exists("C:/Windows/System32/WpcMonnot.exe"):
        textsurface3 = myfont.render('Inaktive', False, (0, 0, 0))
        window_surface.blit(textsurface3,(270,155))

    if os.path.exists("C:/Windows/System32/WpcTok.exe"):
        textsurface4 = myfont.render('Aktive', False, (0, 0, 0))
        window_surface.blit(textsurface4,(610,155))

    if os.path.exists("C:/Windows/System32/WpcToknot.exe"):
        textsurface4 = myfont.render('Inaktive', False, (0, 0, 0))
        window_surface.blit(textsurface4,(610,155))










    


    pygame.display.update()