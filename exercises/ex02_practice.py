"""EX02 Practice for Understanding."""

secret: str = "python"
guess: str = input(f"What is your { str(len(secret)) }-letter guess? " )

while len(guess) != len(secret):
    guess = input(f"That was not { str(len(secret)) } letters! Try again: ")

index: int = 0
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
exists_elsewhere: bool = False
alternate_indices: int = 0

while index < len(secret):
    if guess[index] == secret[index]:
        emoji = emoji + GREEN_BOX
    else:
        while exists_elsewhere != True and alternate_indices < len(secret):
            if secret[alternate_indices] == guess[index]:
                exists_elsewhere = True
            alternate_indices = alternate_indices + 1
        if exists_elsewhere == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
    index = index + 1
    alternate_indices = 0
    exists_elsewhere = False
print(emoji)


if guess == secret:
    print("Woo! You got it!")
else:
    if len(guess) == len(secret) and guess != secret:
        print("Not quite. Play again soon!")