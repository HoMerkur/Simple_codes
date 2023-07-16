import json
from difflib import get_close_matches

word = input("Enter Word :")

file = open("data.json", "r", encoding="utf-8")

dictionary = json.loads(file.read())

if word in dictionary:
    print(dictionary[word])

else:
    list = get_close_matches(word, dictionary.keys(), cutoff=0.8)

    answer = input(f"Did you mean '{list[0]}' ? Y/N :")

    if answer == "Y" or answer == "y":
        print(dictionary[list[0]])

    else:
        print("orld couldn't be found!..")








