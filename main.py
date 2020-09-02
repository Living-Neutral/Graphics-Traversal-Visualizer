import pygame
import graphics
import algorithms
import Menu


pygame.init()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Graph Traversal simulator")


def make_grid(rows,width):
    grid = []
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = graphics.Spot(i,j,gap,rows)
            grid[i].append(spot)
    return grid


# main loop
if __name__ == '__main__':
    print('hello world')
    ROWS = 50
    grid = make_grid(ROWS,WIDTH)

    run = True

    game_state = Menu.GameState.TITLE
    run = True
    while run:
        for event in pygame.event.get():
            if game_state == Menu.GameState.TITLE:
                player = Menu.Player()
                game_state = Menu.title_screen(WIN)

            if game_state == Menu.GameState.LEVEL_SELECT_PAGE_ONE:
                player.current_level = 1
                game_state = Menu.menu_one(WIN,player)

            if game_state == Menu.GameState.QUIT or event.type == pygame.QUIT:
                run = False

    pygame.quit()