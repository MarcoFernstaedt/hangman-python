import random

# list of words
word_list = ["aardvark", "baboon", "camel"]

# randomly select word
chosen_word = random.choice(word_list)

# take user input and convert to lower case
guess = input('Guess a letter: ').lower()

# check if guess is in word
for letter in chosen_word:
    if guess == letter:
        print('Right')
    else:
        print('Wrong')
