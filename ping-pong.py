from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

font.init()
font1 = font.SysFont('Arial',40)
font2 = font.SysFont('Arial',48)

x1 = 100
y1 = 100
x2 = 300
y2 = 300
clock = time.Clock()
FPS = 60
game  = True
speed = 109
finish = False

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

