"""EX02 - One Shot Wordle."""

__author__ = "730467957"

secret: str = "python"
guess: str = input("What is your " + str(len(secret)) + "-letter guess? ")
index: int = 0
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
exists_elsewhere: bool = False
alternate_indices: int = 0

while len(guess) != len(secret):
    guess = input("That was not " + str(len(secret)) +  " letters! Try again: ")

while index < len(secret):
    if str(guess[index]) == str(secret[index]):
            emoji = emoji + GREEN_BOX
    else:
        while exists_elsewhere != True and alternate_indices < len(secret):
            if secret[alternate_indices] == guess[index]:
                exists_elsewhere = True
            alternate_indices = alternate_indices + 1
        if exists_elsewhere:
            emoji = emoji + YELLOW_BOX
        else:
                emoji =  emoji + WHITE_BOX

    index = index + 1
    exists_elsewhere = False
    alternate_indices = 0
print(emoji)
    

if len(guess) == len(secret) and guess == secret:
        print("Woo! You got it!")
if len(guess) == len(secret) and guess != secret:
        print("Not quite. Play again soon!")