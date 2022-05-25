import random
import string
import time


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, Invalid Input try again.\n")
    return response


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a alien " + monster + " "
                " is somewhere around here, and has been"
                "terrifying the nearby village.")
    print_pause("\nIn front of you is a house."
                "\nTo your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def fight(weapon, monster):
    if "plasma gun" in weapon:
        print_pause("As the alien " + monster + " moves to attack, "
                    "you point your new plasma gun at him.")
        print_pause("The gun shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("\nBut the alien " + monster + " "
                    "takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the alien " + monster + "."
                    "You are victorious!\n")
        play_again()
    else:
        print_pause("You do your best...but your dagger is no match "
                    "for the alien " + monster + ".")
        print_pause("You have been defeated!\n")
        play_again()


def cave(weapon, monster):
    if "plasma gun" in weapon:
        print_pause("You peer cautiously into the cave."
                    "\nYou've been here before, "
                    "and gotten all the good stuff.")
        print_pause("It's just an empty cave now." "You walk back out to "
                    "the field.\n ")
    else:
        print_pause("You peer cautiously into the cave."
                    "\nIt turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock."
                    "\nYou have found a big plasma gun!")
        print_pause("You discard your silly old dagger,"
                    "and take the plasma gun with you.")
        print_pause("You walk back out to the field.\n")
        weapon.append("plasma gun")
    choices_1(weapon, monster)


def field(weapon, monster):
    print_pause(
        "You run back into the field. Luckily, "
        "you don't seem to have been followed.\n")
    choices_1(weapon, monster)


def house(weapon, monster):
    print_pause("You approach the door of the house."
                "\nYou are about to knock when the door opens "
                "and out steps a alien " + monster + ".")
    print_pause("\nEep! This is the alien " + monster + " house!")
    print_pause("The alien " + monster + "  attacks you!\n")
    choices_2(weapon, monster)


# noinspection PyArgumentList
def choices_1(weapon, monster):
    response = valid_input("Enter 1.to knock on the door of the house.\n"
                           "Enter 2.to peer into the cave.\n",
                           "1", "2")
    if "1" in response:
        house(weapon, monster)
    elif "2" in response:
        cave(weapon, monster)


def choices_2(weapon, monster):
    response = valid_input("Would you like to: 1.fight or 2.run away?",
                           "1", "2")
    if "1" in response:
        fight(weapon, monster)
    elif "2" in response:
        field(weapon, monster)


def play_again():
    response = valid_input("GAME OVER\n"
                           "Would you like to play again?" "\n(y / n)\n",
                           "y", "n")
    if "y" in response:
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif "n" in response:
        print_pause("OK, goodbye!")
    exit()


def play_game():
    weapon = []
    monster = random.choice(["pirate", "dragon", "troll", "zombie"])
    intro(monster)
    choices_1(weapon, monster)
    choices_2(weapon, monster)
    play_again()


if __name__ == '__main__':
    play_game()
