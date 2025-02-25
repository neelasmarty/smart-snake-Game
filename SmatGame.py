import random
import pygame

pygame.init()

# Screen settings
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grishma Snake Game")

# Snake settings
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]
snake_size = 10

# Food settings
food_x, food_y = random.randrange(0, width, 10), random.randrange(0, height, 10)

# Clock to control game speed
clock = pygame.time.Clock()

# Function to generate new food position
def generate_food():
    while True:
        new_food_x = random.randrange(0, width, 10)
        new_food_y = random.randrange(0, height, 10)
        if (new_food_x, new_food_y) not in snake_body:
            return new_food_x, new_food_y

# Function to update game screen
def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y

    # Move snake
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check for collision with itself
    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER")
        pygame.quit()
        quit()

    # Add new position to the snake body
    snake_body.append((snake_x, snake_y))

    # Check if food is eaten
    if food_x == snake_x and food_y == snake_y:
        food_x, food_y = generate_food()
    else:
        del snake_body[0]  # Remove tail if no food is eaten

    # Draw elements
    game_screen.fill((150, 150, 150))  # Background color
    pygame.draw.rect(game_screen, (0, 0, 128), [food_x, food_y, snake_size, snake_size])  # Food

    for (x, y) in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 102), [x, y, snake_size, snake_size])  # Snake body

    pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT and change_x == 0:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP and change_y == 0:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN and change_y == 0:
                change_x = 0
                change_y = 10

    # Update snake movement
    display_snake_and_food()

    # Control speed
    clock.tick(15)

pygame.quit()
