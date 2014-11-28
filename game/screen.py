
import random

#note: using this for all drawing to screen
class Screen:
    def __init__(self, pygame):
        #create screen
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Break Outta Here!')
        self.pygame = pygame

    def drawScreen(self, ballx, bally, paddlex, paddley, block_container):
        #needs to be run every game loop
        self.fillBackground()
        self.drawBlocks(block_container)
        self.drawBall(ballx, bally)
        self.drawPaddle(paddlex, paddley)
        self.screen.blit(self.background, (0, 0))
        self.pygame.display.flip()

    def fillBackground(self):
        self.background = self.pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 250, 250))

    def drawBall(self, x, y):
        self.pygame.draw.rect(self.background, (0,0,0), (x,y,10,10))

    def drawPaddle(self, x, y):
        self.pygame.draw.rect(self.background, (0,0,0), (x,y,40,10))

    def drawBlocks(self, block_container):
        i = 0
        for inner in block_container.container:
            j=0
            for block in inner:
                if block == 1:
                    x = 64 * i
                    y = 10 * j
                    self.drawSingleBlock(x, y)
                    j += 1
            i += 1

    def drawSingleBlock(self, x, y):
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)
        self.pygame.draw.rect(self.background, (r,b,g), (x,y,64,10))

if __name__ == "__main__":
    screen = Screen()
