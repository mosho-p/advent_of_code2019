# Make board as a DataFrame with indices and columns centered at 0, 0
# (or 2 boards and set values to 1, then add them together and look for length of 2s)
# (a + b)[(a + b) == 2].stack().index.tolist() to get list of coordinates

import pandas as pd
import numpy as np 


def make_board(instructions, question1=True):
    board = pd.DataFrame([[0]], columns=[0], index=[0])
    x, y, i = 0, 0, 0
    for step in instructions:
        direction = step[0].lower()
        distance = int(step[1:])
        x, y, board = eval(f'{direction}({x}, {y}, {distance}, {i}, board, question1={question1})')
        i += distance
    board.loc[0, 0] = 0
    return board.fillna(0)


def r(x, y, n, count, board, question1=True):
    if board.columns.max() < y + n:
        board.loc[x, y+n] = 0
        board = expand_board(board)
    if question1:
        board.loc[x, y: y+n] = 1
    else:
        possible_line = board.loc[x, y: y+n]
        possible_line.loc[possible_line==0] = np.arange(count, count+n+1)[possible_line==0]
    return x, y + n, board

def l(x, y, n, count, board, question1=True):
    if board.columns.min() > y - n:
        board.loc[x, y-n] = 0
        board = expand_board(board)
    if question1:
        board.loc[x, y-n: y] = 1
    else:
        possible_line = board.loc[x, y-n: y]
        possible_line.loc[possible_line==0] = np.arange(count+n, count-1, -1)[possible_line==0]
    return x, y - n, board

def u(x, y, n, count, board, question1=True):
    if board.index.max() < x + n:
        board.loc[x+n, y] = 0
        board = expand_board(board)
    if question1:
        board.loc[x: x+n, y] = 1
    else:
        possible_line = board.loc[x: x+n, y]
        possible_line.loc[possible_line==0] = np.arange(count, count+n+1)[possible_line==0]
    return x + n, y, board

def d(x, y, n, count, board, question1=True):
    if board.index.min() > x - n:
        board.loc[x-n, y] = 0
        board = expand_board(board)
    if question1:
        board.loc[x-n: x, y] = 1
    else:
        possible_line = board.loc[x-n: x, y]
        possible_line.loc[possible_line==0] = np.arange(count+n, count-1, -1)[possible_line==0]
    return x - n, y, board

def expand_board(exp_brd):
    return exp_brd.T.reindex(pd.RangeIndex(exp_brd.columns.min(), exp_brd.columns.max()+1))\
                     .T.reindex(pd.RangeIndex(exp_brd.index.min(), exp_brd.index.max()+1)).fillna(0)

def answer1():
    with open('day3data.txt') as f:
        red = make_board(f.readline().split(','))
        green = make_board(f.readline().split(','))
    combined = red + green
    return min([abs(x) + abs(y) for x, y in combined[combined==2].stack().index])

def answer2(test=False):
    if not test:
        with open('day3data.txt') as f:
            red = make_board(f.readline().split(','), question1=False)
            green_instructions = f.readline().split(',')
    else:
        red = make_board('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','), question1=False)
        green_instructions='U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
    x, y, count = 0, 0, 0
    intersections = []
    for step in green_instructions:
        direction = step[0].lower()
        n = int(step[1:])
        if direction == 'r':
            if red.columns.max() < y + n:
                red.loc[x, y+n] = 0
                red = expand_board(red)
            possible_line = red.loc[x, y: y+n]
            if not possible_line.loc[possible_line!=0].empty:
                intersections.append((possible_line.loc[possible_line!=0]+np.arange(count, count+n+1)[possible_line!=0]).min())
            x, y = x, y + n
        elif direction == 'l':
            if red.columns.min() > y - n:
                red.loc[x, y-n] = 0
                red = expand_board(red)
            possible_line = red.loc[x, y-n: y]
            if not possible_line.loc[possible_line!=0].empty:
                intersections.append((possible_line.loc[possible_line!=0]+np.arange(count+n, count-1, -1)[possible_line!=0]).min())
            x, y = x, y - n
        elif direction == 'u':
            if red.index.max() < x + n:
                red.loc[x+n, y] = 0
                red = expand_board(red)
            possible_line = red.loc[x: x+n, y]
            if not possible_line.loc[possible_line!=0].empty:
                intersections.append((possible_line.loc[possible_line!=0]+np.arange(count, count+n+1)[possible_line!=0]).min())
            x, y = x + n, y
        elif direction == 'd':
            if red.index.min() > x - n:
                red.loc[x-n, y] = 0
                red = expand_board(red)
            possible_line = red.loc[x-n: x, y]
            if not possible_line.loc[possible_line!=0].empty:
                intersections.append((possible_line.loc[possible_line!=0]+np.arange(count+n, count-1, -1)[possible_line!=0]).min())
            x, y = x - n, y
        count += n
        # trace the red board:
        #   mask where red != 0
        #   if it's not empty, mask the np.arange(green_steps), add them, take the min
    return min(intersections)


if __name__ == '__main__':
    print(int(answer2()))
