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
    count1: int = 1
else:
    count1 = 0
if word_guess[1] == letter_guess:
    print(letter_guess + " found at index " + str(1))
    count2: int = 1
else:
    count2 = 0
if word_guess[2] == letter_guess:
    print(letter_guess + " found at index " + str(2))
    count3: int = 1
else:
    count3 = 0
if word_guess[3] == letter_guess:
    print(letter_guess + " found at index " + str(3))
    count4: int = 1
else:
    count4 = 0
if word_guess[4] == letter_guess:
    print(letter_guess + " found at index " + str(4))
    count5: int = 1
else:
    count5 = 0

matching_count: str = str(count1 + count2 + count3 + count4 + count5)

if matching_count == "1":
    print(matching_count + " instance of " + letter_guess + " found in " + word_guess)
if matching_count == "0":
    print("No instances of " + letter_guess + " found in " + word_guess) 
if matching_count >= "2":
    print(matching_count + " instances of " + letter_guess + " found in " + word_guess)