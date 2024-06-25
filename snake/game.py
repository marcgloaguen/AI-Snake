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
        self.snake_pos = [[config.SCREEN_HEIGHT/2,config.SCREEN_WIDTH/2]]
        self.snake_mvt = [0,0]
        self.apple_pos = self.random_apple()
        self.body = 1

    def run(self):

        while self.running:
            self.screen.fill(config.BACKGROUND_COLOR)
            self.handle_events()
            self.draw_apple()
            self.snake()
            pygame.display.update()
            self.clock.tick(config.SNAKE_SPEED)
        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.body == 1 or self.snake_pos[0][0] - config.BLOCK_SIZE != self.snake_pos[1][0]:
                        self.snake_mvt = [-1, 0]
                elif event.key == pygame.K_RIGHT:
                    if self.body == 1 or self.snake_pos[0][0] + config.BLOCK_SIZE != self.snake_pos[1][0]:
                        self.snake_mvt = [1, 0]
                elif event.key == pygame.K_UP:
                    if self.body == 1 or self.snake_pos[0][1] - config.BLOCK_SIZE != self.snake_pos[1][1]:
                        self.snake_mvt = [0, -1]
                elif event.key == pygame.K_DOWN:
                    if self.body == 1 or self.snake_pos[0][1] + config.BLOCK_SIZE != self.snake_pos[1][1]:
                        self.snake_mvt = [0, 1]

    def snake(self):
        self.snake_pos.insert(
            0,
            [
                pos + mvt*config.BLOCK_SIZE for pos, mvt
                in zip(self.snake_pos[0], self.snake_mvt)
            ])
        if not -config.BLOCK_SIZE < self.snake_pos[0][0] < config.SCREEN_HEIGHT or not -config.BLOCK_SIZE < self.snake_pos[0][1] < config.SCREEN_WIDTH:
            self.running = False

        if self.snake_pos[0] == self.apple_pos:
            self.apple_pos = self.random_apple()
            self.body += 1

        self.snake_pos = self.snake_pos[:self.body]
        if self.snake_pos[0] in self.snake_pos[1:]:
            self.running = False

        for x,y in self.snake_pos :
            snake_rect = pygame.Rect(x, y, config.BLOCK_SIZE, config.BLOCK_SIZE)
            pygame.draw.rect(
                self.screen,
                config.SNAKE_COLOR,
                snake_rect
            )

    def quit(self):
        # Quitter Pygame
        pygame.quit()

    def random_apple(self):
        x = round(random.randrange(0, config.SCREEN_WIDTH - config.BLOCK_SIZE) / 20.0) * 20.0
        y = round(random.randrange(0, config.SCREEN_HEIGHT - config.BLOCK_SIZE) / 20.0) * 20.0
        return [x,y]


    def draw_apple(self):
        food_rect = pygame.Rect(self.apple_pos[0], self.apple_pos[1], config.BLOCK_SIZE, config.BLOCK_SIZE)
        pygame.draw.rect(self.screen, (255, 0, 0), food_rect)

