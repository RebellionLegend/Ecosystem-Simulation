import pygame
import keyboard
import random
from sprite import spritePosition
from collision import collision
screenHeight = 300
screenWidth = 300
frameRate = 10
numPredator = 10
numOrganism = 10
numPrey = 10
numGameObj = [numPredator, numOrganism, numPrey]
color_list=[[240,200,40], [200,40,240], [40,240,200]]
screen = pygame.display.set_mode((screenHeight,screenWidth))
clock = pygame.time.Clock()
organism_group = pygame.sprite.Group()
predator_group = pygame.sprite.Group()
prey_group = pygame.sprite.Group()
gameObjGroup = [predator_group, organism_group, prey_group]
pygame.init()
for j in range(len(numGameObj)):
    for i in range(numGameObj[j]):
        gameObjGroup[j].add(spritePosition(screenHeight, screenWidth, color_list[j]))
while (keyboard.is_pressed('q')==False):
    pygame.event.get()
    pygame.display.update()
    for i in range(len(gameObjGroup)):
        gameObjGroup[i].draw(screen)
        gameObjGroup[i].update(screenHeight, screenWidth, gameObjGroup[i])
    
    collision(gameObjGroup)
    #Refresh Screen
    pygame.display.flip()
    #Number of frames per second e.g. 60
    clock.tick(frameRate)
    screen.fill((0,0,0))
pygame.quit()