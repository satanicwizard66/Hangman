# bugs currently...
# lose a live when accidently guessing 2 letters or blank

# gameWon While loop might need some tuning
# end of game options need to be added e.g. replay & quit
# classes should be added for organization
# possible pygame version?

import images, word, os, bigletters

os.system("title Hangman CLI")

win = bigletters.win_text()
title = bigletters.title_text()


def check_letter(letter, word):
    for i in range(0, len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False


# Displays current status of letters
def status():
    hangman = images.show_stages(lives)
    print(hangman)
    print(f"\t{reveal}")
    print("\n")


# Main Game Function
def hangman():
    global word
    global lives
    global reveal
    global guess
    global win
    global title

    word = word.pick_word_from_list().lower()
    reveal = list(len(word) * '_')

    lives = 6
    gameWon = False

    print(title)
    while gameWon == False and lives > -1:
        status()
        guess = input("\tGuess a letter or an entire word: ").lower()

        if guess == word:
            gameWon = True
            break
        if lives < 0:
            break
        if len(guess) == 1 and guess in word:
            gameWon = check_letter(guess, word)
        else:
            print(f"\n\n\tWrong, {lives} Lives remaining, try again...\n")
            lives -= 1
    

    if gameWon:
        print(win)
        print("\n\t!!!WELL DONE YOU ARE A GODDAMN WINNER!!!\n\tYou saved the hanging man!! He is thankful  ;)")
        print(f"\n\tThe word was: {word}")
    else:
        print("\n\tYOU FAILED, the word was:", word)

    


if __name__ == '__main__':
    hangman()
    input('\tPress ENTER to continue... ')
