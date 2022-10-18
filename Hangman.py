import random

# Presentation of the game:

print('Welcome to Hangman!')
name = input('¿What\'s your name? ')
print('Hello, ' + name + '! Let\'s play!')

# List of possible words:

with open('Wordbank.csv') as file:
    wordlist = file.read().split(', ')

# We define a function that returns a list of the indices of a string in which a character occurs:

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

# A loop to re-execute the game when it finishes:

def play_loop():
    play_again = input('Do you want to play again?\n y = yes, n = no\n')
    while play_again.lower() not in ['y', 'yes', 'n', 'no']:
        play_again = input('Do you want to play again?\n y = yes, n = no\n')
    if play_again.lower() == 'y':
        main()
    else:
        print('Thanks for playing, ' + name + '!')

# Initializing the game:

def main():
    lives = 5
    word = random.choice(wordlist)
    length = len(word)
    display = '_' * length
    failed_attempts = []

    while lives != 0:

        guess = input('This is the word: ' + display + ' Enter your guess: ')
        guess = guess.strip()

        if not guess.isalpha() or len(guess) != 1:
            print('Invalid input. Please, try a letter.')

        elif guess in display or guess in failed_attempts:
            print('Please, try another letter.')

        elif guess in word:
            indices = findOccurrences(word, guess)
            for index in indices:
                display = display[:index] + guess + display[index + 1:]
               
        else:
            lives -= 1
            failed_attempts.append(guess)

            if lives > 0:

                if lives > 1:
                    print('Wrong answer. ' + str(lives) + ' lives remaining.')
                else:
                    print('Wrong answer. Last life remaining.')

                print('Attempts: ' + ', '.join(failed_attempts) + '.')

            else:
                print('Wrong answer. You are dead!')
                print('The word was "' + word + '".')
                
        if display == word:
            print('Congrats! You have guessed the word "' + word + '".')
            break
    
    play_loop()
        
main()