import pygame
import pygame_gui
import os
import time
import subprocess
import commandlib
import ctypes
from cryptography.fernet import Fernet
import base64


key=b'gVn0XxalByeYBM2qXSCXK5T1MBITKEpe3nzS9zl624g='

def recover():
    r = open("login.dll", 'r')
    tmp1 = r.readline().rstrip('\n')
    tmp2 = r.readline().rstrip('\n')
    tmp3 = r.readline().rstrip('\n')
    tmp4 = r.readline().rstrip('\n')
    r.close()
    w = open("login.dll", 'w')
    w.write(str(tmp1)+"\n")
    w.write(str(tmp2)+"\n")
    w.write(str(tmp3)+"\n")
    w.write(str("0")+"\n")
    w.write(str("0")+"\n")
    w.close()

def hard_reset():
    w = open("login.dll", 'w')
    w.write(str("gAAAAABgt9XqVARLUQ7D4Gf5WCIyneII2oww_YlX6LJNgVYNWT4DsZaKCM8OeGE4LV3cvRDdFkmeUq4o20O86vCB32qnHCjtvg==")+"\n")
    w.write(str("gAAAAABgt9XqVARLUQ7D4Gf5WCIyneII2oww_YlX6LJNgVYNWT4DsZaKCM8OeGE4LV3cvRDdFkmeUq4o20O86vCB32qnHCjtvg==")+"\n")
    w.write(str("gAAAAABguJNW2FfLrOjBHZ73a0a0-lQMWk0K72NqXcj19WHId-RZuQjR7a3S-mlVCfbLkPk8GmoI4uITq_29HOcKyVy8e0x4qA==")+"\n")
    w.write(str("0")+"\n")
    w.write(str("0")+"\n")
    w.close()

def read_data():
    r = open("login.dll", 'r')
    usr = r.readline().rstrip('\n')
    pswd = r.readline().rstrip('\n')
    prot = r.readline().rstrip('\n')
    updates = r.readline().rstrip('\n')
    data = r.readline().rstrip('\n')
    r.close()
    return usr, pswd, prot, updates, data


def crypt(data):
    encrypt = Fernet(key).encrypt(data.encode())
    return encrypt

def encrypt(data):
    decrypt = Fernet(key).decrypt(data).decode()
    return decrypt

def login():

    prot = 1
    usr = 'none'
    pswd = 'none'
    try:
        r = open("login.dll", 'r')
        raw1 = r.readline().rstrip('\n')
        raw2 = r.readline().rstrip('\n')
        raw3 = r.readline().rstrip('\n')
        r.close()
        usr = encrypt(str(raw1).encode('ascii'))
        pswd = encrypt(str(raw2).encode('ascii'))
        prot = int(encrypt(str(raw3).encode('ascii')))


    except:
        print("Error! No login.dll file Found!")
        ctypes.windll.user32.MessageBoxW(0, "No login.dll file", "Error!", 1)

    if prot == 1:
        print("You have to login!")
        in1 = input("Enter your Username: ")
        in2 = input("Enter your Password: ")
        if in1 == usr:
            if in2 == pswd:
                logindone()
            else:
                ctypes.windll.user32.MessageBoxW(0, "Wrong Username or Password", "Error!", 1)
                login()
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
        r = open("login.dll", 'r')
        raw1 = r.readline().rstrip('\n')
        raw2 = r.readline().rstrip('\n')
        raw3 = r.readline().rstrip('\n')
        r.close()
        usr = encrypt(str(raw1).encode('ascii'))
        pswd = encrypt(str(raw2).encode('ascii'))
        prot = int(encrypt(str(raw3).encode('ascii')))
    except:
        print("Error! No login.dll file Found!")
        ctypes.windll.user32.MessageBoxW(0, "No login.dll file", "Error!", 1)
    
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
    w = open("login.dll", 'w')
    w.write(crypt(str(usr)).decode('ascii')+"\n")
    w.write(crypt(str(pswd)).decode('ascii')+"\n")
    w.write(crypt(str(prot)).decode('ascii'))
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

    tmp1,tmp2,tmp3,tmp4,data =read_data()

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
    button_fix = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 90), (120, 50)),
                                                text='Fix-bug',
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
                            r = open("login.dll", 'r')
                            tmp1 = r.readline().rstrip('\n')
                            tmp2 = r.readline().rstrip('\n')
                            tmp3 = r.readline().rstrip('\n')
                            tmp4 = r.readline().rstrip('\n')
                            r.close()
                            w = open("login.dll", 'w')
                            w.write(str(tmp1)+"\n")
                            w.write(str(tmp2)+"\n")
                            w.write(str(tmp3)+"\n")
                            w.write(str(tmp4)+"\n")
                            w.write(str(data)+"\n")
                            w.close()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_two:
                            print('On!')
                            data = 1
                            r = open("login.dll", 'r')
                            tmp1 = r.readline().rstrip('\n')
                            tmp2 = r.readline().rstrip('\n')
                            tmp3 = r.readline().rstrip('\n')
                            tmp4 = r.readline().rstrip('\n')
                            r.close()
                            w = open("login.dll", 'w')
                            w.write(str(tmp1)+"\n")
                            w.write(str(tmp2)+"\n")
                            w.write(str(tmp3)+"\n")
                            w.write(str(tmp4)+"\n")
                            w.write(str(data)+"\n")
                            w.close()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_fix:
                            print('Please Wait!!')
                            ctypes.windll.user32.MessageBoxW(0, "Please Wait!", "Info", 1)
                            subprocess.call([r'delete-fix.bat'])
                                            
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_four:
                            print('Off!')
                            updates = 0
                            r = open("login.dll", 'r')
                            tmp1 = r.readline().rstrip('\n')
                            tmp2 = r.readline().rstrip('\n')
                            tmp3 = r.readline().rstrip('\n')
                            tmp4 = r.readline().rstrip('\n')
                            tmp5 = r.readline().rstrip('\n')
                            r.close()
                            w = open("login.dll", 'w')
                            w.write(str(tmp1)+"\n")
                            w.write(str(tmp2)+"\n")
                            w.write(str(tmp3)+"\n")
                            w.write(str(updates)+"\n")
                            w.write(str(tmp5)+"\n")
                            w.close()
                            ctypes.windll.user32.MessageBoxW(0, "You have made changes!", "Info", 1)
                            

                            


                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == button_three:
                            print('On!')
                            r = open("login.dll", 'r')
                            tmp1 = r.readline().rstrip('\n')
                            tmp2 = r.readline().rstrip('\n')
                            tmp3 = r.readline().rstrip('\n')
                            tmp4 = r.readline().rstrip('\n')
                            tmp5 = r.readline().rstrip('\n')
                            r.close()
                            w = open("login.dll", 'w')
                            w.write(str(tmp1)+"\n")
                            w.write(str(tmp2)+"\n")
                            w.write(str(tmp3)+"\n")
                            w.write(str(updates)+"\n")
                            w.write(str(tmp5)+"\n")
                            w.close()
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
            w.close()
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

        pygame.display.update()

