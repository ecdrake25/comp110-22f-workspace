"""Choose Your Own Adventure. Buzzfeed Quiz."""

__author__ = "730467957"
 
player: str = ""
points: int = 0
from random import choice

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
    global player
    player = input("Welcome! Today you will be taking care of a pet and recieving a score of your performance. What is your name? ")

def dog(x: int) -> int:
    print(DOG)
    global points
    global player
    walk = input("Would you like to take your dog for a walk? ")
    if walk == "yes":
        points += 1
        print(WALK)

    water = input(f"{player}, would you like to freshen your dog's water? ")
    if water == "yes":
        points += 1
        print(WATER)

    play = input("Would you like to play fetch? ")
    if play == "yes":
        points += 1
        print(PLAY)

    feed = input("Would you like to feed your dog? ")
    if feed == "yes":
        points += 1
        print(BONE)

    playdate = input("Would you like to go to the park and have your dog meet other dogs? ")
    if playdate == "yes":
        points += 1
        print(DOG)

    return points


def lizard() -> None:
    global points
    global player
    print(LIZARD)
    tank = input(f"{player}, would you like to add some plants and rocks to your lizard's habitat? ")
    if tank == "yes":
        points += 1
        print(PLANT)
    
    lamp = input("Do you have a lamp to maintain the proper habitat temperature? ")
    if lamp == "yes":
        points += 1
        print(BULB)

    food = input("Have you fed your lizard? ")
    if food == "yes":
        points += 1
        print(CRICKET)

    clean = input("Have you cleaned its cage? ")
    if clean == "yes":
        points += 1
        print(CAGE)

    water = input("Have you refilled your pet's water? ")
    if water == "yes":
        points += 1
        print(WATER)

def random_pet() -> None:
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
        
    play = input(f"{player}, would you like to play with your {chosen}? ")
    if play == "yes":
        points += 1
        print(PLAY)

    feed = input(f"Would you like to feed your {chosen}? ")
    if feed == "yes":
        points += 1
        print(PLATE)

    water = input(f"Would you like to freshen your {chosen}'s water? ")
    if water == "yes":
        points += 1
        print(WATER)

    groom = input(f"Would you like to groom your {chosen}? ")
    if groom == "yes":
        points += 1
        print(SMILE)

    pet = input(f"Would you like to pet your {chosen}? ")
    if groom == "yes":
        points += 1
        print(HAND)


def counter(score: int) -> int:
    global points
    global player
    print(f"Congratulations on taking care of your pet, {player}. You recieved { points } points")

    if points <= points/2:
        print("Try spending more time with your pet!")
    else:
        print("You are a great pet owner!")
    
    return points
    

def main() -> None:
    playing: bool = True
    greet()

    while playing:
        response = input("Would you like to look after a dog (enter 'D'), look after a lizard (enter 'L'), look after a random pet (enter 'R'), or end the experience (enter 'E')? ")

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