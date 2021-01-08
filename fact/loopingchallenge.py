#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for key in farms[0].values():
        print(key)

notAnimal = ["carrots", "celery"]
answer=""
user = input("Choose farm and enter:[NE],[W], [SE]: ").upper().strip()

if answer == "NE":
    for key in farms[0].values():
        if key not in notAnimal:
            print("chosen farm NE: ", key)
elif answer == "W":
    for key in farms[1].values():
        if key not in notAnimal:
             print("chosen farm W: ", key)
elif answer == "SE":
    for key in farms[-1].values():
        if key not in notAnimal:
             print("chosen farm SE: ", key)
else: 
    print("invalid input")

