import math

class Vector:
    def __init__(self, type, x: int = 0, y: int = 0):
        self.x = x
        self.y = y        
        self.type = type


    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other: 'Vector') -> 'Vector':
        factor = 0.4
        return Vector(self.type, self.x + other.x * factor, self.y + other.y*factor)

    def within(self, other: 'Vector') -> bool:
        distance = math.sqrt(abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2)

        return distance < 1
    
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y
   