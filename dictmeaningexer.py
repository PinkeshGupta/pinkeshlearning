word = {"accidial": "dial someone's number on phone accidentally","agender": "people do not identify as male or female",
        "airball": "completely miss the basket, rim, and backboard with a shot",
        "automagically": "in a way that seems magical, especially by computer",
        "awesomesauce": "extremely good; excellent"}

# print(word.keys())
valent= input("Please select any word from list to check there meaning : \n" \
      "accidial\n agender\n airball\n automagically\n awesomesauce \n")

if valent in word:
    print(word[valent])
else:
    print("Invalid data")