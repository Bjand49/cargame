import math
import pygame
from entitytype import EntityType
from vector import Vector

class Car:
    def __init__(self, *, game, position: Vector):
        self.game = game
        self.score = 0
        self.speed = 0
        #default direction is looking up, might need to refector that later
        self.direction = Vector(EntityType.CAR, 0, -1)
        self.angle = 0
        self.position = position
        

    def move(self):
        new_position = self.position + Vector(EntityType.CAR,self.speed * self.direction.x,self.speed * self.direction.y )
        self.wall_distances = self.get_wall_distances()
        _, entity_type = self.collides_with_walls(new_position)
        current_checkpoint_walls = self.game.checkpoints[self.game.current_checkpoint]['walls']
        rect = pygame.Rect(self.position.x,self.position.y, 1, 1)
        if rect.clipline((current_checkpoint_walls[0].x, current_checkpoint_walls[0].y), (current_checkpoint_walls[1].x, current_checkpoint_walls[1].y)):
            self.game.set_next_checkpoint()
            print(f'Score: {self.score}. checkpoint hit: 10')
            self.add_score()
        if entity_type == EntityType.WALL:
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
            if any(wall.within(Vector(EntityType.NONE, x, y)) for wall in self.game.entities):
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
        self.direction = Vector(EntityType.NONE,new_x,new_y)

        
    def accelerate(self) -> None:
        self.speed += 0.01
        if self.speed > 5:
            self.speed = 5
        
    def deccelerate(self) -> None:
        self.speed -= 0.01
        if self.speed < -5:
            self.speed = -5
   