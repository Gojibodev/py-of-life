import random
import time
# import pygame

def create_board(width, height):
    return [[random.randint(0, 1) for _ in range(height)] for _ in range(width)]

def check(board,x,y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1,y+2):
            if (i != x or j != y) and 0 <= i < len(board) and 0 <= j < len(board[0]):
                count += board[i][j]  
    return count

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


def display_board(board):
    for width in board:
        width = ["\u25A0" if cell == 1 else " " for cell in width]
        print(" ".join(str(cell) for cell in width))
    
board = create_board(100, 100)
while True:
    print(chr(27) + "[2J")
    display_board(board)
    time.sleep(0.50)
    board = update_board(board)
