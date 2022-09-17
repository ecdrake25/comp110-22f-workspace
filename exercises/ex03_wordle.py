"""EX03 Wordle."""

__author__ = "730467957"


def contains_char(searched_through: str, single_char: str) -> bool:
    """Searching a guessed word for a character."""
    index: int = 0
    assert len(single_char) == 1

    while index < len(searched_through):
        if searched_through[index] == single_char:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Adding emojis for the presence of letters."""
    assert len(guess) == len(secret)
    index = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while index < len(guess):
        if contains_char(secret, guess[index]):
            if guess[index] == secret[index]:
                emoji += GREEN_BOX
            else:
                emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Verify length of guess."""
    guess: str = input(f"Enter a { expected_length } character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't { expected_length } chars! Try again: ")
    
    return guess


def main() -> None:
    """The entrypoint of the program and main game."""
    secret: str = "codes"
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn { turn }/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if secret == guess:
            print(f"You won in { turn }/6 turns!")
            won = True
        else:
            turn += 1
        
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()