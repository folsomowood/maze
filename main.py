import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont("freesansserif", 300)
maze = pygame.image.load("Maze.png")
mazeMask = pygame.mask.from_surface(maze, threshold=127)
arrow = pygame.image.load("Arrow.png")
arrow = pygame. transform.scale(arrow, (20, 20))
ArrowMask = pygame.mask.from_surface(arrow, threshold=127)
Flag = pygame.image.load("Flag.png")
Flag = pygame.transform.scale(Flag, (20, 20))
FlagMask = pygame.mask.from_surface(Flag, threshold=127)
Maze2 = pygame.image.load("Maze2.png")
Maze2 = pygame.transform.scale(Maze2, (600, 600))
Maze2Mask = pygame.mask.from_surface(Maze2, threshold=127)
x = 79
y = 500
Level = 1
currentMaze = maze
currentMask = mazeMask
flagx = 540
flagy = 510
while True:

    pygame.event.get()

    color = (0, 255, 255)
    screen.fill(color)
    screen.blit(currentMaze, (0, 0))
    screen.blit(arrow, (x, y))
    screen.blit(Flag, (flagx, flagy))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 1
        overlap = currentMask.overlap(ArrowMask, (x, y))
        if overlap is not None:
            y += 1
    if keys[pygame.K_s]:
        y += 1
        overlap = currentMask.overlap(ArrowMask, (x, y))
        if overlap is not None:
            y -= 1
    if keys[pygame.K_d]:
        x += 1
        overlap = currentMask.overlap(ArrowMask, (x, y))
        if overlap is not None:
            x -= 1
    if keys[pygame.K_a]:
        x -= 1
        overlap = currentMask.overlap(ArrowMask, (x, y))

        if overlap is not None:
            x += 1
    overlap = FlagMask.overlap(ArrowMask, (540 - x, 510 - y))
    if overlap is not None:
        if Level == 2:
            print("You Win Level 2!")
            break
        print("You Win Level 1!")
        Level += 1
        currentMaze = Maze2
        currentMask = Maze2Mask
        x = 60
        y = 500
        flagx = 560
    pygame.display.flip()
