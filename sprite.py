import pygame
import random

spriteWidth = 5
spriteHeight = 5
initHealth = 100
all_sprites_list = pygame.sprite.Group()

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
    def update(self, screenHeight, screenWidth, group):
        # random movement
        if self.rect.x == screenHeight:
            self.rect.x -= 1
        elif self.rect.x == 0:
            self.rect.x += 1
        else:
            randomNum = random.randint(0,1)
            if randomNum == 0:
                self.rect.x += 1
            else:
                self.rect.x -= 1 
        if self.rect.y == screenHeight:
            self.rect.y -= 1
        elif self.rect.y == 0:
            self.rect.y += 1
        else:
            randomNum = random.randint(0,1)
            if randomNum == 0:
                self.rect.y += 1
            else:
                self.rect.y -= 1 
        # kill if health == 0
        if self.health == 0:
            self.kill()

def spritePosition(screenHeight, screenWidth, color):
    spriteColor = pygame.Color(color[0],color[1],color[2])
    #create new sprite
    block = Block(spriteColor, spriteHeight, spriteWidth)
    block.rect.x = random.randrange(screenHeight)
    block.rect.y = random.randrange(screenWidth)
    return block