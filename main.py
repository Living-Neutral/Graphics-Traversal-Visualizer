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


if __name__ == '__main__':
    print('hello world')
    ROWS = 50
    grid = make_grid(ROWS,WIDTH)

    run = True

    UI_E = Menu.UIElement(
        center_position= (400,400),
        font_size=30,
        bg_rgb=graphics.BLUE,
        text_rgb=graphics.WHITE,
        text="Hello World"
    )

    quit_btn = Menu.UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=graphics.BLUE,
        text_rgb=graphics.WHITE,
        text="Quit",
        action = Menu.GameState.QUIT
    )

    while run :
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            pass
        WIN.fill(graphics.BLUE)

        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None or event.type ==pygame.QUIT:
            run = False
        quit_btn.draw(WIN)
        pygame.display.flip()


    pygame.quit()



