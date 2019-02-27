import random
import string
word = ["Luke", "cat", "cool", "look!", "tools",
        "run", "code", "notes", "event", "girlfriends"]
letters_guess = []
letters_guess_right = []
guesses = 0
guesses_made = []
guesses_right = []
random_word = random.choice(word)
playing = True
hidden = list(random_word)

for i in range(len(hidden)):
        if hidden[i] in string.ascii_letters:
                hidden.pop(i)
                hidden.insert(i, "* ")

while guesses_made != 0 and playing:
        letter = input("What letter?")
        if letter in guesses_made:
                print("You already guessed this letter")
        elif letter not in random_word:
                print("wrong letter guess another one")
                guesses -= 1
                guesses_made.append(letter)
                print("" .join(hidden))
        else:
           print("Hey look you got it right good for you now guess another!")
           guesses_right.append(letter)
           guesses_made.append(letter)
           for i in range(len(random_word)):
                if random_word[i].lower() in guesses_right:
                    hidden.pop(i)
                    hidden.insert(i, random_word[i])
                    if list(random_word) == hidden:
                        playing = False
if not playing:
    print("Good job you get.................NOTHING!!!!")
else:
    print("Hey look you won good for you.")
print("de word was %s" % random_word)
