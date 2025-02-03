import pygame
import random

# Размеры игрового поля
FIELD_WIDTH = 10
FIELD_HEIGHT = 20
BLOCK_SIZE = 30

# Цвета
COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 120, 0),
    (255, 255, 0),
    (180, 0, 255),
    (0, 220, 220)
]

# Фигуры тетрамино
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((FIELD_WIDTH * BLOCK_SIZE + 150, FIELD_HEIGHT * BLOCK_SIZE))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.field = [[0] * FIELD_WIDTH for _ in range(FIELD_HEIGHT)]
        self.score = 0
        self.new_piece()

    def new_piece(self):
        self.current_shape = random.choice(SHAPES)
        self.current_color = random.randint(1, len(COLORS) - 1)
        self.current_x = FIELD_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0

    def check_collision(self, x, y, shape):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]:
                    new_x = x + col
                    new_y = y + row
                    if (new_x < 0 or new_x >= FIELD_WIDTH or
                            new_y >= FIELD_HEIGHT or
                            (new_y >= 0 and self.field[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[row])):
                if self.current_shape[row][col]:
                    self.field[self.current_y + row][self.current_x + col] = self.current_color

    def remove_lines(self):
        lines_removed = 0
        for row in range(FIELD_HEIGHT):
            if 0 not in self.field[row]:
                del self.field[row]
                self.field.insert(0, [0] * FIELD_WIDTH)
                lines_removed += 1
        self.score += lines_removed ** 2

    def rotate(self):
        rotated = list(zip(*self.current_shape[::-1]))
        if not self.check_collision(self.current_x, self.current_y, rotated):
            self.current_shape = rotated

    def run(self):
        fall_time = 0
        fall_speed = 1000

        while True:
            self.screen.fill(COLORS[0])

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.check_collision(self.current_x - 1, self.current_y, self.current_shape):
                            self.current_x -= 1
                    if event.key == pygame.K_RIGHT:
                        if not self.check_collision(self.current_x + 1, self.current_y, self.current_shape):
                            self.current_x += 1
                    if event.key == pygame.K_DOWN:
                        if not self.check_collision(self.current_x, self.current_y + 1, self.current_shape):
                            self.current_y += 1
                    if event.key == pygame.K_UP:
                        self.rotate()

            # Автоматическое падение
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if fall_time >= fall_speed:
                fall_time = 0
                if not self.check_collision(self.current_x, self.current_y + 1, self.current_shape):
                    self.current_y += 1
                else:
                    self.merge_piece()
                    self.remove_lines()
                    self.new_piece()
                    if self.check_collision(self.current_x, self.current_y, self.current_shape):
                        print("Game Over! Score:", self.score)
                        pygame.quit()
                        return

            # Отрисовка поля
            for y in range(FIELD_HEIGHT):
                for x in range(FIELD_WIDTH):
                    if self.field[y][x]:
                        pygame.draw.rect(self.screen, COLORS[self.field[y][x]],
                                         (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

            # Отрисовка текущей фигуры
            for y in range(len(self.current_shape)):
                for x in range(len(self.current_shape[y])):
                    if self.current_shape[y][x]:
                        pygame.draw.rect(self.screen, COLORS[self.current_color],
                                         ((self.current_x + x) * BLOCK_SIZE,
                                          (self.current_y + y) * BLOCK_SIZE,
                                          BLOCK_SIZE - 1, BLOCK_SIZE - 1))

            pygame.display.flip()


if __name__ == "__main__":
    game = Tetris()
    game.run()