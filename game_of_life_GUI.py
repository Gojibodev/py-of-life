import random
import pygame


##############################################
#                                            #
#      Start of the games logic              #
#                                            #
##############################################

#Creates and fills a new board at random with 0s and 1s
def create_board(width, height):
    return [[random.randint(0, 1) for _ in range(height)] for _ in range(width)]

#Checks the sorrounding 8 cells if they are alive and returns their amount
def check(board,x,y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1,y+2):
            if (i != x or j != y) and 0 <= i < len(board) and 0 <= j < len(board[0]):
                count += board[i][j]  
    return count

#Initializes a new board with just 0s then checks the old board to decide wich cell is going to live
def update_board(board):
    new_board = [[0 for _ in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            alive = check(board,i,j)
            if board[i][j] == 1:
                if alive < 2 or alive > 3:
                    new_board[i][j] = 0 
                else:
                    new_board[i][j] = 1
            elif alive == 3:
                new_board[i][j] = 1
    return new_board


##############################################
#                                            #
#      Start of the GUI using pygame         #
#                                            #
##############################################

pygame.init()

# Set the dimensions of the game board
board_width = 100
board_height = 100

# Set the size of each cell in the game board
cell_size = 10

# Set the width and height of the screen (width, height).
size = (board_width * cell_size, board_height * cell_size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Py of Life")

# Create the game board with a random distribution of living and dead cells
board = [[random.randint(0, 1) for _ in range(board_height)] for _ in range(board_width)]

#Init of the necessary colors
black = (0, 0, 0)
white = (255, 255, 255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the game board
    for i in range(board_width):
        for j in range(board_height):
            if board[i][j] == 1:
                pygame.draw.rect(screen, white, (i*cell_size, j*cell_size, cell_size, cell_size))

    board = update_board(board)

    # Update the screen
    pygame.display.flip()

pygame.quit()
