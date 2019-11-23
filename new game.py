import pygame
pygame.init()
HORIZONTAL=500
VERTICAL=500
win=pygame.display.set_mode((HORIZONTAL,VERTICAL))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(10) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x< HORIZONTAL-vel-width:
        x += vel
#jump
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.4
            pygame.time.delay(10)
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()  # If we exit the loop this will execute and close our game




#Now we can draw a rectangle to the screen to represent our character. We will draw the rectangle in the main loop so that it is constantly redrawn each time we loop.

