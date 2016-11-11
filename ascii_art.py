import time
import os
from getch import pause


def intro():
    game_name = ("""\033[1;32;1m

                    ___________.__
                    \__    ___/|  |__    ____
                      |    |   |  |  \ _/ __ \\
                      |    |   |   Y  \\\\  ___/
                      |____|   |___|  / \___  >
                                    \/      \/\033[1;31;1m
        __      __         .__    __    .__
       /  \    /  \_____   |  |  |  | __|__|  ____    ____
       \   \/\/   /\__  \  |  |  |  |/ /|  | /    \  / ___\\
        \        /  / __ \_|  |__|    < |  ||   |  \/ /_/  >
         \__/\  /  (____  /|____/|__|_ \|__||___|  /\___  /
              \/        \/            \/         \//_____/
                    \tAnd Picking Up Items!\033[0m\033[1;34;1m
                  ________
                 /  _____/ _____     _____    ____
                /   \  ___ \__  \   /     \ _/ __ \\
                \    \_\  \ / __ \_|  Y Y  \\\\  ___/
                 \______  /(____  /|__|_|  / \___  >
                        \/      \/       \/      \/\033[0m

    """)
    os.system('clear')
    print(game_name)
    time.sleep(1)
    pause()


def know_how():

    know_how = ("""
    \033[0;34;1m
     __  __                                  __  __
    /\ \/\ \                                /\ \/\ \\
    \ \ \/'/'    ___     ___   __  __  __   \ \ \_\ \    ___   __  __  __
     \ \ , <   /' _ `\  / __`\/\ \/\ \/\ \   \ \  _  \  / __`\/\ \/\ \/\ \\
      \ \ \\\\`\ /\ \/\ \/\ \L\ \ \ \_/ \_/ \   \ \ \ \ \/\ \L\ \ \ \_/ \_/ \\
       \ \_\ \_\ \_\ \_\ \____/\ \___x___/'    \ \_\ \_\ \____/\ \___x___/'
        \/_/\/_/\/_/\/_/\/___/  \/__//__/       \/_/\/_/\/___/  \/__//__/\033[0m

    """)

    print(know_how)

    print("\nThe world is in great danger... Well, maybe not whole world...\
    \nBut the part of it... Really important part! Codecool! Collect items,\
    \ntravel through raw and brutal world of early access Walking And Picking up Items Game\
    \nbeat the boss and fulfill your destiny...")

    print("\n\033[0;32;1mCONTROLS:\033[0m\n\nW go up\nS go down\nA go left\nD go right\n")

    print("Collect 5 items to open portal to next level.")

    print("\n\033[0;33;1mTHIS GAME WAS CREATED BY:\033[0m\n\nKlaudia Borowska\nCezary'Czarosław' Broś\
    \nTomasz Budkiewicz\nGrzegorz Bury")
    pause()


def boss_init():
    boss_art = ("""
    \033[1;30;1m                                   _
    \033[1;30;1m                                ==(W{==========-\033[1;32;1m      /===-
    \033[1;30;1m                                  ||  (.--.)\033[1;32;1m         /===-_---~~~~~~~~~------____
    \033[1;30;1m                                  | \_,|**|,__  \033[1;32;1m    |===-~___                _,-'
    \033[1;32;1m                     -==\\\033[1;30;1m        `\ ' `--'   ),\033[1;32;1m    `//~\\   ~~~~`---.___.-~~
    \033[1;32;1m                 ______-==|\033[1;30;1m        /`\_. .__/\ \ \033[1;32;1m   | |  \\           _-~`
    \033[1;32;1m           __--~~~  ,-/-==\\ \033[1;30;1m     (   | .  |~~~~| \033[1;32;1m  | |   `\        ,'
    \033[1;32;1m        _-~       /'    |  \\ \033[1;30;1m    )__/==0==-\<>/   \033[1;32;1m/ /      \      /
    \033[1;32;1m      .'        /       |   \\ \033[1;30;1m     /~\___/~~\/  \033[1;32;1m/' /        \   /'
    \033[1;32;1m     /  ____  /         |    \`\.__\033[1;30;1m/\033[1;32;1m-~~   \033[1;30;1m\  |\033[1;32;1m_/'  /          \/'
    \033[1;32;1m    /-'~    ~~~~~---__  |     ~-/~         \033[1;30;1m( )\033[1;32;1m   /'        _--~`
    \033[1;32;1m                      \_|      /        _) \033[1;30;1m| ;\033[1;32;1m  ),   __--~~
    \033[1;32;1m                        '~~--_/      _-~/- \033[1;30;1m|/\033[1;32;1m \   '-~ \\
    \033[1;32;1m                       {\__--_/}    / \\_>-\033[1;30;1m|)\033[1;32;1m<__\      \\
    \033[1;32;1m                       /'   (_/  _-~  | |__>--<__|      |
    \033[1;32;1m                      |   _/) )-~     | |__>--<__|      |
    \033[1;32;1m                      / /~ ,_/       / /__>---<__/      |
    \033[1;32;1m                     o-o _//        /-~_>---<__-~      /
    \033[1;32;1m                     (^(~          /~_>---<__-      _-~
    \033[1;31;1m                    ,/|\033[0m\033[1;32;1m           /__>--<__/     _-~
    \033[1;31;1m                 ,//('(\033[0m\033[1;32;1m          |__>--<__|     /                  .----_
    \033[1;31;1m                ( ( '))\033[0m\033[1;32;1m          |__>--<__|    |                 /' _---_~\\
    \033[1;31;1m             `-)) )) (\033[0m\033[1;32;1m           |__>--<__|    |               /'  /     ~\`\\
    \033[1;31;1m            ,/,'//( (\033[0m\033[1;32;1m             \__>--<__\    \            /'  //        ||
    \033[1;31;1m          ,( ( ((, ))\033[0m\033[1;32;1m              ~-__>--<_~-_  ~--____---~' _/'/        /'
    \033[1;31;1m        `~/  )` ) ,/|\033[0m\033[1;32;1m                 ~-_~>--<_/-__       __-~ _/
    \033[1;31;1m      ._-~//( )/ )) `\033[0m\033[1;32;1m                    ~~-'_/_/ /~~~~~~~__--~
    \033[1;31;1m       ;'( ')/ ,)(\033[0m\033[1;32;1m                              ~~~~~~~~~~
    \033[1;31;1m      ' ') '( (/\033[0m
    \033[1;31;1m        '   '  `\033[0m

            """)
    print(boss_art)
    print("\n\n\n\033[4;30;47mYou've travelled long way just to find your end,\
    \nall this items, all this puzzles, all this adventures for nothing!\
    \nI should make more than just three levels, maybe next time uhh... nevermind.\
    \nI know your destiny, it's death from my hand!\
    \nYou have only one chance to defeat me, play a game called 'Cold Hot'.\
    \nI shouldn't tell you about this, but it's too late. Play for your life and\
    \nsafety of this pathetic world... I mean Codecool!\033[0m\n")
    pause()
