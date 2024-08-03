import pygame
import sys

#Ініціалізація Pygame
pygame.init()

#Кольори
WHITE = (255,255,255)
BLACK = (0,0,0)

#Розмір екрану
WIDTH = 800
HEIGHT = 600

#Швидкість платформи
PLATFORM_SPEED = 5

#Швидкість м'яча
BALL_SPEED_X = 3
BALL_SPEED_Y = 3


#Клас для м'яча
class Ball(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surfase((20,20))
        self.image.fill(WHITE)
        self.rect = self.image.get.rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
    def update(self):
        self.rect.x += self.speef_x
        self.rect.y += self.speef_y
        
        #Відбивання від стін
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
            
#Класс для платформи
class Platform(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface((100,20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect.left > 0
        self.rect.center = (WIDTH // 2, HEIGHT - 30)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect_x -= PLATFORM_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLATFORM_SPEED
        
#Клас для монстрів
class Monster(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        self.image = pygame.Surface((30,30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)  
        
#Ініціалізація екрану        
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

#Створення груп спрайтів
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
platform = pygame.sprite.Group()
monsters = pygame.sprite.Group()

#створення об'єктів
ball = Ball()
platform = Platform()

all_sprites.add(ball, platform)

#Створення монстрів
for i in range(4):
    for j in range(10):
        monster = Monster(60 * j + 50,40 * j + 50)
        all_sprites.add(monster)
        monster.add(monster)

#Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #Оновлення
    all.sprites.update()

    #Первірка зіткнень м'яча та монстрів
    hits = pygame.sprite.spritecollide(ball, monster, True)
    for hit in hits:
        ball.speed_y *= -1

    #Перевірка зіткнень м'яча та платформи
    if pygame.sprite.collide_rect(ball, platform):
        ball.speed_y *= -1

    #Перевірка кінця гри
    if ball.rect.bottom >= HEIGHT:
        print("Game Over")
        running = False

    #відображення
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    #Частота кадрів
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
