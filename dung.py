from os import system
from random import randint, choice
from getch import getch, pause  # additional module for instant input reading
import ascii_art  # importing ascii arts
import cold_hot as boss_game  # importing cold_hot game


ITEMS = ['^', '%', '&', '!', '*']
OBSTACLES = ['\x1b[1;33;40m'+'#'+'\x1b[0m', '\x1b[1;33;1m'+'🌵'+'\x1b[0m', '\x1b[0;37;0m'+'⛰'+'\x1b[0m',
             '\x1b[1;31;1m'+'⌂'+'\x1b[0m', '\x1b[1;32;1m'+'🌳'+'\x1b[0m']
HERO_START_POS = ((1, 1), (1, 18), (38, 1), (38, 18))


def loot_table(inventory):
    '''Returns formatted inventory as list of strings for better screening.

    Args:
        inventory (dict): current inventory
    Returns:
        inv_formated: inventory foramted as list of strings
        total: total number of items in inventory
    '''
    inv_formated = []
    total = 0
    inv_formated.append('{:^44}'.format('\x1b[1;32;40m'+'INVENTORY'+'\x1b[0m'))
    inv_formated.append('{t1:^3}|{t3:^3}|{t2:^8}|{t4:^3}|{t5:^9}'.format(t1='it', t2='name', t3='cnt',
                        t4='wgt', t5='type'))
    inv_formated.append('{:<30}'.format('-'*29))

    for item in inventory:
        inv_formated.append('{it:^3}|{t1:^3}|{t2:20}'.format(it=item, t1=inventory[item][0], t2=inventory[item][1]))
        total += inventory[item][0]

    inv_formated.append('{:<30}'.format('-'*29))
    inv_formated.append('{text:<30}'.format(text='Total items: %s' % total))
    return inv_formated, total  # returns total to check how many items we have


def create_board():
    """Creates empty board and then adds obstacles to it.

    Returns:
        board (list): list of lists containing board elements
    """
    # board = [[' ' if y > 0 and y < 39 else '\033[7;30;43m' + '#' + '\033[0m' for y in range(40)] if x > 0 and x < 19
    #          else ['\033[7;30;43m' + '#' + '\033[0m' for x in range(40)] for x in range(20)]
    board = []

    for row in range(20):
        rows = []
        for cell in range(40):
            if row == 0 or row == 19:
                rows.append(OBSTACLES[0])
            else:
                if cell == 0 or cell == 39:
                    rows.append(OBSTACLES[0])
                else:
                    rows.append(' ')
        board.append(rows)
    baord = board_obstacle(board)
    return board


def board_obstacle(board):
    """Generating random obstacles on board

    Args:
        board (list): empty board generated as list of lists

    Returns:
        board (list): updated board with OBSTACLES elements
    """
    for x in range(randint(1, 3)):
        for obstacle in OBSTACLES[1:]:
            length = randint(2, 18)
            height = randint(3, 8)
            mod_x = randint(5, 20)
            mod_y = randint(3, 10)

            for x in range(length):
                for y in range(height):
                    board[y + mod_y][x + mod_x] = obstacle
    for item in ITEMS:
        item_pos(item, board)

    return board


def print_board(board, inv):
    """Prints inventory and board on terminal window

    Args:
        board (list): list of lists containing board elements to print
    """
    for row in range(len(board)):
        if row in range(len(inv)):
            print('{:<30}{}'.format(inv[row], ''.join(board[row])))
        else:
            print('{:30}{}'.format('', ''.join(board[row])))


def hero_pos(board, x=choice(HERO_START_POS)[0], y=choice(HERO_START_POS)[1]):  # choice allows to select random value from HERO_START_POS
    """Sets hero represented as @ on x, y position on board

    Args:
        board (list): list of lists which contains board elements
        x (int): x position of hero on board
        y (int): y position of hero on board

    Returns:
        x (int): x position of hero on board
        y (int): y position of hero on board
    """
    board[y][x] = '\033[1;33;1m' + '@' + '\033[0m'

    return x, y


def item_pos(item_sign, board):
    """Generates and places item on random positon on board

    Args:
        board (list): updated list of lists containing board elements
        item_sign (char): char which represents item_sign
    """
    y = randint(1, 18)
    x = randint(1, 38)

    if board[y][x] in OBSTACLES:
        if (board[y-1][x] or board[y+1][x] or board[y][x-1] or board[y][x+1]) not in OBSTACLES:  # checks if there aren't chars that blocks way to get to item
            board[y][x] = item_sign
        else:
            item_pos(item_sign, board)  # recurence which allows us to place the same item on different position
    else:
        board[y][x] = item_sign


def walk(board, x, y, inv):
    """Checks if hero can move to location by checking what element of board is on x, y position to wich hero should be moved.
    limit_x, limit_y are local variables storing current position, and if neccessary, used to restore hero position if he can't go in selected postion.
    If hero want to change position to item location, function add_inv() is called. If hero want to chage position to boss location, boss_game.main() is called.

    Args:
        board (list): list of lists containing board elements
        x (int): current x postion of hero
        y (int): current y postion of hero
        inv (dict): current dictionary holding items and their atributes

    Returns:
        x (int): new x hero position on board
        x (int): new y hero position on board
        inv (dict): current/upadted dictionary holdings items and their atributes
    """
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

    if board[y][x] in ITEMS:  # check if symbol on position x, y is in predefined ITEMS list
        inv = add_inv(inv, board[y][x])  # if yes call add_inv

    if board[y][x] in OBSTACLES:
        x = limit_x
        y = limit_y

    if board[y][x] == '😠':  # boss fight here
        system('clear')
        ascii_art.boss_init()  # boss ascii art initialization
        system('clear')
        boss_game.main()  # boss game initialization

    x, y = hero_pos(board, x, y)
    return x, y, inv


def add_inv(inventory, item):
    """Adds +1 to item count in inventory and returns updated inventory

    Args:
        inventory (dict): current dictionary holding items and their atributes
        item (char): char representing item

    Returns:
        inventory (dict): updated dictionary holding items and their atributes
    """
    if item in inventory:
        inventory[item][0] += 1
    return inventory


def item_attributes(name, weight, it_type='Other'):
    """Returns formatted string with item atributes

    Args:
        name (str): string representing item name
        weight (int): int representing item weight (for future use)
        it_type (str): string representing item type

    Returns:
        atributes (str): formatted string with item name, weight and type
    """
    atributes = '{:^8}|{:^3}|{:^9}'.format(name, weight, it_type)
    return atributes


def boss_position(board, x=37, y=17):  # hello boss
    """Spawns boss on x, y position on board

    Args:
        board (list): list of lists containing board elements
        x (int): boss x position on board
        y (int): boss y position on board

    Returns:
        board (list): updated list of lists containing board elements
    """
    board[y][x] = '😠'
    return board


def main():
    """Script main loop, which creates inventory, and calls ascii arts from external filesself."""
    ascii_art.intro()
    system('clear')
    ascii_art.know_how()
    inventory = {'^': [0, item_attributes(name='czapka', weight=2, it_type='Clothes')],
                 '&': [0, item_attributes(name='szal', weight=1, it_type='Clothes')],
                 '%': [0, item_attributes(name='browar', weight=5, it_type='Food')],
                 '*': [0, item_attributes(name='ciastko', weight=1, it_type='Food')],
                 '!': [0, item_attributes(name='patyk', weight=2)]}

    system('clear')
    level = 1
    inv, total_items = loot_table(inventory)
    game_board = create_board()
    x, y = hero_pos(game_board)

    while True:
        system('clear')

        if level == 1 and total_items == 5:
            level += 1
            game_board = create_board()
            x, y = hero_pos(game_board)

        elif level == 2 and total_items == 10:
            level += 1
            game_board = create_board()
            x, y = hero_pos(game_board)

        elif level == 3 and total_items == 15:
            game_board = boss_position(game_board)

        print_board(game_board, inv)
        x, y, inventory = walk(game_board, x, y, inventory)
        inv, total_items = loot_table(inventory)

if __name__ == '__main__':
    main()
