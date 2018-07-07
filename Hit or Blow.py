import random

# Rules
print("""
HIT or BLOW game!
You have 10 guesses to enter the correct 4 digit number.
At the end of each guess you will receive HITS or BLOWS.
HIT: Correct digit and in the correct position.
BLOW: Correct digit but not in the correct position.
You need to guess the correct 4 digit number within 10
tries or it is game over.
NOTE: Each digit in the code is unique, there will never be
more than one of the same digit. i.e '2255' '4555'
""")


def code_creator():
    """
    Creates a unique random 4 digit code.
    """
    code = ''.join(random.sample("0123456789", 4))

    return code


def main():
    """
    Runs the entire game.
    """
    win = False
    guess_count = 1
    code = code_creator()

    while guess_count != 11:

        # Input validation
        while True:
            user_guess = input("\nPlease enter a 4 digit number.")
            
            if len(user_guess) != 4 or not user_guess.isdigit():
                print("Make sure to enter a 4 digit number.")
            
            elif len(set(user_guess)) != len(user_guess):
                print("You cannot enter the same number more than once.")
                
            else:
                break
        
        hits = 0
        blows = 0

        # Determines hits and blows
        for i in range(4):
                if user_guess[i] in code:
                    if user_guess[i] == code[i]:
                        hits += 1  
                    else:
                        blows += 1

        # Prints current status
        print("Guess:", guess_count)
        print("Hits:", hits)
        print("Blows:", blows)

        # Winning the game stuff
        if hits == 4:
            win = True
            print("\nCongratulations you guessed the correct code: {}".format(code))
            break

        guess_count += 1

    # Losing the game stuff
    if win == False:
        print("\nUnlucky! You didn't manage to find the code: {}\n".format(code))
    
    retry = ""
    while retry not in ["y", "n"]:
        retry = input("Would you like to play again? (Y/N)").lower()
        
    return retry

# Starts game and handles replay
if __name__ == "__main__":
    loop = main()

    while loop == "y":
        loop = main()

    else:
        exit
        
