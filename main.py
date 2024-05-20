import csv
import math
from typing import List
import pygame
from enum import Enum
import numpy as np
import time


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
        distance = math.sqrt(abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2)

        return distance < 1
    
    def withinEntity(self, other: 'Entity') -> bool:
        return self.within(other.position)


    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y
           
class CarGame:
    def __init__(self, scale: int = 30):
        self.scale = scale
        self.entities: List[Entity]= []
        self.checkpoints = []

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
        self.max_rounds = 2
        self.rounds = 0
        self.running = True
        self.start_time = time.time()

        

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
                # Assuming that the cell is not empty, the only last option is that its a number, and therefore a checkpoint.
                # Migth need to be refactored later
                elif cell != '':
                    checkpoints.append(dict({
                            'id':cell,
                            'point':Entity(Vector(j,y),EntityType.CHECKPOINT),
                            'walls':[],
                            'is_active':False
                            
                        }))
        directions = ['N','E','S','W']
        for checkpoint in checkpoints:
            points = [] 
            for y in directions:
                distance = 0
                temp_x = 0
                temp_y = 0
                while True:
                    if(y == 'N'):
                        temp_y -= 1
                    elif(y == 'E'):
                        temp_x += 1
                    elif(y == 'S'):
                        temp_y += 1
                    elif(y == 'W'):
                        temp_x -= 1
                    else:
                        raise Exception('uninteded alteration happened')
                    distance += 1
                    temp_vector = Vector(checkpoint['point'].x + temp_x, checkpoint['point'].y + temp_y)
                    if any(wall.within(Entity(temp_vector,EntityType.RAY)) for wall in self.entities):
                        points.append((distance,temp_vector))
                        break

                sorted_points = sorted(points, key=lambda point: point[0])
                checkpoint['walls'] = [x[1] for x in sorted_points][:2]
            
        self.checkpoints = sorted(checkpoints, key=lambda x: x["id"])

        return height,width
        

    def draw_map(self):
        
        for i,b in enumerate(self.entities):
            if(b.type == EntityType.WALL):
                color = self.wall_color
                pygame.draw.rect(self.screen,
                                    color,
                                    self.block(b))
            if(self.current_checkpoint is not None):
                checkpoint = self.checkpoints[self.current_checkpoint]
                color = self.checkpoint_color
                pygame.draw.line(self.screen,
                                    color,
                                    (checkpoint['walls'][0].x*self.scale,checkpoint['walls'][0].y*self.scale),
                                    (checkpoint['walls'][1].x*self.scale,checkpoint['walls'][1].y*self.scale))

            
    def __del__(self):
        pygame.quit()

    def block(self, ent: 'Entity'):
        obj = ent.position
        return (obj.x * self.scale, obj.y * self.scale, self.scale, self.scale)

    def get_car_points(self, ent: 'Car'):
        vector = np.array([ent.direction.x,ent.direction.y])
        point = np.array([ent.position.x +.5,ent.position.y+.5])

        perpendicular_vector = np.array([-vector[1], vector[0]])

        half_width = 0.5
        val2 = vector * half_width
        point1 = (point - perpendicular_vector *half_width*1.1 - val2)*self.scale
        point2 = (point + perpendicular_vector *half_width*1.1 - val2)*self.scale
        point3 = (point + perpendicular_vector * half_width*0.9 + val2)*self.scale
        point4 = (point - perpendicular_vector * half_width*0.9 + val2)*self.scale        
        points = [(point1[0],point1[1]),(point2[0],point2[1]),(point3[0],point3[1]),(point4[0],point4[1])]

        return points
    def run(self):
        next_moves = []
        while self.running:
            # handle pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                    elif event.key == pygame.K_r:
                        self.__init__()
                    else:
                        next_moves.append(event.key)

                if event.type == pygame.KEYUP:
                    next_moves.remove(event.key)
            if pygame.K_UP in next_moves:
                self.car.accelerate()
            if pygame.K_DOWN in next_moves:
                self.car.deccelerate()
            if pygame.K_LEFT in next_moves:
                self.car.rotate(math.pi/-18)
            if pygame.K_RIGHT in next_moves:
                self.car.rotate(math.pi/18)
            # wipe screen
            self.screen.fill('black')
            
            # update game state
            self.car.move()

            # render game
            pygame.draw.polygon(self.screen,
                    self.car_color,
                    self.get_car_points(self.car))

            self.draw_map()
                # render screen
            pygame.display.flip()

            # progress time
            self.clock.tick(40)
        print(f"final score: {self.car.score - int(time.time() - self.start_time)}")

    def set_next_checkpoint(self):
        checkpointcount = len(self.checkpoints)
        for x in self.checkpoints:
            x['is_active'] = False
        if(self.current_checkpoint is None):
            self.current_checkpoint = 0
        else:
            self.current_checkpoint +=1
            if(self.current_checkpoint >= checkpointcount):
                self.current_checkpoint=0
                self.rounds +=1
                if(self.rounds == self.max_rounds):
                    self.running = False
        self.checkpoints[self.current_checkpoint]['is_active'] = True
                    
        
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
        self.direction = Vector(0, -1)
        self.angle = 0
        self.position = position
        

    def move(self):
        new_position = self.position + Vector(self.speed * self.direction.x,self.speed * self.direction.y )
        self.wall_distances = self.get_wall_distances()
        entity, type = self.collides_with_walls(new_position)
        current_checkpoint_walls = self.game.checkpoints[self.game.current_checkpoint]['walls']
        rect = pygame.Rect(self.position.x,self.position.y, 1, 1)
        if rect.clipline((current_checkpoint_walls[0].x, current_checkpoint_walls[0].y), (current_checkpoint_walls[1].x, current_checkpoint_walls[1].y)):
            self.game.set_next_checkpoint()
            print(f'Score: {self.score}. checkpoint hit: 10')
            self.add_score()
        if type == EntityType.WALL:
            self.speed = 0
            self.subtract_score()
            print(f'Score: {self.score}. wall hit: -5')
            return
        
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
        increcment = 0.5
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
        pygame.draw.line(self.game.screen,
                                 (255,255,255),
                                 ((self.position.x+0.5)*self.game.scale, (self.position.y+0.5)*self.game.scale),
                                 ((x+0.5)*self.game.scale,(y+0.5)*self.game.scale))
        return distance
    def rotate(self, angle: float) -> None:
        cos_theta = math.cos(angle)
        sin_theta = math.sin(angle)
        new_x = self.direction.x * cos_theta - self.direction.y * sin_theta
        new_y = self.direction.x * sin_theta + self.direction.y * cos_theta
        self.direction = Vector(new_x,new_y)

        
    def accelerate(self) -> None:
        self.speed += 0.001
        if self.speed > 5:
            self.speed = 5
        
    def deccelerate(self) -> None:
        self.speed -= 0.001
        if self.speed < -5:
            self.speed = -5
    
if __name__ == '__main__':
    game = CarGame()
    game.run()
