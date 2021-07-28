from Robot import robot
import pygame
import time
import math
import textprint

# Define some colors.
WHITE = pygame.Color('white')

MACAdress = ["1c:52:16:25:82:27", "1c:52:16:25:82:27"] #loop related variables
Robot = []
done = False
pygame.init() #pygame related variables
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Joystick")
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = textprint.TextPrint()

for i in MACAdress:
    Robot.append(robot(i))

while not done:

    for i in Robot: # for every robot object make it roll
        i.roll()

    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # end loop

    screen.fill(WHITE) # fill the screen white
    textPrint.reset() # reset the text 
    joystick_count = pygame.joystick.get_count() #get total joysticks

    for i in range(joystick_count): #for every joystick
        joystick = pygame.joystick.Joystick(i) # initiate each joystick
        joystick.init()
        xaxis = joystick.get_axis(0) #setting variables
        yaxis = joystick.get_axis(1)
        taxis = joystick.get_axis(3)
        if -0.095 <= xaxis <= 0.095: #buffer value to fix controller drift
            xaxis = 0
        if -0.095 <= yaxis <= 0.095:
            yaxis = 0
        if -0.095 <= taxis <= 0.095:
            taxis = 0
        
        if  (xaxis == 0) and (yaxis == 0):
            direction = 0
        elif xaxis == 0:
            if yaxis > 0:
                direction = 180
            if yaxis < 0:
                direction = 0
        elif yaxis == 0:
            if xaxis > 0:
                direction = 90
            if xaxis < 0:
                direction = 270
        else:
            direction = math.degrees(math.atan(yaxis/xaxis)) #find angle using trig 
            if xaxis < 0: #depending on which quadrant of the cartisian plane it would be in add a certain value to find the true bearing
                if yaxis < 0:
                    direction += 180
                else:
                    direction +=270
            if xaxis > 0:
                if yaxis < 0:
                    direction += 90
                else:
                    direction += 90
            direction = round(direction) #rounding the angle to the nearest degree
        textPrint.tprint(screen, "The joystick direction is {}".format(direction)) # print out direction to the screen
        textPrint.tprint(screen, "Thrust percent: {}%".format(taxis*100)) # print out thrust percentage to the screen
        for i in Robot: # for every robot object update its values
            i.update(255*taxis, direction)
    pygame.display.flip() #update screen
    # Limit to 20 frames per second.
    clock.tick(60) #set cap to 60 fps

pygame.quit()
