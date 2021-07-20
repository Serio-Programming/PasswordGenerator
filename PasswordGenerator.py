# Password Generator
# This program generates a password by combining randomly selected numbers and words
# Circa May 2021
# Tyler Serio
# Python > 3.7

import random

def generate_number():
    number = random.randint(0, 1000)
    return number

def generate_adjective():
    print("Gathering an adjective...")
    adjective_list = []
    file = open("adjectives.txt", "r")
    counter = -1
    for line in file:
        adjective_list.append(line.replace("\n", ""))
        counter += 1
    adjective = adjective_list[random.randint(0, counter)]
    file.close()
    return adjective

def generate_noun():
    print("Searching for a noun...")
    noun_list = []
    file = open("nouns.txt", "r")
    counter = -1
    for line in file:
        noun_list.append(line.replace("\n", ""))
        counter += 1
    noun = noun_list[random.randint(0, counter)]
    file.close()
    return noun

def generate_verb():
    print("Looking for a verb...")
    verb_list = []
    file = open("verbs.txt", "r")
    counter = -1
    for line in file:
        verb_list.append(line.replace("\n", ""))
        counter += 1
    verb = verb_list[random.randint(0, counter)]
    file.close()
    return verb

def generate_verb2():
    print("Looking for a verb...")
    verb_list = []
    file = open("verbs2.txt", "r")
    counter = -1
    for line in file:
        verb_list.append(line.replace("\n", ""))
        counter += 1
    verb = verb_list[random.randint(0, counter)]
    file.close()
    return verb

def generate_special_character():
    print("Selecting a special character...")
    special_character_list = ["?", "!", ".", "+"]
    special_character = special_character_list[random.randint(0, 3)]
    return special_character

def generate_password():
    selection = "y"
    while selection == "y":
        generator = random.randint(0, 1)
        if generator == 0:
            number = generate_number()
            adjective = generate_adjective()
            noun = generate_noun()
            verb = generate_verb()
            special_character = generate_special_character()
            print("Done!")
            print("Your new password is:\n" + "\n" + str(number) + adjective + noun + verb + special_character)
            print("")

        if generator == 1:
           number = generate_number()
           noun1 = generate_noun()
           verb = generate_verb2()
           noun2 = generate_noun()
           special_character = generate_special_character()
           print("Done!")
           print("Your new password is:\n" + "\n" + str(number) + noun1 + verb + noun2 + special_character)
           print("")

        print("Would you like to generate another password?")
        print('Please enter either "y" for yes, or "n" for no')
        selecting = 1
        while selecting == 1:
            selection = input("Selection: ")
            if selection == "n":
                selecting = 0
                break
            if selection == "y":
                selecting = 0
                print("")
            if selection != "y" and selection != "n":
                print('Please choose either "y" or "n"')
                selecting = 1

generate_password()
