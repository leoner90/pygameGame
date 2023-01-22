# importing pygame module
import pygame
import sys
from time import sleep
 
class Player(pygame.sprite.Sprite):
    right = True
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ninja.png')
        self.change_x = 0
        self.change_y = 440
        self.moveRight = 0
        self.moveLeft = 0
        self.jumpHeight = 0
        self.jumpControll = True
        
    def move_right(self):
        self.moveRight = 3
        if (not self.right):
            self.image = pygame.transform.flip(self.image, True, False)
            self.right = True

    def move_left(self):
        self.moveLeft = -3
        if (self.right):
            self.image = pygame.transform.flip(self.image, True, False)
            self.right = False

    def jump(self):
        if self.jumpControll:
            self.jumpHeight = 100
            self.jumpControll = False

    def update(self):
        self.change_x += self.moveRight
        self.change_x += self.moveLeft

        #jump
        if self.jumpHeight != 0:
            self.change_y -= 2
            self.jumpHeight -= 4
        elif self.change_y < 440 :
            self.change_y += 4
        if self.change_y > 330:   
            self.jumpControll = True
             
            
    def stop(self):
        self.moveLeft = 0
        self.moveRight = 0
        
def main():
    def screenUpdate():
        bg = pygame.image.load('mainImg.jpg')
        screen.blit(bg, (0, 0))
        screen.blit(player.image, (player.change_x, player.change_y))
        pygame.display.flip()
    #init
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode([1000,500])
    pygame.display.set_caption("GAME")
    player = Player()
    pygame.key.set_repeat(40)
    

    while True:
        player.update()
        screenUpdate()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:  
                        player.move_right()        
                if event.key == pygame.K_a: 
                        player.move_left()                   
                if event.key == pygame.K_SPACE:
                        player.jump()
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.stop()
                if event.key == pygame.K_d :
                    player.stop()
    clock.tick(60)
main()  

   
                
        




            
