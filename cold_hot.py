import random
from getch import pause_exit

def pick_number():
    """picking random number (three different digits)"""
    num0 = random.randint(0, 9)
    num1 = random.randint(0, 9)
    while num0 == num1:
        num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    while num2 == num0 or num1 == num2:
        num2 = random.randint(0, 9)
    number = [num0, num1, num2]
    return number


def guess_number(lives):
    """ask user to pick number(3 digits)"""
    user_input = str(input("Guess: #%s: " % (lives)))
    while len(user_input) != 3:
        user_input = str(input("Guess: #%s: " % (lives)))
    return user_input


def hot(random, guess):
    """check if hot == True"""
    guess_list = list(guess)
    result = []
    for i in range(len(guess_list)):
        if int(guess_list[i]) == int(random[i]):
            result.append("hot")
    return result


def warm(random, guess):
    """check if warm == True"""
    guess_list = list(guess)
    result = []
    for i in range(len(guess_list)):
        if int(guess_list[i]) in random:
            if int(guess_list[i]) == int(random[i]):
                pass
            else:
                result.append("warm")
    return result


def main():
    random_number = pick_number()
    hp = 1
    while hp < 11:
        picked_number = guess_number(hp)
        hot_list = hot(random_number, picked_number)
        warm_list = warm(random_number, picked_number)
        result = hot_list + warm_list
        if result == ["hot", "hot", "hot"]:
            print ("GZ")
            pause_exit()
            break
        if len(result) == 0:
            result.append("cold")
        print (result)
        hp += 1


if __name__ == '__main__':
    main()
