import os
import time
from getch import getch, pause
from knowhow import you_know_it
from welcomescreen import intro


ITEMS = ['^', '&', '%', '!', '*']


def loot_table(inventory, order=None):
    '''Prints formatted inventory depending on order (default=None).

    Args:
        inventory (dict): current inventory
        order (str, optional): if left unfilled prints unsorted inventory,
            'count,asc' prints sorted inventory ascending based on item count
            'count,desc' prints sorted inventory descending based in item count
    '''
    list_help = []
    total = 0
    list_help.append('{:30}'.format('Inventory:'))
    list_help.append('{t1:^3}|{t3:^3}|{t2:^8}|{t4:^3}|{t5:^9}'.format(t1='it', t2='name', t3='cnt',
                     t4='wgt', t5='type'))
    list_help.append('{:<30}'.format('-'*29))
    # it's alive!
    for item in inventory:
        list_help.append('{it:^3}|{t1:^3}|{t2:20}'.format(it=item, t1=inventory[item][0], t2=inventory[item][1]))
        total += inventory[item][0]

    list_help.append('{:<30}'.format('-'*29))
    list_help.append('{text:<30}'.format(text='Total items: %s' % total))
    return list_help


def create_board(inv):
    # board = [['.' if y > 0 and y < 39 else '\033[7;30;43m' + '#' + '\033[0m' for y in range(40)] if x > 0 and x < 19
    #          else ['\033[7;30;43m' + '#' + '\033[0m' for x in range(40)] for x in range(20)]
    board = []
    for row in range(20):
        rows = []
        for cell in range(40):
            if row == 0 or row == 19:
                rows.append('#')
            else:
                if cell == 0 or cell == 39:
                    rows.append('#')
                else:
                    rows.append(' ')
        board.append(rows)
    board = building_gen(board)
    return board


def building_gen(board):
    # print(board)
    for x in range(3, 8):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(3, 7):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + 'x' + '\x1b[0m'
    for x in range(28, 34):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(2, 10):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + 'x' + '\x1b[0m'
    for x in range(20, 25):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(12, 18):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + 'x' + '\x1b[0m'
    for x in range(4, 9):  # x-na szeroskosc/ex.(10,12) its 2*x count fr.left/10
        for y in range(11, 17):  # x-na dlugosc/(3,7) its 4*x and count fr. up-down/3
            board[y][x] = '\x1b[1;31;1m' + 'x' + '\x1b[0m'
    return board


def print_board(board, inv):
    for row in range(len(board)):
        if row in range(len(inv)):
            print('{:<30}{}'.format(inv[row], ''.join(board[row])))
        else:
            print('{:30}{}'.format('', ''.join(board[row])))


def hero_pos(board, x=10, y=10):
    board[y][x] = '\033[1;33;1m' + '@' + '\033[0m'
    return x, y


def walk(board, x, y, inv):
    move = getch()

    limit_x = x
    limit_y = y

    board[y][x] = ' '
    if move == 'w':
        y -= 1
    elif move == 's':
        y += 1
    elif move == 'a':
        x -= 1
    elif move == 'd':
        x += 1
    elif move == 'q':
        exit()

    if board[y][x] in ITEMS:
        inv = add_inv(inv, board[y][x])

    if board[y][x] == '#':
        x = limit_x
        y = limit_y

    if board[y][x] == '\x1b[1;31;1m' + 'x' + '\x1b[0m':
        x = limit_x
        y = limit_y

    x, y = hero_pos(board, x, y)
    return x, y, inv


def item_pos(item_sign, board, a=15, b=20):
    board[a][b] = item_sign


def add_inv(inventory, item):
    if item in inventory:
        inventory[item][0] += 1
    return inventory


def item_attributes(name, weight=1, it_type='Other'):
    atributes = '{:^8}|{:^3}|{:^9}'.format(name, weight, it_type)
    return atributes


def main():
    intro()
    you_know_it()
    inventory = {'^': [0, item_attributes(name='czapka', weight=2, it_type='Clothes')],
                 '&': [0, item_attributes(name='szal', weight=1, it_type='Clothes')],
                 '%': [0, item_attributes(name='browar', weight=5, it_type='Food')],
                 '*': [0, item_attributes(name='ciastko', weight=1, it_type='Food')],
                 '!': [0, item_attributes(name='patyk', weight=2)]}

    os.system('clear')
    inv = loot_table(inventory)
    game_board = create_board(inv)
    x, y = hero_pos(game_board)
    item_pos('&', game_board)
    item_pos('%', game_board, 8, 28)
    item_pos('^', game_board, 5, 7)
    item_pos('!', game_board, 16, 30)
    item_pos('*', game_board, 16, 4)
    while True:
        os.system('clear')
        print_board(game_board, inv)
        x, y, inventory = walk(game_board, x, y, inventory)
        inv = loot_table(inventory)

if __name__ == '__main__':
    main()
