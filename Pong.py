import pygame
from pygame.locals import *
import math

width = 1000
height = 1000
#Tạo khung hình hiển thị game
display_surf = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Pong")

white = (255, 255, 255)
green = (0, 255,   0)

fps = 200 # Số frame trên giây
fps_clock = pygame.time.Clock()

class Ball:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def draw():
        pygame.draw.circle(display_surf, white, (self.x, self.y), math.radians(self.r), 0)

class scoreBoard:
    def __init__(self, score, x, y, font):
        self.score = score
        self.x = x
        self.y = y
        self.font = font
    def display(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        
