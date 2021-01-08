#!/usr/bin/env python3

starred_rows=5
for num in range(starred_rows,0, -1):

    print("*", end="")
    for column in range(0,num +1):
         print(column, "*")
         print("\r")
