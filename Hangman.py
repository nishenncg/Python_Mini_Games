#importing libraries
import random
import time

#functions with arguments
print('Hangman')
name = input("Name: ")
print('Hi ' + name + "..! WELCOME!")
time.sleep(1)
print("Let's play...!")
time.sleep(1)


def main():
    global count
    global display
    global word
    global Existing_guess
    global length
    global play_game
    Guess = ["affix","avenue","awkward","beekeeper","boggle","cobweb","cycle","disavow","duplex","equip","exodus","funny","galaxy","gossip","icebox","injury","ivory","jackpot","jelly","jockey","joking","joyful","jumbo","lengths","lucky","luxury","nightclub","pneumonia","puppy","scratch","staff","stretch"]
    word = random.choice(Guess)
    length = len(word)
    count = 0
    display = '_' * length
    Existing_guess = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Play again? y = yes, n = no \n")
    while play_game not in ["y", "n"]:
        play_game = input("Invalid!!! Play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for Playing!")
        exit()

def hangman():
    global count
    global display
    global word
    global Existing_guess
    global play_game
    limit = 8
    guess = input("Word: " + display + " Your Guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try again..!\n")
        hangman()
    elif guess in word:
        Existing_guess.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in Existing_guess:
        print("Try another letter.\n")
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 6:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
        elif count == 7:
            time.sleep(1)
            print("   _____   \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "__|__\n")
        elif count == 8:
            time.sleep(1)
            print("   _____   \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", Existing_guess, word)
            play_loop()

    if word == '_' * length:
        print("Congratulations! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()

