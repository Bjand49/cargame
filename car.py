import math
import pygame
from entitytype import EntityType
from vector import Vector

class Car:
    def __init__(self, *, game, position: Vector):
        self.game = game
        self.score = 0
        self.speed = 0
        self.direction = Vector(EntityType.CAR, 0, -1)
        self.angle = 0
        self.position = position
        self.wall_distances = []

    def move(self):
        new_position = self.position + Vector(EntityType.CAR, self.speed * self.direction.x, self.speed * self.direction.y)
        self.wall_distances = self.get_wall_distances()
        _, entity_type = self.collides_with_walls(new_position)
        current_checkpoint_walls = self.game.checkpoints[self.game.current_checkpoint]['walls']
        if self.circle_intersects_segment(
            (self.position.x + 0.5, self.position.y - 0.5), 1,
            (current_checkpoint_walls[0].x, current_checkpoint_walls[0].y),
            (current_checkpoint_walls[1].x, current_checkpoint_walls[1].y)
        ):
            self.game.set_next_checkpoint()
            self.add_score()
        if entity_type == EntityType.WALL:
            self.speed = 0
            self.subtract_score()
            return
        
        self.position = new_position

    def collides_with_walls(self, position: Vector):
        for wall in self.game.entities:
            if wall.within(position):
                return wall, wall.type
        return None, EntityType.NONE

    def subtract_score(self):
        self.score -= 0

    def add_score(self):
        self.score += 100

    def get_wall_distances(self) -> dict:
        wall_distances = {}
        i = 0
        for angle in [45, 0, -45]:
            wall_distances[i] = self.calculate_distance_in_direction(angle)
            i += 1
        return wall_distances

    def calculate_distance_in_direction(self, angle: float) -> float:
        increment_step = 0.5
        max_distance = 20.0
        increment = 0.0

        rotated_direction = self.rotate_vector(self.direction, angle)
        while increment < max_distance:

            new_x = self.position.x + rotated_direction.x * increment
            new_y = self.position.y + rotated_direction.y * increment
            compensated_vector = Vector(EntityType.CAR, new_x, new_y)

            if any(wall.within(compensated_vector) for wall in self.game.entities):
                break

            increment += increment_step

        if self.game.controller.draw and self.game.running:
            pygame.draw.line(
                self.game.screen,
                (255, 255, 255),
                ((self.position.x + 0.5) * self.game.scale, (self.position.y + 0.5) * self.game.scale),
                ((new_x + 0.5) * self.game.scale, (new_y + 0.5) * self.game.scale)
            )
        return increment

    def rotate(self, angle: float) -> None:
        self.angle += angle
        self.direction = self.rotate_vector(self.direction, angle)

    def increase_vector_length(self, direction: Vector, position: Vector, increase_by):
        relative_x = direction.x + position.x
        relative_y = direction.y + position.y
        current_length = math.sqrt(relative_x**2 + relative_y**2)
        new_length = current_length + increase_by
        if relative_y != 0:
            relative_y = relative_y / current_length
        if relative_x != 0:
            relative_x = relative_x / current_length
        multiplier = new_length / current_length
        new_vector = Vector(EntityType.NONE, direction.x * multiplier, direction.y * multiplier)
        return new_vector

    def rotate_vector(self, direction: Vector, angle: float) -> Vector:
        angle_radians = math.radians(angle)
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)

        new_x = direction.x * cos_angle - direction.y * sin_angle
        new_y = direction.x * sin_angle + direction.y * cos_angle
        vector = Vector(EntityType.NONE, new_x, new_y)
        return vector

    def accelerate(self) -> None:
        self.speed += 0.01
        if self.speed > 6:
            self.speed = 5

    def decelerate(self) -> None:
        self.speed -= 0.01
        if self.speed < -5:
            self.speed = -5

    def distance_point_to_segment(self, point, seg_start, seg_end):
        px, py = point
        x1, y1 = seg_start
        x2, y2 = seg_end

        segment_length_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

        if segment_length_squared == 0:
            return math.sqrt((px - x1) ** 2 + (py - y1) ** 2)

        t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / segment_length_squared))
        closest_x = x1 + t * (x2 - x1)
        closest_y = y1 + t * (y2 - y1)

        distance = math.sqrt((px - closest_x) ** 2 + (py - closest_y) ** 2)
        return distance

    def circle_intersects_segment(self, circle_center, radius, seg_start, seg_end):
        distance = self.distance_point_to_segment(circle_center, seg_start, seg_end)
        return distance <= radius
