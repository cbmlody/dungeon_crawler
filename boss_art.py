from getch import pause


def boss_init():
    boss_art = ("""
                                   _
                                ==(W{==========-      /===-
                                  ||  (.--.)         /===-_---~~~~~~~~~------____
                                  | \_,|**|,__      |===-~___                _,-'
                     -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
                 ______-==|        /`\_. .__/\ \    | |  \\           _-~`
           __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
        _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
      .'        /       |   \\      /~\___/~~\/  /' /        \   /'
     /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
    /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                      \_|      /        _) | ;  ),   __--~~
                        '~~--_/      _-~/- |/ \   '-~ \\
                       {\__--_/}    / \\_>-|)<__\      \\
                       /'   (_/  _-~  | |__>--<__|      |
                      |   _/) )-~     | |__>--<__|      |
                      / /~ ,_/       / /__>---<__/      |
                     o-o _//        /-~_>---<__-~      /
                     (^(~          /~_>---<__-      _-~
                    ,/|           /__>--<__/     _-~
                 ,//('(          |__>--<__|     /                  .----_
                ( ( '))          |__>--<__|    |                 /' _---_~\\
             `-)) )) (           |__>--<__|    |               /'  /     ~\`\\
            ,/,'//( (             \__>--<__\    \            /'  //        ||
          ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
        `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
      ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
       ;'( ')/ ,)(                              ~~~~~~~~~~
      ' ') '( (/
        '   '  `

        """)
    print(boss_art)
    print("\n\n\n\033[4;30;47m You've travelled long way just to find your end.\
    I should make more than just three levels, next time, nevermind.\
    I know your destiny, it's death from my hand.\
    You have only one chance to defeat me, play a game, 'cold, warm, hot' game.\
    I shouldn't tell you about this, but it's too late. Play for your life, and\
    safety of this pathetic world!\033[47m\n")
    pause()
