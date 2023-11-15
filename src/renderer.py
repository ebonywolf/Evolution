import pygame

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Creature Simulator")

    def render(self, creature):
        self.screen.fill((255, 255, 255))  # Fill screen with white
        creature.draw(self.screen)
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()