import pygame
from . import config
import random

pygame.init()


class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (config.SCREEN_HEIGHT, config.SCREEN_WIDTH)
        )

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        while self.running:
            self.handle_events()

        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def quit(self):
        # Quitter Pygame
        pygame.quit()

    def random_coord_apple(self):
        x = round(random.randrange(0, config.SCREEN_WIDTH - config.BLOCK_SIZE) / 20.0) * 20.0
        y = round(random.randrange(0, config.SCREEN_HEIGHT - config.BLOCK_SIZE) / 20.0) * 20.0
        return (x, y)


        """
        food_rect = pygame.Rect(food_x, food_y, config.BLOCK_SIZE, config.BLOCK_SIZE)

        pygame.draw.rect(self.screen, (255, 0, 0), food_rect)
        pygame.display.flip()
        
        """
