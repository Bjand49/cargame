import csv
import math
import pygame
import numpy as np
import time
from entitytype import EntityType
from vector import Vector
from car import Car

class CarGame:
    def __init__(self, scale: int = 30):
        self.scale = scale
        self.entities:list[Vector]= []
        self.checkpoints = []

        ysize,xsize = self.load_map()
        self.grid = Vector(EntityType.NONE,xsize, ysize)
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
                    self.entities.append(Vector(EntityType.WALL,j,y))
                    
                elif cell == 'C':
                    self.car = Car(game=self,position=Vector(EntityType.CAR,j,y))
                # Assuming that the cell is not empty, the only last option is that its a number, and therefore a checkpoint.
                # Migth need to be refactored later
                elif cell != '':
                    checkpoints.append(dict({
                            'id':cell,
                            'point':Vector(EntityType.CHECKPOINT,j,y),
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
                    temp_vector = Vector(EntityType.CHECKPOINT,checkpoint['point'].x + temp_x, checkpoint['point'].y + temp_y)
                    if any(wall.within(temp_vector) for wall in self.entities):
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

    def block(self, obj: 'Vector'):
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
   