import pygame
from renderer import Renderer
from creature import Creature

def main():
    WIDTH, HEIGHT = 800, 600
    renderer = Renderer(WIDTH, HEIGHT)
    creature = Creature(WIDTH // 2, HEIGHT // 2, 30)  # Centered creature

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        creature.update()
        renderer.render(creature)

    renderer.cleanup()

if __name__ == "__main__":
    main()
