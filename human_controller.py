from cargame import CarGame
from controller import controller

import pygame

class human_controller(controller):
    def __init__(self, game: CarGame) -> None:
        self.game= game
        self.input = [0,0,0,0]
        
    def update(self,data):
            #items are up down left right
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game.running = False
                    elif event.key == pygame.K_r:
                        return None
                    elif event.key == pygame.K_UP:
                        self.input[0]=1
                    elif event.key == pygame.K_DOWN:
                        self.input[1]=1
                    elif event.key == pygame.K_LEFT:
                        self.input[2]=1
                    elif event.key == pygame.K_RIGHT:
                        self.input[3]=1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.input[0]=0
                    elif event.key == pygame.K_DOWN:
                        self.input[1]=0
                    elif event.key == pygame.K_LEFT:
                        self.input[2]=0
                    elif event.key == pygame.K_RIGHT:
                        self.input[3]=0
            return self.input

