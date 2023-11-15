class Creature:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def update(self):
        # Update creature properties here (if needed)
        pass

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)
