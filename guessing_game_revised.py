#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------
print("=========================")
print("Number Guessing Game")
print("=========================")
import random
highscore = []
def start_game():
    
    player_input= input("Would you like to play a number guessing game? [Yes/No] ")
    random_number = random.randint(1,10)
    attempts = 0
    while player_input.lower() == "yes":
        try:
            question = int(input("Please pick a number between 1 and 10: "))
            attempts += 1
            if question < 1:
                print("That is outside of the range 1 and 10")
            elif question > 10:
                print("That is outside of the range 1 and 10")
            elif question > random_number:
                print("It's lower")
            elif question < random_number:
                print("It's higher")
            else:
                print("That is correct! You picked the right number in {} tries.".format(attempts))
                print("We hope you enjoyed playing the Number Guessing Game!")
                new_game = input("Would you like to play again? [Yes/No] ")
                highscore.append(attempts)
                if new_game.lower() == "yes":
                    print("The current highscore is {}.".format(min(highscore)))
                    print("You have attempted this game {} times. Thank you for playing!".format(len(highscore)))
                    start_game()
                break
        except ValueError:
            print("Oh no, invalid entry. That is not a number between 1 and 10")
            continue
    print("Have a great day")    
start_game()