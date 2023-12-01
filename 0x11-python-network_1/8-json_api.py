#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    playload = {'d': letter}
    req = requests.get('http://0.0.0.0:5000/search_user', playload)
    response = req.json()
    if response:
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    else:
        print("Not a valid JSON")
