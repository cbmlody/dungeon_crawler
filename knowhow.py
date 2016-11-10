import os
from getch import pause


def you_know_it():

    know_how = ("""
     __  __                                  __  __
    /\ \/\ \                                /\ \/\ \\
    \ \ \/'/'    ___     ___   __  __  __   \ \ \_\ \    ___   __  __  __
     \ \ , <   /' _ `\  / __`\/\ \/\ \/\ \   \ \  _  \  / __`\/\ \/\ \/\ \\
      \ \ \\\\`\ /\ \/\ \/\ \L\ \ \ \_/ \_/ \   \ \ \ \ \/\ \L\ \ \ \_/ \_/ \\
       \ \_\ \_\ \_\ \_\ \____/\ \___x___/'    \ \_\ \_\ \____/\ \___x___/'
        \/_/\/_/\/_/\/_/\/___/  \/__//__/       \/_/\/_/\/___/  \/__//__/

    """)
    os.system('clear')
    print(know_how)

    print("The world is in great danger... Well, mayby not whole world...\
    But the part of it... Really important part! Codecool! Collect items,\
     travel through raw and brutal world, beat the boss and \
    fulfill your destiny.. And don't ask questions, ANY questions.")

    print("\nW go up\nS go down\nA go left\nD go right\n")

    print("THIS GAME WAS CREATED BY:\n\nKlaudia Borowska\nCezary'Czarosław' Broś\
            \nTomasz Budkiewicz\nGrzegorz Bury")
    pause()
