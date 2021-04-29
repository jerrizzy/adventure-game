import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In the field in front of you are two passageways.")
    print_pause("Which way do you want to go?\n")


def obstacles():
    challenges = ["lord pirate", "dragon", "zeus"]
    creature = random.choice(challenges)
    return creature


def house(items):
    challenges = ["lord pirate", "dragon", "zeus"]
    boss = random.choice(challenges)
    if "lightning sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and")
        print_pause("out steps a " + (boss) + " . Yikes! "
                    "This the " + (boss) + "'s house")
        print_pause("The " + (boss) + " attacks you!")
        decision = input("Would you like to (1) fight or (2) run away?")
        if decision == "2":
            print_pause("You run back into the field. Luckily,"
                        "you don't seem to have been followed.")
            field(items)
        elif decision == "1":
            print_pause("As the " + (boss) + " moves to attack,"
                        "you unsheath your new sword.")
            print_pause("The lightning sword shines brightly in your hand as ")
            print_pause("you brace yourself for the attack. "
                        "But the " + (boss) + "")
            print_pause("takes one look at your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + (boss) + ". "
                        "You are victorious!")
            play_again(items)
        else:
            victorious_error(items)
    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens "
                    "and out steps a " + (boss) + " "
                    "Eep! This is the " + (boss) + "'s house! "
                    "The " + (boss) + " attacks you!")
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
        decision2 = input("Would you like to (1) fight or (2) run away?")
        if decision2 == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.\n")
            field(items)
        elif decision2 == "1":
            print_pause("You do your best..."
                        "but your dagger is no match for the " + (boss) + " "
                        "You have been defeated!")
            play_again(items)
        else:
            defeated_error(items)


def defeated_error(items):
    user_input = input("Please enter 1 or 2:\n")
    if user_input == "1":
        print_pause("You do your best..."
                    "but your dagger is no match for the troll."
                    "You have been defeated!")
        play_again(items)
    elif user_input == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        field(items)
    else:
        defeated_error(items)


def victorious_error(items):
    user_input = input("Please enter 1 or 2:\n")
    if user_input == "1":
        victorious_print()
        play_again(items)
    elif user_input == "2":
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        field(items)
    else:
        victorious_error(items)


def victorious_print():
    print_pause("As the creature moves to attack, "
                "you unsheath your new sword.")
    print_pause("The lightning sword shines brightly in your hand as ")
    print_pause("you brace yourself for the attack. "
                "But the creature ")
    print_pause("takes one look at your shiny new toy and runs away!")
    print_pause("You have rid the town of the creature. "
                "You are victorious!")


def cave(items):
    print_pause("in cave.")
    if "lightning sword" in items:
        print_pause("You got everything already, "
                    "you walk back out to the field.")
        field(items)
    else:
        print_pause("You have found the powerful lightning sword")
        items.append("lightning sword")
        print_pause("you walk back out to the field.")
        field(items)


def field(items):
    choices = input("Enter 1 to knock on the door of the house.\n"
                    "Enter 2 to peer into the cave.\n"
                    "Please enter 1 or 2\n")
    if choices == "1":
        house(items)
    elif choices == "2":
        cave(items)
    else:
        print_pause("Sorry, I don't understand")
        field(items)


def weapons():
    item = []
    return item


def play():
    items = weapons()
    intro()
    field(items)


def play_again(items):
    repeat = input("Would you like to play again? (y/n)").lower()
    if repeat == "n":
        print_pause("Game Over")
        sys.exit()
    elif repeat == "y":
        print_pause("Restarting the game...")
        play()
    else:
        play_again(items)


play()
