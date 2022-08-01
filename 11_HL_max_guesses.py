2# HL component 11 - Maximum Guesses Calculator 

import math 

for item in range(0,4):

    low = int(input("Low: "))   # ues int check in due coures
    high = int(input("High: ")) # ues int check in due coures 

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum # of guesses using 
    max_upper = math.ceil(max_raw)  # rounds up (ceil --> ceilir)
    max_guesses = max_upper + 1
    print("Max Guesses; {}".format(max_guesses))

    print()
