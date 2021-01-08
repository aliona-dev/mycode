#!/usr/bin/env python3
"""Author: Aliona | Program is a calculator that calculates two  numbers chosen by the user """

print("Welcome to Calculations Helper")
#list of valid operators
operators = ["-", "+", "*", "/"]
#foolproof operator input from the user
#promp user until a valid operator is chosen
while True:
    operator=input("Please choose an operator to start your calculation: [+,-,*,/] -> ").strip()
    try:
        if operator in operators: 
            print(f"You chose [{operator}] operator")
            break
        else:
            print("not an operator")
    except:
        print("Not a valid operator")
#foolproof user input for the two numbers
#promp user until a valid 1st number and 2nd number is chosen
while True:
    try:
        num1 = float(input("Please enter the 1st number for your calculation: ").strip())
        break
    except:
        print("not a number")
while True:
    try:
        num2 = float(input("Please enter 2nd number for your calculation: ").strip())
        break
    except:
        print("not a number")
       
#function for corresponding calculations for each operator and chosen two numbers
def calc():
    if operator == operators[1]:
        print(f"Result: {num1} + {num2} =", num1 + num2)
        print("Thank you for using Calculations Helper!")
    elif operator == operators[0]:
        print(f"Result: {num1} - {num2} =", num1 - num2)
        print("Thank you for using Calculations Helper!")
    elif operator == operators[2]:
        print(f"Result: {num1} * {num2} =", num1 * num2)
        print("Thank you for using Calculations Helper!")
    elif operator == operators[3]:
        print(f"Result: {num1} + {num2} =", num1 / num2)
        print("Thank you for using Calculations Helper!")        
    else:
        print("error in calculating")
#call the function    
calc()
