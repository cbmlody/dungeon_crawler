import os
from random import randint

OBSTACLES = ['#', '\x1b[1;32;1m' + '🌵' + '\x1b[0m', '⛰', '\x1b[1;31;1m' + '⌂' + '\x1b[0m', '🌳']


def create_board(level):
    board = [[' ' if y > 0 and y < 39 else '\033[7;30;43m' + '#' + '\033[0m' for y in range(40)] if x > 0 and x < 19
             else ['\033[7;30;43m' + '#' + '\033[0m' for x in range(40)] for x in range(20)]
    if level == 1:
        board = board_obstacle_one(board)
    elif level == 2:
        board = board_obstacle_two(board)
    elif level == 3:
        board = board_obstacle_three(board)
    return board


def board_obstacle_one(board):
    # print(board)
    for x in range(3, 8):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(3, 7):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + '⌂' + '\x1b[0m'
    for x in range(28, 34):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(2, 10):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + '⌂' + '\x1b[0m'
    for x in range(20, 25):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(12, 18):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + '⌂' + '\x1b[0m'
    for x in range(4, 9):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(11, 17):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + '⌂' + '\x1b[0m'

    item_pos('\x1b[1;22;1m'+'&'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'^'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'%'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'!'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'*'+'\x1b[0m', board)
    return board


def board_obstacle_two(board):
    # print(board)
    for x in range(randint(1, 3)):
        for obstacle in OBSTACLES[1:]:
            length = randint(2, 18)
            height = randint(3, 8)
            mod_x = randint(5, 20)
            mod_y = randint(3, 10)
            for x in range(length):
                for y in range(height):
                    board[y + mod_y][x + mod_x] = obstacle
    item_pos('\x1b[1;22;1m'+'&'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'^'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'%'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'!'+'\x1b[0m', board)
    item_pos('\x1b[1;22;1m'+'*'+'\x1b[0m', board)
    return board


def board_obstacle_three(board):
    # print(board)
    for x in range(5, 6):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(3, 4):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(28, 29):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(9, 10):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(8, 9):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(18, 19):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(24, 25):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(18, 19):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(19, 20):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(13, 14):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(8, 9):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(16, 17):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(13, 14):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(18, 19):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(8, 9):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(10, 11):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(27, 28):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(7, 8):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    for x in range(27, 28):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(2, 3):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;32;1m' + '🌵' + '\x1b[0m'
    item_pos('&', board)
    item_pos('%', board, 8, 28)
    item_pos('^', board, 5, 7)
    item_pos('!', board, 16, 30)
    item_pos('*', board, 16, 4)
    return board


def print_board(board):
    for row in board:
        print('{}'.format(''.join(row)))


def item_pos(item_sign, board):
    y = randint(1, 18)
    x = randint(1, 38)
    if board[y][x] in OBSTACLES:
        if (board[y-1][x] or board[y+1][x] or board[y][x-1] or board[y][x+1]) not in OBSTACLES:
            board[y][x] = item_sign
        else:
            item_pos(item_sign, board)
    else:
        board[y][x] = item_sign


def main():
    level = 2
    game_board = create_board(level)
    os.system('clear')
    print_board(game_board)

if __name__ == '__main__':
    main()
