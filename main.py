from pygame import *
from random import randint

font.init()
font_text = font.Font(None, 36)

WIDTH = 600
HEIGTH = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 3000

def generate_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)

background = generate_color()
window = display.set_mode((WIDTH, HEIGTH))
display.set_caption('PING_PONG')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

color_generation = False
run = True
finish = False

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                color_generation = True
        elif e.type == KEYUP:
            if e.key == K_SPACE:
                color_generation = False

    if not finish:
        if generate_color:
            background = generate_color()
        window.fill(background)
    else:
        pass

    display.update()