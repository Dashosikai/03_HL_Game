
from tkinter import S
from turtle import st


def statement_generator(statement, decorartion):

    sides = decorartion * 4
    
    statement = "{} {} {}".format(sides, statement, sides)
    

    
    print(statement)
    
    
    return ""


# Main routine goes here
statement_generator("Welcome to the Higher Lower Game", "*")
print()
statement_generator("For each game you will asked to... ", "")
statement_generator("- Enter a 'low' and 'high' number. the computer will randomly", "")
statement_generator("generate a", "")
statement_generator("'secret' number between your two chosen numbers. Tt will ues", "")
statement_generator("these nubers for all", "")
statement_generator("the rounds in a given game.", "")
statement_generator("- The computer will calculate how many guesses you aer allowed", "")
statement_generator("- enter the number if rounds you want to play", "")
statement_generator("- guess the secret number", "")
print()
statement_generator("Good Luck!", "")
print()