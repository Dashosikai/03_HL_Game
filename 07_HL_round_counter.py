def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please tytpe either <enter> " \
                      "or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

            return response
# Main routine gose here...

rounds_played = 0
choose_instruction = "Please choose Higher (H) or Lower (L)"

# Ask user for # of rounds, <enter> for infinite mode 
rounds = check_rounds()
 
end_game = "no"
while end_game == "no":

    # Start of game Loop

     # Round Heading 
     print()
     if rounds == "":
         heading = "Continuous Mode: " \
                    "Round {}".format(rounds_played + 1)
     else:
         heading = "Round {} of " \
                    "{}".format(rounds_played + 1, rounds)
     
     print(heading)
     choose = input("{} or 'xxx' to "
                    "end: ".format(choose_instruction))

     # End game if exit code is typed
     if choose == "xxx":
         break
            