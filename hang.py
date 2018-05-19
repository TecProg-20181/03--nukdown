import random
import string
import os

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True

def getGuessedWord():
     guessed = ''
     return guessed

def tryanotherletter(lettersGuessed, secretWord):
    _=os.system("clear")
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    print ('Oops! You have already guessed that letter: ', guessed)

def correctletter(lettersGuessed, secretWord):
    _=os.system("clear")
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    print ('Good Guess: ', guessed)

def incorrectletter(lettersGuessed, secretWord):
    _=os.system("clear")
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    print ('Oops! That letter is not in my word: ',  guessed)

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print ('You have ', guesses, 'guesses left.')

        available = string.ascii_lowercase
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            tryanotherletter(lettersGuessed, secretWord)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            correctletter(lettersGuessed, secretWord)
        else:
            guesses -=1
            lettersGuessed.append(letter)
            incorrectletter(lettersGuessed, secretWord)
        print ('------------')
    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ('Congratulations, you won!')
        else:
            _=os.system("clear")
            print ('Sorry, you ran out of guesses. The word was ', secretWord, '.')

def menu():
    print ('Welcome to the game, Hangman!')
    print ('Menu')
    print ("       1 - New game\n       2 - Exit")
    option = input()
    if option=="1":
        _=os.system("clear")
        secretWord = loadWords().lower()
        hangman(secretWord)
    elif option=="2":
        _=os.system("clear")
        print ('YOU\nARE\nA\nLOSER\nDO\nIT\nAGAIN')
        menu(0)
    else:
        menu(0)

_=os.system("clear")
menu()
