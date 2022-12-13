from time import time, sleep
from random import choice

#display whenever the input is wrong
def hangman_display(num):
    hangman =["""                       ------|
                                        |                  
                                        |  
                                        |
                                        |
                                                        """,
                                                        """
                                            ------|
                                            |     O <it's okay everyone made mistake:D
                                            |            
                                            |
                                            |             
                                                        """,
                                                        """
                                            ------|
                                            |     O < again.?
                                            |    /
                                            |
                                            |            
                                                        """,
                                                        """
                                            ------|
                                            |     O <Oh boy!
                                            |    /|
                                            |
                                            |            
                                                        """,
                                                        """
                                            ------|
                                            |     O <Oh no!
                                            |    /|\\
                                            |
                                            |       
                                                        """,
                                                        """
                                            ------|
                                            |     O <Praying.....
                                            |    /|\\
                                            |    /
                                            |
                                                        """,
                                                        """
                                            ------|
                                            |     O <Goodbye!ouch!
                                            |    /|\\
                                            |    / \\
                                            |            
                                                        """]

    return hangman[num]

# safe man
def safe_hangman(name):
    print(                                                        f"""
                                            
                                                 O <phew! Good Job! {name}
                                                /|\\
                                                / \\
                                                        
                                            """)

list_of_words = ['machine', 'incredible', 'honest', 'stadium', 'player', 'normal', 'triangle']

#get the name of the user
user_name = input("Input user name here: ").upper()
print(f"          Hello! {user_name} Welcome to Hangman!")
print("In this game you only have 30 seconds to guess the missing word")
print("You can input as much as you like, but be aware of getting hang if you input a wrong letter/word. Enjoy!")
print("---------------------------------------------------------------------------------------------")
print()
max_guesses = 0
repeater = True
words = choice(list_of_words)
guess_letter = []
#ask user if start or exit
start_input = input("Input 'start' and your 30 seconds will start.: ").lower()
if start_input == 'start':
    timer = round(time()) + 30
    while repeater: 
            for letter in words:
                if letter.lower() in guess_letter:
                    print(letter, end=" ")
                else:
                    print("_ ", end=" ")
            print()
            user_guess_input = input(f"Input guess here: ").lower()
            guess_letter.append(user_guess_input)

            #for the wrong input
            if user_guess_input not in words:
                max_guesses = max_guesses + 1
                print(hangman_display(max_guesses))
                print(f"{user_guess_input} is not part of the word")

                #user used all the guesses
                if max_guesses == 6:
                    print(f"Game Over! You failed!")
                    print()
                    break
            
            #user get the right word
            if user_guess_input == words:
                print()
                safe_hangman(user_name)
                print(f"Congratulation {user_name} you guessed the missing word")
                print(f"You answered '{user_guess_input}'")
                print(f"Missing word is '{words}'")
                print()
                break
            
            #timer stopper
            if round(time()) >= timer:
                print("Game Over! Time's up!!")
                print()
                break
else:
    print("Thank you for visiting Hangman ")
    print()



