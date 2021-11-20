from documentation_pkg.homepage import welcome_page, press_start, player_menu, choose_genre, twoplayer_menu
from documentation_pkg.questions_base import horror_questions, drama_questions, action_questions, comedy_questions,scifi_questions

welcome_page()
option = input("Choose an option: ")
print(option)
if option == "1":
        player_menu()
        print()
        option = input("Choose number of players: ")
        print()
        if option == "1": 
                print()
                press_start()
                print()
                option = input("Press 1 to start the game: ")
        elif option == "2":
                twoplayer_menu()
                option = input("Press 1 to start the game: ")
                print()
                print()
        else: 
                print("game over")
else:
        print("Noooooo! okay try again next time!")
        print()

"""TRIVIA QUESTIONS START HERE"""

choose_genre()
option = input("Choose a genre: ")
print()
if option == "1":
        #romance_questions()
        from documentation_pkg.linked_romance import linkedListRomance #error edit this
        print()
elif option == "2":
        drama_questions()
        print()
elif option == "3":
        horror_questions()
        print()
elif option == "4":
        action_questions()
        print()
elif option == "5":
        comedy_questions()
        print()
elif option == "6":
        scifi_questions()
        print()
else:
        print("bye")


