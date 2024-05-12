import csv
import json
import math
import pprint
import random
from typing import List
import pygame
from enum import Enum


class EntityType(Enum):
    NONE = 0,
    WALL = 1,
    CAR = 2
    CHECKPOINT = 3,
    RAY = 4

class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other: 'Vector') -> 'Vector':
        factor = 0.4
        return Vector(self.x + other.x * factor, self.y + other.y*factor)

    def within(self, other: 'Vector') -> bool:
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

        return distance < 1
    
    def withinEntity(self, other: 'Entity') -> bool:
        return self.within(other.position)


    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y
    
        
class CarGame:
    def __init__(self, scale: int = 30):
        self.scale = scale
        self.entities: List[Entity]= []
        self.checkpoints: List[Entity]= []

        ysize,xsize = self.load_map()
        self.grid = Vector(xsize, ysize)
        self.current_checkpoint = None
        pygame.init()

        self.screen = pygame.display.set_mode((xsize * scale, ysize * scale))
        self.clock = pygame.time.Clock()
        self.car_color = (255, 0, 0)
        self.wall_color = (0, 255, 0)
        self.checkpoint_color = (0, 0, 255)
        self.draw_map()
        self.set_next_checkpoint()
        

    def load_map(self):
        filename = 'road.csv'
        data = []
        height = 0
        width = 0
        checkpoints = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        for y, row in enumerate(data):
            height+=1
            width = len(row)
            for j, cell in enumerate(row):
                if cell == 'x':
                    self.entities.append(Entity(Vector(j,y),EntityType.WALL))
                    
                elif cell == 'C':
                    self.car = Car(game=self,position=Vector(j,y))

                elif cell != '':
                    checkpoints.append(dict({
                            'id':cell,
                            'checkpoint':Entity(Vector(j,y),EntityType.CHECKPOINT)
                        }))

        checkpoints = sorted(checkpoints, key=lambda x: x["id"])
        self.checkpoints += [x['checkpoint'] for x in checkpoints]
        return height,width
        

    def draw_map(self):
        
        for i,b in enumerate(self.entities):
            color = (255, 255, 255)
            if(b.type == EntityType.CHECKPOINT):
                color = self.checkpoint_color
            elif(b.type == EntityType.WALL):
                color = self.wall_color
            pygame.draw.rect(self.screen,
                                 color,
                                 self.block(b))
    def __del__(self):
        pygame.quit()

    def block(self, ent: 'Entity'):
        obj = ent.position
        return (obj.x * self.scale, obj.y * self.scale, self.scale, self.scale)

    def run(self):
        
        running = True          

        while running:
            # handle pygame events
            print(f'Speed: {self.car.speed}')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.car.rotate(math.pi/-10)
                    if event.key == pygame.K_RIGHT:
                        self.car.rotate(math.pi/10)
                    if event.key == pygame.K_UP:
                        self.car.accelerate()
                    if event.key == pygame.K_DOWN:
                        self.car.deccelerate()
                    if event.key == pygame.K_q:
                        running = False
                    if event.key == pygame.K_r:
                        self.__init__()
            # wipe screen
            self.screen.fill('black')
            
            # update game state
            self.car.move()

            # render game
            pygame.draw.rect(self.screen,
                                self.car_color,
                                self.block(self.car))
            self.draw_map()
            # render screen
            pygame.display.flip()

            # progress time
            self.clock.tick(60)
        print(f"final score: {self.car.score}")
    def set_next_checkpoint(self):
        checkpointcount = len(self.checkpoints)
        if(self.current_checkpoint is None):
            self.current_checkpoint = 0
            self.entities.append(self.checkpoints[self.current_checkpoint])
            return
        else:
            self.entities.remove(self.checkpoints[self.current_checkpoint])
            self.current_checkpoint +=1
            if(self.current_checkpoint >= checkpointcount):
                self.current_checkpoint=0
            self.entities.append(self.checkpoints[self.current_checkpoint])
            
        
        
        
        
class Entity:
    def __init__(self, position: Vector,type: EntityType):
        self.position = position
        self.type = type
        self.x = position.x
        self.y = position.y

    def within(self, other: 'Entity') -> bool:
        return self.position.within(other.position)
    
    def within(self, other: 'Vector') -> bool:
        return self.position.within(other)

class Checkpoint:
    def __init__(self, game: CarGame, position: Vector, index:str):
        self.game = game
        self.position = position
        self.index = 0
   
class Car:
    def __init__(self, *, game: CarGame, position: Vector):
        self.game = game
        self.score = 0
        self.speed = 0
        self.acceleration_value = 0.1
        self.direction = Vector(0, -1)
        self.angle = 0
        self.position = position
        

    def move(self):
        new_position = self.position + Vector(self.speed * self.direction.x,self.speed * self.direction.y )
        self.wall_distances = self.get_wall_distances()
        entity, type = self.collides_with_walls(new_position)
        if type == EntityType.WALL:
            self.speed = 0
            self.subtract_score()
            print(f'Score: {self.score}. wall hit: -5')
            return
        elif type == EntityType.CHECKPOINT:
            self.game.set_next_checkpoint()
            print(f'Score: {self.score}. checkpoint hit: 10')
            self.add_score()
        
        self.position = new_position
        
    def collides_with_walls(self, position: Vector):
        for wall in self.game.entities:
            if wall.within(position):
                return wall,wall.type
        return None,EntityType.NONE

    def subtract_score(self):
        self.score -= 5
    def add_score(self):
        self.score += 10
   
    def get_wall_distances(self) -> dict:
        wall_distances = {}

        for direction in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
            wall_distances[direction] = self.calculate_distance_in_direction(direction)

        return wall_distances

    def calculate_distance_in_direction(self, direction: str) -> float:
        increcment = 0.03
        dx,dy = 0,0
        if 'N' in direction:
            dy = -increcment
        if 'S' in direction:
            dy = increcment
        if 'E' in direction:
            dx = increcment 
        if 'W' in direction:
            dx = -increcment 
        
        distance = 0
        x, y = self.position.x, self.position.y
        while True:
            x += dx
            y += dy
            if any(wall.within(Entity(Vector(x, y),EntityType.RAY)) for wall in self.game.entities):
                break
            distance += increcment

        return distance
    def rotate(self, angle: float) -> None:
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = self.direction.x * cos_theta - self.direction.y * sin_theta
        new_y = self.direction.x * sin_theta + self.direction.y * cos_theta
        self.direction = Vector(new_x,new_y)

        
    def accelerate(self) -> None:
        self.speed += 0.1
        if self.speed > 5:
            self.speed = 5
        
    def deccelerate(self) -> None:
        self.speed -= 0.1
        if self.speed < -5:
            self.speed = -5
    
if __name__ == '__main__':
    game = CarGame()
    game.run()
