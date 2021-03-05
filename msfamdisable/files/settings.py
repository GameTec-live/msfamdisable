import pygame
import pygame_gui
import os
import time
import subprocess

try:
    r = open("data.txt", 'r')
    variable = r.readline()
    r.close()
    data = int(variable)

except:
    print("Error! No data.txt file Found! Please execute setup!")
    time.sleep(2)
    subprocess.call([r'debugconsole.bat'])








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
                        

                        


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_three:
                        print('On!')
                        x = open("updates.txt", 'w')
                        x.close()
            

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_rst:
                        is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_help:
                        print('Starting Console')
                        subprocess.call([r'debugconsole.bat'])





            manager.process_events(event)

    except:
        print("Error 1")
        print("Continuing on!")
        subprocess.call([r'minor.bat'])
    


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