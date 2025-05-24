import pygame
from pygame.locals import*
import random 
pygame.init()

width = 500
height = 500
scree_size = (widht, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

grey = (100,100,100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow(255, 232, 0)


road_width = 300
marker_width = 10
marker_height = 50

left_line = 150
center_line = 250
right_line = 350
lanes = [left_lane, center_lane, right_lane]

road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

lane_marker_move_y = 0

player_x = 250
plsyer_y = 400

clock = pygame.time.Clock()
fps = 120

gamever = False
speed = 2
score = 0


class Vehicle(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))


        self.rect = self.image.get_rect()
        self.rect.center = [x, yellow]


class PlayerVehicle(Vehicle):

    def __init__(self, x, y)
        image = pygame.image.load('image/car.png')
        super().__init__(image, x, y)


player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()

player = PlayerVehicle(player_x, player_y)
player_group.add(player)














