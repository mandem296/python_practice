secret_word = "Bobo"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess secret word: ")
        #guess=input("Guess secret word: ").lower() used lower() so as to convert it to lowercase since python is case sensitive...in scenarios where the guessed word has both then lower() can be removed
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!!")
else:
    print("Yeey you have gotten it!!")