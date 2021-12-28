
import random

def pick_word_from_list():

    with open("wordlist.txt") as f:
        wordlist = f.read().splitlines()

    for i in wordlist[:]:
        if len(i) < 5 or len(i) > 7:
            wordlist.remove(i)
        

    random_num = random.randint(0, len(wordlist)-1)
    word = wordlist[random_num]


    return word

pick_word_from_list()