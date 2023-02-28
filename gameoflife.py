import sys
import pygame

SCALE = 10
TARGET_FPS = 25
OFFSET = 10

BACKGROUND = (0,5,24)
AXIS_COLOUR = (17,24,53)
WHITE = (255,255,255)

WIDTH = 800
HEIGHT = 600

SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.font.init()

TEXT_FONT = pygame.font.SysFont("comicsans", 50)
pause_text = TEXT_FONT.render("PAUSED ", True, WHITE)


class Grid:

    def __init__(self):
        self.matrix = [[0 for j in range(WIDTH // SCALE + 2 * OFFSET)] for i in range(HEIGHT // SCALE + 2 * OFFSET)]

    def set(self, val, *lst):
        for l in lst:
            self.matrix[-l[1] + HEIGHT // SCALE // 2 + OFFSET - 1][l[0] + WIDTH // SCALE // 2 + OFFSET] = val

    def show(self):
        for w in range(WIDTH // SCALE + 2 * OFFSET):
            for h in range(HEIGHT // SCALE + 2 * OFFSET):
                if self.matrix[h][w] == 1:
                    pygame.draw.rect(SCREEN, WHITE, ((w - OFFSET) * SCALE, (h - OFFSET) * SCALE, SCALE, SCALE))

    def next(self):

        self.new_matrix = [[0 for j in range(WIDTH // SCALE + 2 * OFFSET)] for i in range(HEIGHT // SCALE + 2 * OFFSET)]

        for w in range(1, WIDTH // SCALE + 2 * OFFSET - 1):
            for h in range(1, HEIGHT // SCALE  + 2 * OFFSET - 1):

                neighbours = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbours += self.matrix[h + j][w + i]

                neighbours -= self.matrix[h][w]

                if neighbours == 3:
                    self.new_matrix[h][w] = 1

                if neighbours == 2:
                    self.new_matrix[h][w] = self.matrix[h][w]
        
        self.matrix = self.new_matrix


def draw_grid():

    pygame.draw.line(SCREEN, AXIS_COLOUR, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), width = 1)
    pygame.draw.line(SCREEN, AXIS_COLOUR, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), width = 1)

    for axis_var in range(1, WIDTH // (SCALE * 2)):
        
        pygame.draw.line(SCREEN, AXIS_COLOUR, (WIDTH / 2 + SCALE * axis_var, 0), (WIDTH / 2 + SCALE * axis_var, HEIGHT))
        pygame.draw.line(SCREEN, AXIS_COLOUR, (WIDTH / 2 - SCALE * axis_var, 0), (WIDTH / 2 - SCALE * axis_var, HEIGHT))

    for axis_var in range(1, HEIGHT // (SCALE * 2)):
        
        pygame.draw.line(SCREEN, AXIS_COLOUR, (0, HEIGHT / 2 + SCALE * axis_var), (WIDTH, HEIGHT / 2 + SCALE * axis_var))
        pygame.draw.line(SCREEN, AXIS_COLOUR, (0, HEIGHT / 2 - SCALE * axis_var), (WIDTH, HEIGHT / 2 - SCALE * axis_var))


grid = Grid()

running = False
RUNNING_FPS = 0

while True:
    
    clock.tick(RUNNING_FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            running = not running

    SCREEN.fill(BACKGROUND)

    grid.show()
    draw_grid()

    if running:
        RUNNING_FPS = TARGET_FPS
        grid.next()
    
    else:
        SCREEN.blit(pause_text, (WIDTH - 10 - pause_text.get_width(), 10))
        RUNNING_FPS = 0

        pos = pygame.mouse.get_pos()
        pos = (pos[0] // SCALE - WIDTH // SCALE // 2, - pos[1] // SCALE + HEIGHT // SCALE // 2)

        mouse_state_L = pygame.mouse.get_pressed()[0]
        mouse_state_R = pygame.mouse.get_pressed()[2]

        if mouse_state_L:
            grid.set(1, pos)

        elif mouse_state_R:
            grid.set(0, pos)

    pygame.display.update()
