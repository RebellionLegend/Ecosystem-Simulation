import pygame
import random
from variables import screenHeight, screenWidth, spriteHeight, spriteWidth, initHealth

allSpritesList = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # make Block a sprite
        super().__init__()
        # Call the parent class (Sprite) constructor
        #pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.health = initHealth
        self.moveX = True if (random.randint(0,1)==0) else False
        self.moveY = True if (random.randint(0,1)==0) else False

    def update(self):
        '''change direction if touched edge
        kill if health == 0'''

        if self.rect.x == screenHeight:
            self.moveX = False
        elif self.rect.x == 0:
            self.moveX = True

        if self.rect.y == screenWidth:
            self.moveY = False
        elif self.rect.y == 0:
            self.moveY = True
        
        if self.moveX == True:
            self.rect.x += 1
        else:
            self.rect.x -= 1

        if self.moveY == True:
            self.rect.y += 1
        else:
            self.rect.y -= 1

        # kill if health == 0
        if self.health == 0:
            self.kill()

def spritePosition(color):
    spriteColor = pygame.Color(color[0],color[1],color[2])
    #create new sprite
    block = Block(spriteColor, spriteHeight, spriteWidth)
    block.rect.x = random.randrange(screenHeight)
    block.rect.y = random.randrange(screenWidth)
    return block