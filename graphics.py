import pygame
#global color values
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)


class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row , self.col

    """
    def is_func():
    
    these sets of is_what() returning the respective color 
    for their status red = closed, green==open, and so on.
    """
    def is_closed(self):

        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == BLACK

    def is_end(self):
        return self.color == TURQUOISE


    def reset(self):
        """resets the color of the spot to white"""
        self.color = WHITE

    """ 
    def make_status():
    just like the respective is_funcs(): 
    alters the status instead of retriving the value
    colors correspond in the same way
    """
    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = TURQUOISE

    def draw(self,win):
        """
        :param win:
        the window of the game that is being played
        :return:
        nothing as it's a void function that just draws the spot only
        """
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbors(self,grid):
        """
        :param grid:
        grid object that contains all the spots are in use of the game
        :return:
        nothing as it just updates the neighbors for the respective spot
        """
        self.neighbors = []

        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors(grid[self.row-1][self.col])

        if self.col < self.total_rows -1 and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])


    def __lt__(self,other):
        """
        :param other:
        another spot object
        :return:
        always returns a false value to state that it's larger when compared to another
        """
        return False


def draw_grid(win,rows,width):
    """

    :param win:
    the window of the game that is being played on
    :param rows:
    the current active grid's rows that are being used in the game
    :param width:
    respective width of each indivdual spot
    :return:
    nothing as it just draws a new grid everytime
    """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        for j in range(rows):
            pygame.draw.line(win,GREY,(j*gap,0), (j*gap,width))


def draw(win,grid,rows,width):
    """

    :param win:
    the window of the game that is being played on
    :param grid:
    grid object that contains all the spots are in use of the game
    :param rows:
    the current active grid's rows that are being used in the game
    :param width:
     respective width of each indivdual spot
    :return:
    nothing as it just updates the display and draws a new screen
    """
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win,rows,width)
    pygame.display.update()