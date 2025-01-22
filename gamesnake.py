import pygame
import random
import sys

# Настройки игры
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SNAKE_SIZE = 20
SNAKE_SPEED = 10
HUNTER_SIZE = 20
FOOD_SIZE = 20

# Цвета
BACKGROUND_COLOR = (30, 30, 30)  # Темно-серый
SNAKE_COLOR = (0, 204, 102)  # Зеленый
FOOD_COLOR = (255, 223, 0)  # Желтый
HUNTER_COLOR = (255, 69, 0)  # Оранжевый
TEXT_COLOR = (255, 255, 255)  # Белый

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")


# Класс змеи
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (SNAKE_SIZE, 0)
        self.alive = True

    def move(self):
        if not self.alive:
            return
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        if not self.alive:
            return
        self.body.append(self.body[-1])  # Увеличиваем длину змеи

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def check_collision(self):
        head_x, head_y = self.body[0]

        # Проверка выхода за границы окна
        if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
            self.alive = False

        # Проверка столкновения с самим собой
        if len(self.body) != len(set(self.body)):
            self.alive = False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, SNAKE_SIZE, SNAKE_SIZE))


# Класс еды
class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, (WINDOW_WIDTH // FOOD_SIZE) - 1) * FOOD_SIZE,
                random.randint(0, (WINDOW_HEIGHT // FOOD_SIZE) - 1) * FOOD_SIZE)

    def draw(self):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, FOOD_SIZE, FOOD_SIZE))


# Класс охотника
class Hunter:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, (WINDOW_WIDTH // HUNTER_SIZE) - 1) * HUNTER_SIZE,
                random.randint(0, (WINDOW_HEIGHT // HUNTER_SIZE) - 1) * HUNTER_SIZE)

    def draw(self):
        pygame.draw.rect(screen, HUNTER_COLOR, (*self.position, HUNTER_SIZE, HUNTER_SIZE))


# Функция для отображения текста


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Основная функция игры
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    hunters = [Hunter() for _ in range(3)]

    # Шрифт для правил и конца игры
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -SNAKE_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, SNAKE_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-SNAKE_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((SNAKE_SIZE, 0))

        screen.fill(BACKGROUND_COLOR)
        snake.move()
        snake.check_collision()

        if snake.alive:
            if snake.body[0] == food.position:
                snake.grow()
                food.position = food.random_position()  # Генерируем новую еду

            # Проверка столкновения с охотниками
            for hunter in hunters:
                if snake.body[0] == hunter.position:
                    snake.alive = False

        # Отрисовка объектов
        snake.draw()
        food.draw()
        for hunter in hunters:
            hunter.draw()

        # Отображение правил на экране
        draw_text('Используйте стрелки, чтобы управлять змеей', font, TEXT_COLOR, screen, 20, 20)
        draw_text('Собирайте желтую еду и избегайте охотников!', font, TEXT_COLOR, screen, 20, 60)

        # Проверяем, жива ли змея
        if not snake.alive:
            draw_text('Игра окончена!', font, TEXT_COLOR, screen, WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2)
            draw_text('Нажмите ESC для выхода', font, TEXT_COLOR, screen, WINDOW_WIDTH // 2 - 130,
                      WINDOW_HEIGHT // 2 + 40)

        # Обновление экрана
        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

        # Проверка завершения игры
        if not snake.alive:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main()
