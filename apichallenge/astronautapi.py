#!/usr/bin/env python3
"""API Challenge | Author: Aliona"""
import requests
    # create req, which is our request object
req = requests.get("http://api.open-notify.org/astros.json")
astroInfo = req.json()
print("People in space: ", len(astroInfo["people"]))
for plp in astroInfo["people"]:
    print(f"{plp['name']}")
    print(f"on the {plp['craft']} craft") 
