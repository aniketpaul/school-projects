import random
part_1 = ["I saw a", "I met a", "I found a"]
part_2 = ["mad", "tearful", "psycho", "undead"]
part_3 = ["fireman", "chicken", "buisness man", "rabbi"]
part_4 = ["eat brocolli", "have a big nose", "make the pie well", "look like mushrooms"]
part_5 = ["will get cancer", "have a criminal record", "commit suicide", "over eat fish"]
while True:
    raw_input("press enter for a random David Cameron quote")
    print random.choice(part_1) , \
        random.choice(part_2) , \
        random.choice(part_3) , \
        "who told me people that" ,\
        random.choice(part_4), \
        random.choice(part_5)


