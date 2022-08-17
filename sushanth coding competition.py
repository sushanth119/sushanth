import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinasour', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

print("Welcome to Password Picker")

while True:
    
    adjective = random.choice(adjectives)

    noun = random.choice(nouns)

    number = random.randrange(0, 100)

    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char

    print('Your new password is: %s' % password)

    response = input("would you like another password? Type yes or no: ")
    if response == 'no':
        break
