import pygame 
window = pygame.display.set_mode((700,500))
clock = pygame.time.Clock()


class Object():
    def __init__ (self,color,w,h):
        self.image = pygame.Surface((w,h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
class Player(Object):
    def controler(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w] == 1:
            self.rect.y -= 10
        if key_list[pygame.K_s] == 1:
            self.rect.y += 10
    def auto(self):
        self.rect.y = bal.rect.y
    def collision(self):
        if self.rect.colliderect(bal.rect):
            bal.speed_x = -bal.speed_x 



class Ball(Object):
    speed_x = 10
    speed_y = 10
    def control(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y  > 470:
            self.speed_y = -self.speed_y
        if self.rect.y  < 0:
            self.speed_y = -self.speed_y
        if self.rect.x  > 670:
            self.speed_x = -self.speed_x
        if self.rect.x  < 0:
            self.speed_x = -self.speed_x


bal = Ball((0,0,0),30,30)
p1 = Player((0,0,0),30,100)
p2 = Player((0,0,0),30,100)
p2.rect.x = 670
p2.rect.y = 500
bal.rect.x = 350
bal.rect.y = 250
while True:
    window.fill((212,186,174))
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    p1.controler()
    p2.auto()
    bal.control()
    p1.collision()
    p2.collision()
    window.blit(bal.image, bal.rect)
    window.blit(p2.image, p2.rect)
    window.blit(p1.image, p1.rect)
    pygame.display.update()
    clock.tick(25)
