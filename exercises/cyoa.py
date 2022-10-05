"""Choose Your Own Adventure. Taking care of a pet."""

__author__ = "730467957"

from random import choice
 
player: str = ""
points: int = 0

DOG: str = "\U0001F415"
LIZARD: str = "\U0001F98E"
WALK: str = "\U0001F6B6"
WATER: str = "\U0001F4A6"
PLAY: str = "\U0001F600"
BONE: str = "\U0001F357"
PLANT: str = "\U0001F331"
BULB: str = "\U0001F4A1"
CRICKET: str = "\U0001F997"
CAGE: str = "\U0001F9FC"
CAT: str = "\U0001F408"
BIRD: str = "\U0001F426"
TURTLE: str = "\U0001F422"
HORSE: str = "\U0001f40E"
FISH: str = "\U0001F41F"
PLATE: str = "\U0001F37D"
SMILE: str = "\U0001F604"
HAND: str = "\U000FEF0F"


def greet() -> None:
    """Greet the player."""
    global player
    print("Welcome! Today you will be taking care of a pet and recieving a score of your performance")
    player = input("What is your name? ")


def dog(x: int) -> int:
    """Take care of a dog."""
    print(DOG)
    global points
    global player
    walk: str = input("Would you like to take your dog for a walk? ")
    if walk == "yes":
        points += 1
        print(WALK)

    water: str = input(f"{player}, would you like to freshen your dog's water? ")
    if water == "yes":
        points += 1
        print(WATER)

    play: str = input("Would you like to play fetch? ")
    if play == "yes":
        points += 1
        print(PLAY)

    feed: str = input("Would you like to feed your dog? ")
    if feed == "yes":
        points += 1
        print(BONE)

    playdate: str = input("Would you like to go to the park and have your dog meet other dogs? ")
    if playdate == "yes":
        points += 1
        print(DOG)

    return points


def lizard() -> None:
    """Take care of a lizard."""
    global points
    global player
    print(LIZARD)
    tank: str = input(f"{player}, would you like to add some plants and rocks to your lizard's habitat? ")
    if tank == "yes":
        points += 1
        print(PLANT)
    
    lamp: str = input("Do you have a lamp to maintain the proper habitat temperature? ")
    if lamp == "yes":
        points += 1
        print(BULB)

    food: str = input("Have you fed your lizard? ")
    if food == "yes":
        points += 1
        print(CRICKET)

    clean: str = input("Have you cleaned its cage? ")
    if clean == "yes":
        points += 1
        print(CAGE)

    water: str = input("Have you refilled your pet's water? ")
    if water == "yes":
        points += 1
        print(WATER)


def random_pet() -> None:
    """Take care of a random pet."""
    pet: list[str] = ["cat", "bird", "turtle", "horse", "fish"]
    chosen: str = choice(pet)
    global points
    global player
    
    if chosen == "cat":
        print(CAT)
    if chosen == "bird":
        print(BIRD)
    if chosen == "turtle":
        print(TURTLE)
    if chosen == "horse":
        print(HORSE)
    if chosen == "fish":
        print(FISH)
        
    play: str = input(f"{player}, would you like to play with your {chosen}? ")
    if play == "yes":
        points += 1
        print(PLAY)

    feed: str = input(f"Would you like to feed your {chosen}? ")
    if feed == "yes":
        points += 1
        print(PLATE)

    water: str = input(f"Would you like to freshen your {chosen}'s water? ")
    if water == "yes":
        points += 1
        print(WATER)

    groom: str = input(f"Would you like to groom your {chosen}? ")
    if groom == "yes":
        points += 1
        print(SMILE)

    pet: str = input(f"Would you like to pet your {chosen}? ")
    if groom == "yes":
        points += 1
        print(HAND)


def counter(score: int) -> int:
    """Keep track of points."""
    global points
    global player
    print(f"Congratulations on taking care of your pet, {player}. You recieved { points } points")

    if points >= 3:
        print(f"You are a great pet owner, {player}")
    
    return points
    

def main() -> None:
    """Implementation of game."""
    global points
    points = 0
    playing: bool = True
    greet()

    while playing:
        response: str = input("Would you like to look after a dog (enter 'D'), look after a lizard (enter 'L'), look after a random pet (enter 'R'), or end the experience (enter 'E')? ")

        while response not in ["E", "D", "L", "R"]:
            response = input("Please enter a valid input (E, D, L, or R): ")

        if response == "E":
            playing = False

        if response == "D":
            dog(points)

        if response == "L":
            lizard()

        if response == "R":
            random_pet()
        
        if playing:
            counter(points)
    print(f"Goodbye, {player}! Thanks for playing! You accumulated { points } adventure points.")


if __name__ == "__main__":
    main()