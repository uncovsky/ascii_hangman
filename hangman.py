import requests
import random
import time
import re


def printNext():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", end = "\n\n")


def hangmanGame(fileName = None):

    words = []
    usedLetters = []
    guessedLetters = 0
    incorrectGuesses = 0

    if fileName:
        f = open("file.txt", "r")
        for word in f:
            words.append(word)
    else:
        arguments = {"content-type" : "text/plain"}
        response = requests.get("https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co", arguments)
        words = response.text.splitlines()


    hangman = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

    print("welcome to hangman, guess the word\n")
    
    currentWord = random.choice(words)
    userAnswer = ['-'] * len(currentWord)
    wonGame = False

    while not wonGame:


        correctGuess = False

        print("Current progress: " + ''.join([c for c in userAnswer]))
        print(hangman[incorrectGuesses])
        print("used letters: " + ', '.join([c for c in usedLetters]))
        userLetter = input("Choose your letter: ")
        userLetter = userLetter.lower()
        print("")

        if not re.match("[a-z]", userLetter):
            print("please enter characters from a-z\n")
            time.sleep(1)
            printNext()
            continue

        if len(userLetter) > 1:
            print("please input a single character\n")
            time.sleep(1)
            printNext()
            continue

        if userLetter in usedLetters:
            print("you've already guessed that letter")
            time.sleep(1)
            printNext()
            continue


        usedLetters.append(userLetter)


        for x in range(len(currentWord)):
            if currentWord[x] == userLetter:
                userAnswer[x] = userLetter
                guessedLetters += 1
                correctGuess = True
        

        if (not correctGuess):
            print ("you have guessed incorrectly\n")

            incorrectGuesses += 1
            if incorrectGuesses == 6:
                break

            time.sleep(1)
            printNext()
            continue
        

        print ("you guessed right!\n")
        time.sleep(1)


        if guessedLetters == len(currentWord):
            wonGame = True

       
        printNext()



    if wonGame:
        print("you won")
        time.sleep(3)
    else:
        print (hangman[6])
        print("unfortunately you've lost the game, the word you were looking for was " + currentWord)
        time.sleep(5)
    
if __name__ == "__main__":
    hangmanGame()