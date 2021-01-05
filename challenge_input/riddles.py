#!/usr/bin/env python3

round = 0
riddle = " "
while round < 3 and riddle !="match":
    round += 1
    riddle = input("You walk into a room that contains a [match], a [kerosene lamp], a [candle] and a [fireplace]. What would you light first?").lower().strip()

    if riddle == "match":
        print(riddle+": You so smart, that's correct!")
    elif round == 3:
        print("Dissapointing, you did not guess right.The answer was a match")
    elif riddle == "candle" or riddle == "kerosene lamp" or riddle == "fireplace":
        print(riddle+": Nah not right, think harder and try again!")
    else:
        print(riddle+": Silly, you that is not one of the choices, try again")
