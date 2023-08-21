

# loading the JSON Data into a Python Dictionary

import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

# Returning the definition for a word
def translate(w):
    w = w.lower()
    # counting for non-existing words
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        # calculating similarity ratio between two words & making the program suggest a similar word
        yn = input("Did you mean %s instead? Enter Y if yes , or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Word does not exist please doublecheck it. "
        else:
            return "Entry not understood"
    else:
        return "The word does not exist. Please doublecheck it"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)




