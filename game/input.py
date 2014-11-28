
#note: using this for user input
import sys
from time import sleep

class Input():
    def __init__(self, pygame):
        self.pygame = pygame
        self.left = 0
        self.right = 0
        self.paused = 0

    def checkInput(self):
        #needs to run at least once each game loop
        for event in self.pygame.event.get():
            #quit game
            if event.type == self.pygame.QUIT:
                sys.exit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_LEFT:
                    self.leftKeyDown()
                if event.key == self.pygame.K_RIGHT:
                    self.rightKeyDown()
            if event.type == self.pygame.KEYUP:
                if event.key == self.pygame.K_LEFT:
                    self.leftKeyUp()
                if event.key == self.pygame.K_RIGHT:
                    self.rightKeyUp()
                if event.key == self.pygame.K_p:
                    self.pause()

    def leftKeyDown(self):
        #what left key does
        self.left = 1

    def rightKeyDown(self):
        #what right key does
        self.right = 1

    def leftKeyUp(self):
        self.left = 0

    def rightKeyUp(self):
        self.right = 0

    def pause(self):
        if self.paused == 0:
            self.paused = 1
            sleep(1)
        elif self.paused == 1:
            self.paused = 0
