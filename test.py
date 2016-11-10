def print_table(inventory, order=None):
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
    list_help.append('{:<30}'.format('-'*27))
    # it's alive!
    for item in inventory:
        print(item, inventory[item][0], inventory[item][1])
        list_help.append('{it:^3}|{t1:^3}|{t2:20}'.format(it=item, t1=inventory[item][0], t2=inventory[item][1]))

    list_help.append('{:<30}'.format('-'*27))
    list_help.append('Total items: {}'.format(total))
    return list_help


def item_attributes(name, weight=1, it_type='Other'):
    atributes = '{:^8}{:^3}{:^9}'.format(name, weight, it_type)
    return atributes


def main():
    inventory = {'^': [0, item_attributes(name='czapka', weight=2, it_type='Clothes')],
                 '&': [0, item_attributes(name='szal', weight=1, it_type='Clothes')],
                 '%': [0, item_attributes(name='browar', weight=5, it_type='Food')],
                 '*': [0, item_attributes(name='ciastko', weight=1, it_type='Food')],
                 '!': [0, item_attributes(name='patyk', weight=2)]}

    inv = print_table(inventory)
    print(inv)

if __name__ == '__main__':
    main()
