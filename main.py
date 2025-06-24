import pygame, sys

pygame. init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame. display.set_caption("Python Tetris")

clock = pygame. time. Clock()

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][18] = 7

game_grid.print_grid()

while True:
    for event in pygame. event.get():
        if event. type == pygame. QUIT:
            pygame. quit()
            sys. exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
#Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pygame.display.update()
    clock.tick(60)