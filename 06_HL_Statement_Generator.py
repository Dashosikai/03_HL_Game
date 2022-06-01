
from turtle import st


def statement_generator(statement, decorartion):

    sides = decorartion * 3
    
    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decorartion * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    
    return ""


# Main routine goes here
statement_generator("Welcome to the Higher Lower Game", "*")
print()
statement_generator()