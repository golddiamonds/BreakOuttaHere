



import pygame
from pygame.locals import *
import objects as o
import screen as s
import input as i
from time import sleep


#note: not sure if Main is a great way to go
#been reading a lot of c/c++ code lately
class Main:
    def __init__(self):
        print 'Initializing game.'
        #using pygame
        pygame.init()
	self.clock = pygame.time.Clock()
        self.paddle = o.Paddle()
        self.ball = o.Ball()
        self.block_container = o.BlockContainer()
        self.screen = s.Screen(pygame)
        self.input = i.Input(pygame)

    def mainLoop(self):
        print 'Main game loop.'

        #loop here
        while (True):
            #check for user input
            self.input.checkInput()

            #if paused, skip everything
            if self.input.paused == 0:

                #paddlemovement
                #check input for paddle
                if self.input.left == 1:
                    self.paddle.moveLeft()
                elif self.input.right == 1:
                    self.paddle.moveRight()

                #ball movement
                self.ball.moveBall(self.paddle, self.block_container)
                #restart
                if self.ball.gameover == 1:
                    print 'gameover.'
                    self.ball.x = 300
                    self.ball.y = 400
                    self.paddle.x = 300
                    self.ball.x_move = 1
                    self.ball.y_move = 1
                    self.ball.gameover = 0

                #draw stuff to screen
                #screen needs to check location of objects
                #note: could just pass it ball, paddle and container
                self.screen.drawScreen(ballx=self.ball.x,bally=self.ball.y,
                                        paddlex=self.paddle.x, paddley=self.paddle.y,
                                        block_container=self.block_container)

                self.clock.tick(60)


    def quitGame(self):
        pygame.quit()
        print 'Thanks for playing!'


if __name__ == "__main__":
    game = Main()
    game.mainLoop()
    game.quitGame()
