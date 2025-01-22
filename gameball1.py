import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Лопни шарик!")

# Цвета
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (75, 0, 130), (238, 130, 238)]

# Шрифт для отображения текста
font = pygame.font.Font(None, 36)

# Класс для шарика
class Ball:
    def __init__(self):
        self.x = random.randint(20, width - 20)
        self.y = random.randint(20, height - 20)
        self.radius = 20
        self.color = random.choice(colors)
        self.dx = random.choice([-3, 3])
        self.dy = random.choice([-3, 3])

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Проверка на столкновение со стенами
        if self.x < self.radius or self.x > width - self.radius:
            self.dx *= -1
        if self.y < self.radius or self.y > height - self.radius:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        return (pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2 <= self.radius ** 2

# Создание списка шариков
balls = [Ball() for _ in range(10)]
score = 0

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for ball in balls:
                if ball.is_clicked(mouse_pos):
                    balls.remove(ball)
                    score += 1
                    break  # Выход из цикла, чтобы не увеличивать счет дважды

    # Обновление положения шариков
    screen.fill((255, 255, 255))  # Очистка экрана
    for ball in balls:
        ball.move()
        ball.draw(screen)

    # Отображение счета
    score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Проверка на окончание игры
    if not balls:
        game_over_text = font.render("Игра окончена!", True, (0, 0, 0))
        screen.blit(game_over_text, (width // 2 - 100, height // 2 - 20))

    pygame.display.flip()  # Обновление экрана
    pygame.time.delay(30)  # Задержка для управления скоростью

pygame.quit()
