
#note: I didn't want to store invidual game "objects"
# (e.g. paddle, ball, block) across multiple files.

class Paddle:
    def __init__(self):
        self.x = 300 #center
        self.y = 470 #never changes
        self.length_of_paddle = 40

    def moveLeft(self):
        if self.x - 1 > 0:
            self.x -= 1 #moved
        else:
            pass #at left edge

    def moveRight(self):
        if (self.x + 1) < (600 + self.length_of_paddle):
            self.x += 1 #moved
        else:
            pass #at right edge


class Ball:
    def __init__(self):
        self.x = 300 #center
        self.y = 400 #above paddle
        self.x_move = 1
        self.y_move = 1 #drop ball
        self.gameover = 0 #gameover?

    def moveBall(self, paddle, block_container):
        self.checkHit(paddle, block_container)
        self.x += self.x_move
        self.y += self.y_move

    def changeDirection(self, xmod, ymod):
        self.x_move += xmod
        self.y_move += ymod

    def checkHit(self, paddle, block_container):
        #logic for ball collision

        #check x sides
        if self.x > 630:
            self.x_move *= -1
        elif self.x < 1:
            self.x_move *= -1

        #check y sides
        if self.y < 1:
            self.y_move *= -1
        elif self.y > 469:
            self.gameover = 1

        #check paddle
        if (self.y + 10 >= paddle.y):
            if ((self.x >= paddle.x) and (self.x <= paddle.x + 40)):
                self.y_move *= -1

        #check for block collisions
        #ball location
        self.x, self.y
        #change into array coordinates
        i = 0
        for inner in block_container.container:
            j=0
            for block in inner:
                if block == 1:
                    x = 64 * i
                    y = 10 * j
                    if (self.y >= y) and (self.y <= y+10):
                        if (self.x >= x) and (self.x <= x + 64):
                            block_container.container[i][j] = 0
                            self.y_move *= -1
                    j += 1
            i += 1

#note: with simple blocks you do not
# really need a block object
class Block:
    def __init__(self):
        pass

class BlockContainer:
    def __init__(self):
        self.block_width = 64
        self.block_height = 20
        self.container_width = 10 #in blocks
        self.container_height = 10 #in blocks
        self.container = []
        self.initializeContainer()

    #should do multi-dimension list...
    def initializeContainer(self):
        #0 = no block; 1 = block;
        for i in range(0,self.container_width):
            #self.container.append([])
            inner_container = []
            for j in range(0, self.container_height):
                inner_container.append(1)
            self.container.append(inner_container)



    def checkForBlock(self):
        pass

    def removeBlock(self):
        pass


if __name__ == "__main__":
    block_container = BlockContainer()
    print block_container.container
