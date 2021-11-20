from documentation_pkg.userclass import Players, User

def welcome_page():
    print('|-----------------------------------------------------------------')
    print('|░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗')
    print('|░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝')
    print('|░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░')
    print('|░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░')
    print('|░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗')
    print('|░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝')
    print('|                                  |')
    print('|----------------------------------|')
    print('| ')
    print('███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗')
    print('████╗░████║██╔══██╗██║░░░██║██║██╔════╝')
    print('██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░')
    print('██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░')
    print('██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗')
    print('╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝')
    print('|----------------------------------|')
    print('|    1.Start    |    2.Exit        |')
    print('|----------------------------------|')

def player_menu():
    print('|----------------------------------|')
    print('|                                  |')
    print('|         Select a player          |')
    print('|                                  |')
    print('|----------------------------------|')
    print('|  1. One player  |  2. Two player |')
    print('|----------------------------------|')

def twoplayer_menu():
    print('|                                  |')
    print('|           P l a y e r  1         |')
    print('|                                  |')
    name1 = input('               Name: ')
    print('|                                  |')
    print('|                                  |')
    print()
    print('|            P l a y e r  2        |')
    print('|                                  |')
    name2 = input('               Name: ')
    print('|                                  |')
    print('|                                  |')
    print()
    print()
    player1 = Players(name1)
    player1.display_score()
    print()
    player2 = Players(name2)
    player2.display_score()
    print()
    print()

# note: I may have to create a function in this file to try and export it to a qa file.
# create a short function that returns the name of the players only player 1 and player 2 
#later this function can be called after the player has been create

def press_start():
   print()
   print('|-----------------------------------|')
   print('|                                   |')
   print('|         Let the game begin        |')
   print('|                                   |')
   print('|-----------------------------------|')
   print('|             1. Start              |')
   print('|-----------------------------------|')
   print()

def choose_genre():
    print('|----------------------------------|')
    print('|                                  |')
    print('|            Pick a genre          |')
    print('|                                  |')
    print('|----------------------------------|')
    print('|  1. Romance    |    2. Drama     |')
    print('|----------------------------------|')
    print('|  3. Horror    |     4. Action    |')
    print('|----------------------------------|')
    print('|  5. Comedy    |     6. Sci-Fi    |')
    print('|----------------------------------|')

