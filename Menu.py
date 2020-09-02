import pygame, sys
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
from pygame.rect import Rect
from pygame.sprite import RenderUpdates
import graphics

class Player:
    """
    Stores information about the player
    """
    def __init__(self,current_level=1):

        self.current_level = current_level


def create_surface_text(text, font_size,text_rgb,bg_rgb):
    """
    :param text: string of font to pick
    the type of text that you one would want
    :param font_size: int
    size of the font that the user wants
    :param text_rgb: (text color) - tuple (r,g,b)
    color of the text
    :param bg_rgb: (background color) - tuple (r,g,b)
    :return:
    returns surface with text written on it
    """

    font = pygame.freetype.SysFont("Courier",font_size,bold=True)
    surface, _ = font.render(text=text,fgcolor=text_rgb,bgcolor=bg_rgb)
    return surface.convert_alpha()

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NEXT_LEVEL = 2
class UIElement(Sprite):
    """An user interface element that can be added to a surface"""

    def __init__(self,center_position,text,font_size,bg_rgb,text_rgb,action=None):
        """
        :param self: the object itself
        :param center_position: -tuple (x,y)
        :param text: string of text to write
        :param font_size: int
        :param bg_rgb: (background color) - tuple (r,g,b)
        :param text_rgb: (text color) - tuple (r,g,b)
        :return:
        creates the object only
        """
        self.mouse_over = False

        # default image
        default_image = create_surface_text(
            text=text, font_size=font_size, text_rgb=text_rgb,bg_rgb=bg_rgb
        )

        # highlighted image
        hovered_image = create_surface_text(
            text=text,font_size=font_size*1.2 , text_rgb=text_rgb , bg_rgb=bg_rgb
        )

        self.images = [default_image, hovered_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            hovered_image.get_rect(center=center_position)
        ]

        self.action = action
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self,mouse_pos,mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        #changes image depending on if the mouse is hovering or not
        surface.blit(self.image,self.rect)


def game_loop(screen, buttons):
    """
    Handles game loop until an action is returned by a button in the
    buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(graphics.BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
        buttons.draw(screen)
        pygame.display.flip()

def title_screen(screen):
    start_btn = UIElement(
        center_position=(400,400),
        font_size=30,
        bg_rgb = graphics.BLUE,
        text_rgb=graphics.WHITE,
        text="Start",
        action = GameState.NEWGAME
    )

    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=graphics.BLUE,
        text_rgb=graphics.WHITE,
        text="Quit",
        action=GameState.QUIT
    )
    buttons = RenderUpdates(start_btn,quit_btn)

    return game_loop(screen,buttons)

def play_level(screen,player):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb = graphics.BLUE,
        text_rgb = graphics.WHITE,
        text="Return to main menu",
        action = GameState.TITLE,
    )
    nextlevel_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=graphics.BLUE,
        text_rgb=graphics.WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL
    )

    buttons = RenderUpdates(return_btn, nextlevel_btn)
    return game_loop(screen,buttons)
