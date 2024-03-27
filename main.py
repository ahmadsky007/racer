import pygame
import sys
import random


pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
background_color = (50, 50, 50)
car_color = (0, 255, 255)
obstacle_color = (255, 0, 0)
car_width, car_height = 40, 20
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 7
obstacle_width, obstacle_height = 50, 20
obstacle_speed = 5 * 1.25
obstacles = []
clock = pygame.time.Clock()
running = True
score = 0
spawn_obstacle_timer = 0
obstacle_spawn_rate = 750

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        car_x += car_speed


    car_x = max(0, min(screen_width - car_width, car_x))
    spawn_obstacle_timer += clock.get_time()
    if spawn_obstacle_timer > obstacle_spawn_rate:
        spawn_obstacle_timer = 0
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacles.append([obstacle_x, -obstacle_height])


    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] + obstacle_height > car_y and obstacle[0] < car_x + car_width and obstacle[0] + obstacle_width > car_x:
            obstacles.remove(obstacle)
        elif obstacle[1] > screen_height:
            obstacles.remove(obstacle)
            score += 1


    screen.fill(background_color)
    pygame.draw.rect(screen, car_color, [car_x, car_y, car_width, car_height])
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle + [obstacle_width, obstacle_height])


    score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
