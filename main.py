from solvalid import solve, valid
import pygame
import time
pygame.font.init()


class Grid:
    board = [
        [3, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 0],
        [2, 0, 0, 0, 3, 0, 8, 0, 5],
        [0, 8, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 6, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 4, 0],
        [5, 0, 4, 0, 1, 0, 0, 0, 3],
        [0, 6, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 4]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):  # add the value in its position if its valid
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()  # if there no value or the value that entered is 0 or Wrong value
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows+1):  # عشان يحدد تقسيمات المربعات الكبيرة
            if i % 3 == 0 and i != 0:
                thick = 3
            else:
                thick = 1
            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):  # يرسم المربعات الصغيرة داخل الكبار
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0) # allowing to remove unconfirmed value

    def click(self, pos):

        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return int(y), int(x)  # return the position of selected cube to select function
        else:
            return None

    def is_finished(self):  # chick if there no empty cells
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Cube:
    rows = 9

    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value  # the confirmed value cnt change it
        self.UnconfirmedValue = 0  # the value that are not confirmed write in  gray
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(line, win):  # to draw selected box and value in the box

        fnt = pygame.font.SysFont("Times New Roman", 30)  # sysfont to define font type and size
        """divide the box into 9 cells"""
        gap = line.width / 9
        x = line.col * gap  # number of cells in columns
        y = line.row * gap  # number of cells in row
        if line.UnconfirmedValue != 0 and line.value == 0:  # chick if it unconfirmed value or not
            text = fnt.render(str(line.UnconfirmedValue), 1, (128, 128, 128))  # write the unconfirmed value in light gray
            win.blit(text, (x + 5, y + 5)) # there comment in the end of file about render
            """blit(background,(x,y)) 
            where (x,y) is the position inside the window where we want the top left of the surface to be"""
        elif not (line.value == 0):
            text = fnt.render(str(line.value), 1, (0, 0, 0)) # write the confirmed value in black
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))  #set the position in the medile

        if line.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)  # draw red rectangular around the selected cell

    def set(self, val):
        self.value = val  # assign the confirmed value

    def set_temp(self, val):
        self.UnconfirmedValue = val  # assign the unconfirmed value


def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    # Draw time
    fnt = pygame.font.SysFont("Times New Roman", 20)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    win.blit(text, (540 - 160, 560))
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat


def main():
    win = pygame.display.set_mode((540, 600))  # to identify the window size width and height
    pygame.display.set_caption("Sudoku Game")
    board = Grid(9, 9, 540, 540)  # send the size to grid class (rows, cols, width, height)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  # detect if a key is physically pressed down
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].UnconfirmedValue != 0:
                        if board.place(board.cubes[i][j].UnconfirmedValue):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


main()

pygame.quit()


"""Rect class in Pygame and is used to store and manipulate a rectangular area.
             A Rect object can be created by giving:
             the 4 parameters left, top, width and height
             he position and size
             an object which has a rect attribute
             example :
             Rect(left, top, width, height)
             Rect(pos, size)
             Rect(obj)
             """


"""In pygame,text cannot be written directly to the screen.
 The first step is to create a Font object with a given font size.
  The second step is to render the text into an image with a given color. 
  The third step is to blit the image to the screen. 
  example:
font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, BLUE)
screen.blit(img, (20, 20))"""