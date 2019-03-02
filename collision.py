import pygame
def collision(gameObjGroup):
    '''gameObjGroup = [predator_group, organism_group, prey_group]'''
    def killOrganism(gameObjGroup):
        '''kill if organism touched predator or prey touched organism'''
        for i in range(len(gameObjGroup)):
            if i!=len(gameObjGroup)-1:
                for mySprite in gameObjGroup[i]:
                    collision = pygame.sprite.spritecollideany(mySprite, gameObjGroup[i+1])
                    if collision != None:
                        mySprite.kill()
                        print("killed")
                        collision.health += 10
                        print(collision, collision.health)
    killOrganism(gameObjGroup)