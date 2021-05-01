import pygame
import pygame_gui
import os
import time
import subprocess
import commandlib
import ctypes

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
        ctypes.windll.user32.MessageBoxW(0, "No login.txt file", "Error!", 1)




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
            ctypes.windll.user32.MessageBoxW(0, "Wrong Username or Password", "Error!", 1)
            login()

def logindone():
    print("Login was Sucsessfull!")


def change():
    print("launching changer...")
    print("")
    login()


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
        ctypes.windll.user32.MessageBoxW(0, "No login.txt file", "Error!", 1)
    
    print("The current Infos are:")
    print(usr)
    print(pswd)
    print("Protection:",prot)
    print("Do you want to change these settings?")
    yn()
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
        change()
    print("confuguring done!",usr,pswd,prot)
    input("Press enter to write and continue")
    w = open("login.txt", 'w')
    w.write(str(usr)+"\n")
    w.write(str(pswd)+"\n")
    w.write(str(prot)+"\n")
    w.close









def yn():
    yn = input("Y/N")
    if yn == 'Y':
        print("Changing")
    elif yn == 'N':
        print("Aborting...")
        exit(0)
    else:
        yn()


def debugconsole():
    command = 'none'

    print("Starting CLI..")
    login()
    commandlib.screenfetchsimple()

    while True:
        command = input("crash@msfamdisable: ")
        commandlib.checkcommand(command)

def settings():

    try:
        r = open("data.txt", 'r')
        variable = r.readline()
        r.close()
        data = int(variable)

    except:
        print("Error! No data.txt file Found! Please execute setup!")
        time.sleep(2)
        debugconsole()



    login()




    pygame.init()

    pygame.display.set_caption('Family Control Settings')
    window_surface = pygame.display.set_mode((700, 250))

    background = pygame.Surface((700, 250))
    background.fill(pygame.Color('#a5fc03'))

    manager = pygame_gui.UIManager((700, 250))

    myfont = pygame.font.SysFont('Arial', 28)



    button_one = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 155), (100, 50)),
                                                text='disable',
                                            manager=manager)

    button_two = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 95), (100, 50)),
                                                text='enable',
                                            manager=manager)
    button_four = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 155), (100, 50)),
                                                text='disable',
                                            manager=manager)

    button_three = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((510, 95), (100, 50)),
                                                text='enable',
                                            manager=manager)

    button_rst = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 5), (120, 50)),
                                                text='Done',
                                            manager=manager)

    button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 155), (120, 50)),
                                                text='Console',
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
                        if event.ui_element == button_one:
                            print('Off!')
                            data = 0

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_two:
                            print('On!')
                            data = 1
                                            
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_four:
                            print('Off!')
                            os.remove("updates.txt")
                            ctypes.windll.user32.MessageBoxW(0, "You have made changes!", "Info", 1)
                            

                            


                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_three:
                            print('On!')
                            x = open("updates.txt", 'w')
                            x.close()
                            ctypes.windll.user32.MessageBoxW(0, "You have made changes!", "Info", 1)
                

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_rst:
                            window_surface = pygame.display.set_mode((800, 600))
                            background = pygame.Surface((800, 600))
                            manager = pygame_gui.UIManager((800, 600))
                            is_running = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_help:
                            print('Starting Console')
                            debugconsole()





                manager.process_events(event)

        except:
            print("Error 1")
            print("Continuing on!")
            ctypes.windll.user32.MessageBoxW(0, "An minor error occured! Errorcode: 1", "Error!", 1)
        


        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)


        textsurface1 = myfont.render('WpcTok', False, (0, 0, 0))
        textsurface2 = myfont.render('Updates', False, (0, 0, 0))
        window_surface.blit(textsurface1,(340,5))
        window_surface.blit(textsurface2,(500,5))

        
        if data == 1:
            textsurface4 = myfont.render('On', False, (0, 0, 0))
            window_surface.blit(textsurface4,(270,65))

        if data == 0:
            textsurface4 = myfont.render('Off', False, (0, 0, 0))
            window_surface.blit(textsurface4,(270,65))
    


        if os.path.exists("C:/Windows/System32/WpcTok.exe"):
            textsurface4 = myfont.render('Found', False, (0, 0, 0))
            window_surface.blit(textsurface4,(270,155))

        elif os.path.exists("C:/Windows/System32/WpcToknot.exe"):
            textsurface4 = myfont.render('Found', False, (0, 0, 0))
            window_surface.blit(textsurface4,(270,155))

        else:
            textsurface4 = myfont.render('Not Found', False, (0, 0, 0))
            window_surface.blit(textsurface4,(230,155))


        w = open("data.txt", 'w')
        w.write(str(data))
        w.close()


        


        pygame.display.update()

