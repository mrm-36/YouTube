# Hangman Game

import random
# We import the random module to pick a random word

WORDLIST_FILENAME = "words.txt"
# I already have a file full of words that we will use to pick our
# secret word. You could use any file

def loadWords():
    """
    Returns a list of valid words.
    Words are strings of lowercase ENglish characters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordList = line.split()

    print("  ", len(wordList), "words loaded.")
    return wordList

def chooseWord(wordList):
    """
    wordList: list of words (strings)

    Returns a random word from wordList
    """
    return random.choice(wordList)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    
    Returns: boolean, True if all the letter of secretWord are
    in lettersGuessed
    and False otherwise
    """
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far

    Returns: string, comprised of letters and underscores that
    representes what letters in the secretWord have been guessed so far
    """
    st = str()
    for x in secretWord:
        if x in lettersGuessed: st += x
        else: st += '_ '
    return st

# alph is a list of all the lowercase English letters
alph = list("abcdefghijklmnopqrstuvwxyz")

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far

    Returns: string, comprised of letters that represents what 
    letters have not yet been guessed
    """
    st = str()
    for x in alph:
        if x not in lettersGuessed: st += x
    return st

def hangman(secretWord):
    """
    secretWord: string, the secret word to guess

    Starts up an interactive game of Hangman

    * At the start of the game, we will let the user know how
        many letters the secret word containes.

    * We will ask the user to supply one guess (i.e. letter)
        per round.

    * The user will receive feedback immediately after each guess
        about whether their guess appears in the secret word.

    * After each round, we will also display to the user the partially
        guessed word so far, as well as the letters that the user
        has not yet guessed
    """

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), 
            "letters long.")
    print('-'*20)

    guesses = 8
    # You can adjust the numbers of guesses the user have
    lettersGuessed = []
    # lettersGuessed is an empty list because the user didn't pick
    # any letter yet

    while guesses > 0 and not isWordGuessed(secretWord, lettersGuessed):
        # We will keep looping until either the user is out of guesses
        # or he found the secret word
        print("You have", guesses, "left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = str(input("Please guess a letter: "))

        st = str()
        if letter in lettersGuessed:
            st = "Opps! You've already guessed that letter: "
        elif letter not in alph:
            st = ("Invalid Input! Please choose a lower case "
                    + "character from the alphabet! ")
        elif letter in secretWord:
            st = "Good guess: "
        else:
            st = "Oops! That letter is not in my word: "
            guesses -= 1

        if len(letter) != 0: lettersGuessed.append(letter)

        print(st + getGuessedWord(secretWord, lettersGuessed))
        print('-'*20)

    # The loop ended. We will check if the user won or not
    if guesses > 0:
        print("Congratulations! You Won!")
    else:
        print("Sorry, you ran out of guesses. The word was " 
                + secretWord)


# We wrote the whole program
# That's it
# Now we just have to call the function
secretWord = chooseWord(wordlist)
hangman(secretWord)

# Let's Try it