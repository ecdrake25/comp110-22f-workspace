"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730467957"

word_guess: str = input("Enter a 5-character word: ")
if int(len(word_guess)) != 5:
    print("Error: Word must contain 5 characters")
    exit()
letter_guess: str = input("Enter a single character: ")
if int(len(letter_guess)) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + letter_guess + " in " + word_guess)

if word_guess[0] == letter_guess:
    print(letter_guess + " found at index " + str(0))
    matching_count1: int = 1
else:
    matching_count1: int = 0
if word_guess[1] == letter_guess:
    print(letter_guess + " found at index " + str(1))
    matching_count2: int = 1
else:
    matching_count2: int = 0
if word_guess[2] == letter_guess:
    print(letter_guess + " found at index " + str(2))
    matching_count3: int = 1
else:
    matching_count3: int = 0
if word_guess[3] == letter_guess:
    print(letter_guess + " found at index " + str(3))
    matching_count4: int = 1
else:
    matching_count4: int = 0
if word_guess[4] == letter_guess:
    print(letter_guess + " found at index " + str(4))
    matching_count5: int = 1
else:
    matching_count5: int = 0

matching_count_all: str = str(matching_count1 + matching_count2 + matching_count3 + matching_count4 + matching_count5)

if matching_count_all == "1":
    print(matching_count_all + " instance of " + letter_guess + " found in " + word_guess)
if matching_count_all == "0":
    print("No instances of " + letter_guess + " found in " + word_guess) 
if matching_count_all >= "2":
    print(matching_count_all + " instances of " + letter_guess + " found in " + word_guess)

