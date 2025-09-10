from turtle import Turtle

COLOURS = ["red", "orange", "yellow", "green"]
FULL_SIZE = 3.8
HALF_SIZE = 1.9


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.all_blocks = []

    def create_blocks(self):
        pos_y = 228
        for row in range(4):
            #stagger alternate rows
            if row % 2 == 0:
                pos_x = -360
                for ctr in range(10):
                    new_block = Turtle("square")
                    new_block.shapesize(stretch_wid=1, stretch_len=FULL_SIZE)
                    new_block.penup()
                    new_block.color(COLOURS[row])
                    new_block.goto(pos_x, pos_y)
                    pos_x += 80
                    self.all_blocks.append(new_block)
            else:
                pos_x = -380
                for ctr in range(11):
                    new_block = Turtle("square")
                    new_block.penup()
                    new_block.color(COLOURS[row])
                    if ctr == 0 or ctr == 10:
                        if ctr == 10:
                            pos_x -= 20
                        new_block.shapesize(stretch_wid=1, stretch_len=HALF_SIZE)
                        new_block.goto(pos_x, pos_y)
                        pos_x += 60
                    else:
                        new_block.shapesize(stretch_wid=1, stretch_len=FULL_SIZE)
                        new_block.goto(pos_x, pos_y)
                        pos_x += 80
                    self.all_blocks.append(new_block)
            pos_y -= 22
