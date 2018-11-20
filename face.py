# Examples of the math.sin() and math.cos() trig functions
# Al Sweigart al@inventwithpython.com

# You can learn more about Pygame with the
# free book "Making Games with Python & Pygame"
#
# http://inventwithpython.com/pygame
#

import sys, pygame, math
from pygame.locals import *
from scipy import interpolate
import numpy as np


# set up a bunch of constants
BRIGHTBLUE = (  0,  50, 255)
RED        = (255,   0,   0)
WHITE      = (255, 255, 255)
BLACK      = (  0,   0,   0)

WHITE2      = (240, 240, 240)
f = (245, 176, 147)
rotcolor =(255, 150, 110)
hatcolor=(250, 0, 0)
brown = (100,0,0)
black = (0,0,0)

BGCOLOR = f

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 60

PERIOD_INCREMENTS = 500.0
AMPLITUDE = 100

# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Bounce')

step = 0




# main application loop
while True:
    # event handling loop for quit events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # draw waving ball
    #yPos = -1 * math.sin(step) * AMPLITUDE
    #pygame.draw.circle(DISPLAYSURF, BRIGHTBLUE, (int(WINDOWWIDTH * 0.5), int(WINDOWWIDTH*0) + WIN_CENTERY), step)




    #hat_white
    hat = np.array( [ [0, 120], [WIN_CENTERX, 90], [WINDOWWIDTH, 120] ] )
    x = hat[:,0]
    y = hat[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew,ynew = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)

    xy_hat=[[0,0]]
    for i in range(len(xnew)):
        xy_hat.append([int(xnew[i]),int(ynew[i])])
    xy_hat.append([WINDOWWIDTH,0])
    pygame.draw.polygon(DISPLAYSURF, WHITE, xy_hat)


    #hat
    hat = np.array( [ [0, 100], [WIN_CENTERX, 70], [WINDOWWIDTH, 100] ] )
    x = hat[:,0]
    y = hat[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew,ynew = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)

    xy_hat=[[0,0]]
    for i in range(len(xnew)):
        xy_hat.append([int(xnew[i]),int(ynew[i])])
    xy_hat.append([WINDOWWIDTH,0])
    pygame.draw.polygon(DISPLAYSURF, hatcolor, xy_hat)


    

    # draw the border
    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)+110, int(WIN_CENTERY) - 20), 65)
    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)-110, int(WIN_CENTERY) - 20), 65)

    pygame.draw.circle(DISPLAYSURF, brown, (int(WIN_CENTERX)+110, int(WIN_CENTERY) - 20), 50)
    pygame.draw.circle(DISPLAYSURF, brown, (int(WIN_CENTERX)-110, int(WIN_CENTERY) - 20), 50)

    pygame.draw.circle(DISPLAYSURF, black, (int(WIN_CENTERX)+110, int(WIN_CENTERY) - 20), 42)
    pygame.draw.circle(DISPLAYSURF, black, (int(WIN_CENTERX)-110, int(WIN_CENTERY) - 20), 42)

    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)+135, int(WIN_CENTERY) - 24), 15)
    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)-135, int(WIN_CENTERY) - 24), 15)

    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)+115, int(WIN_CENTERY) - 45), 9)
    pygame.draw.circle(DISPLAYSURF, WHITE, (int(WIN_CENTERX)-115, int(WIN_CENTERY) - 45), 9)

    pygame.draw.circle(DISPLAYSURF, f, (int(WIN_CENTERX)+135, int(WIN_CENTERY) +80), 90)
    pygame.draw.circle(DISPLAYSURF, f, (int(WIN_CENTERX)-135, int(WIN_CENTERY) +80), 90)

    pygame.draw.ellipse(DISPLAYSURF, rotcolor, (WIN_CENTERX-240, WIN_CENTERY+50 ,80,60))
    pygame.draw.ellipse(DISPLAYSURF, rotcolor, (WIN_CENTERX+240-80, WIN_CENTERY+50 ,80,60))


    brow_up=np.array( [ [WIN_CENTERX+70, WIN_CENTERY-130], [WIN_CENTERX+100, WIN_CENTERY-170], [WIN_CENTERX+230, WIN_CENTERY-135], [WIN_CENTERX+235, WIN_CENTERY-105] ] )
    brow_down=np.array( [ [WIN_CENTERX+70, WIN_CENTERY-130], [WIN_CENTERX+100, WIN_CENTERY-140], [WIN_CENTERX+235, WIN_CENTERY-105],  ] )

    x = brow_up[:,0]
    y = brow_up[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew,ynew = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)

    x = brow_down[:,0]
    y = brow_down[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew2,ynew2 = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)
    xnew2=np.flipud(xnew2)
    ynew2=np.flipud(ynew2)

    xy_brow_up=[]
    for i in range(len(xnew)):
        xy_brow_up.append([int(xnew[i]),int(ynew[i])])
    for i in range(len(xnew)):
        xy_brow_up.append([int(xnew2[i]),int(ynew2[i])])
    pygame.draw.polygon(DISPLAYSURF, WHITE2, xy_brow_up)


    brow_up=np.array( [ [WIN_CENTERX-70, WIN_CENTERY-130], [WIN_CENTERX-100, WIN_CENTERY-170], [WIN_CENTERX-230, WIN_CENTERY-135], [WIN_CENTERX-235, WIN_CENTERY-105] ] )
    brow_down=np.array( [ [WIN_CENTERX-70, WIN_CENTERY-130], [WIN_CENTERX-100, WIN_CENTERY-140], [WIN_CENTERX-235, WIN_CENTERY-105],  ] )

    x = brow_up[:,0]
    y = brow_up[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew,ynew = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)

    x = brow_down[:,0]
    y = brow_down[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew2,ynew2 = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)
    xnew2=np.flipud(xnew2)
    ynew2=np.flipud(ynew2)

    xy_brow_up=[]
    for i in range(len(xnew)):
        xy_brow_up.append([int(xnew[i]),int(ynew[i])])
    for i in range(len(xnew)):
        xy_brow_up.append([int(xnew2[i]),int(ynew2[i])])
    pygame.draw.polygon(DISPLAYSURF, WHITE2, xy_brow_up)





    rot = np.array( [ [WIN_CENTERX-100, WIN_CENTERY+130], [WIN_CENTERX, WIN_CENTERY+150+step], [WIN_CENTERX+100, WIN_CENTERY+130] ] )
    x = rot[:,0]
    y = rot[:,1]
    
    tck,u = interpolate.splprep( [x,y], k = 2)
    xnew,ynew = interpolate.splev( np.linspace( 0, 1, 20 ), tck,der = 0)

    xy_rot=[]
    for i in range(len(xnew)):
        xy_rot.append([int(xnew[i]),int(ynew[i])])
    pygame.draw.polygon(DISPLAYSURF, rotcolor, xy_rot)




    pygame.display.update()
    FPSCLOCK.tick(FPS)

    if (step==40):
        flag=1
    if (step==0):
        flag=0
    if(step<40 and flag==0):
        step += 1

    if(step>0 and flag==1):
        step -= 1
    #step %= 2 * math.pi
