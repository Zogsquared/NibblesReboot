import pygame
import sys
import random

pygame.display.set_caption('Snake Game 2')

class Snake():
    def __init__(self):
        self.length = 2
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (247, 27, 93)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)

        if len(self.positions) >= screen_height or new in self.positions[screen_height:]:
            self.reset()
        
        if len(self.positions) >= screen_width or new in self.positions[screen_width:]:
            self.reset()

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
            #self.score = 0
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
                

    def reset(self):
        self.length = 2
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        end()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (227, 27, 93), r, 5)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize,
                         random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (0, 0, 0), r, 1)


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (40, 237, 83), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize),
                                 (gridsize, gridsize))
                pygame.draw.rect(surface, (40, 227, 83), rr)


screen_width = 1000
screen_height = 1000

gridsize = 50
grid_width = screen_height / gridsize
grid_height = screen_width / gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

#finalscore = 0


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("comic sans", 36)

    global score

    score = 0
    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            score += 1
            food.randomize_position()
        if snake.get_head_position() == screen_height:
            end()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("Score: {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


def start():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    

    myfont = pygame.font.SysFont("arial", 82)
    myfont2 = pygame.font.SysFont("arial", 62)
    
    while (True):
        clock.tick(10)
        screen.blit(surface, (0, 0))
        text = myfont.render("Snake Game 2", 1, (0, 0, 0))
        screen.blit(text, (210, 200))
        image = pygame.image.load(r'Screenshot_1.png')
        screen.blit(image, (400, 375))
        text2 = myfont2.render("Press any key to Start", 1, (0, 0, 0))
        screen.blit(text2, (180, 700))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    main()
                    
def end():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    myfont = pygame.font.SysFont("arial", 82)
    myfont2 = pygame.font.SysFont("arial", 62)
    cooldown = 20
    
    while (True):
        clock.tick(10)
        cooldown -= 1
        screen.blit(surface, (0, 0))
        text = myfont.render("Game Over", 1, (0, 0, 0))
        screen.blit(text, (180, 200))
        text2 = myfont2.render("Score: {0}".format(score), 1, (0, 0, 0))
        screen.blit(text2, (180, 400))
        text3 = myfont2.render("Press any key to Start", 1, (0, 0, 0))
        screen.blit(text3, (180, 700))
        pygame.display.update()
        if cooldown < 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    main()

start()
#main()
