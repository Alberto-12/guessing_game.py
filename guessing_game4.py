"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("""
    ------------------------------------
    Welcome to the Number Guessing Game
    ------------------------------------
    """)
    attempt = 1
    x = random.randint(1 ,10)
    y = None
    
    while y != x:
      try:
        y = int(input("Guess"))
      except ValueError:
        print("sorry wrong value! Try again!")
      else:  
        if y > x :
          print("lower")
          attempt += 1
          
        elif y < x :
          print("higher")
          attempt += 1
          

        else:
            if  y == x :
              print("it took {}.".format(attempt))
              y = input("would you like to play again? [y]es/[n]o? ")
              attempt += 1
            if y.lower == "y":
                print("hiscore {}".format(attempt))
                    
            elif  y.lower == "n":
                print("Game over")
                    
                    
              

# Kick off the program by calling the start_game function.
start_game()