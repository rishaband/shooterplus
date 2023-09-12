import pygame
import random

#setting the background color and text color. Also setting canvas size
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
screen_height = 500
screen_width = 1000
font = pygame.font.Font(None,50)
size = [screen_width,screen_height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Dodge the Cars')
x=0
background_position = [0,0]
background_image = pygame.image.load("r2.png")
background_image=pygame.transform.scale(background_image,[800,500])
background_image2 = pygame.image.load("r2.png")
background_image=pygame.transform.scale(background_image,[800,500])
done=False
display_instructions = True
instruction_page = 1
#car
class car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('rocket.png')
        self.image=pygame.transform.scale(self.image,[50,50])
        self.rect = self.image.get_rect()
        self.rect.x=50
        self.rect.y=250
        self.score=0
    def update(self):
        if self.rect.y<0 or self.rect.y>500:
            self.rect.x=20
            self.rect.y=random.randint(0,300)
        self.k=pygame.key.get_pressed()
        if self.k[pygame.K_UP]:
            self.rect.y=self.rect.y-5
        if self.k[pygame.K_DOWN]:
            self.rect.y+=5
# obstacles

class obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('obstacle 2.png')
        self.image=pygame.transform.scale(self.image,[50,60])
        self.rect = self.image.get_rect()

        self.rect.x=x
        self.rect.y=y
    def update(self):
        self.rect.x-=3
        if self.rect.x<0:
            self.rect.x=random.randint(300,650)
            self.rect.y=random.randint(0,400)



class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([4, 10])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet in up direction. """
        self.rect.x += 3
        if pygame.sprite.spritecollide(bullet, obstacle_list, True):
            # For each block hit, remove the bullet and add to the score
            bullet_list.remove(self)
            all_sprites_list.remove(self)
            p1.score += 1
        # Remove the bullet if it flies up off the screen
        if self.rect.y < 0:
            bullet_list.remove(self)
            all_sprites_list.remove(self)

all_sprites_list = pygame.sprite.Group()
car_list=pygame.sprite.Group()
obstacle_list=pygame.sprite.Group()
bullet_list=pygame.sprite.Group()
p1 = car()
all_sprites_list.add(p1)
p2 = obstacle(550,210)
all_sprites_list.add(p2)
obstacle_list.add(p2)
p3= obstacle(450,100)
all_sprites_list.add(p3)
obstacle_list.add(p3)
p4= obstacle(550,250)
all_sprites_list.add(p4)
obstacle_list.add(p4)
p5= obstacle(400,350)
all_sprites_list.add(p5)
obstacle_list.add(p5)
p6= obstacle(300,450)
all_sprites_list.add(p6)
obstacle_list.add(p6)
p7= obstacle(200,100)
all_sprites_list.add(p7)
obstacle_list.add(p7)
clock = pygame.time.Clock()
done=False
# instruction game loop
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1 #typing mistake
            if instruction_page == 3:
                display_instructions = False
    screen.fill(BLACK)
    if instruction_page == 1:
        text = font.render("Welcome to Space Jumper",True,WHITE)
        screen.blit(text,[10,10])
        text = font.render("Avoid the enemies!", True, WHITE)
        screen.blit(text,[10,40])
        text = font.render('Once you collide with enemies', True, WHITE)
        screen.blit(text,[10,70])
        text = font.render("Your game will be over", True, WHITE)
        screen.blit(text,[10,100])
    if instruction_page == 2:
        text = font.render("You can move the player with the arrow keys", True, WHITE)
        screen.blit(text,[10,10])
        text = font.render("Right click to shoot the bullet", True, WHITE)
        screen.blit(text,[10,40])
        text = font.render("How many enemies can you avoid in 1 minute?",True, WHITE)
        screen.blit(text,[10,80])
    clock.tick(60)
    pygame.display.flip()
#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = p1.rect.x
            bullet.rect.y = p1.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    if (len(obstacle_list)<6):
        p2 = obstacle(550,random.randint(0,400))
        all_sprites_list.add(p2)
        obstacle_list.add(p2)
    x=x-2#speed        
    screen.blit(background_image,[x,0])
    screen.blit(background_image2,[x+800,0])
    if x<-800:
        x=0
    all_sprites_list.draw(screen)

    all_sprites_list.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
                          
    

