import random
import time

keys = 0
key1 = False
key2 = False
key3 = False

def welcome():
    global key1
    global key2
    global key3
    print("Welcome to the game, in this game your objective is to the 3 golden keys to be able to escape the manor with your life")
    name = input("Enter your username - ")
    input("Do you want to begin? ")
    global keys
    keys = 0
    key1 = False
    key2 = False
    key3 = False
    mainHall()

def mainHall():
    print("You have entered the manor but something seems off, its eerily quite and the doors have slammed behind you and you must find a way to escape, but be warned there is a monster in the basement that is on the hunt. Find 3 keys and escape with your life")
    print("What would you like to do? ")
    print("(1) Living Room")
    print("(2) Downstairs Hallway")
    print("(3) Basement")
    print("(4) Stairway")
    print("(5) Front Door")
    choice = input().lower()
    if choice == "1":
        livingRoom()
    elif choice == "2":
        downstairsHallway()
    elif choice == "3":
        basement()
    elif choice == "4":
        stairway()
    elif choice == "5":
        frontDoor()
    else:
        mainHall()

def frontDoor():
    if keys == 3:
        print("Would you like to escape? ")
        choice = input().lower()
        if choice == "yes" or choice == "y":
            print("You have escaped, would you like to play again? ")
            choice = input().lower()
            if choice == "yes" or choice == "y":
                welcome()
            elif choice == "no" or choice == "n":
                while True:
                    break
            else:
                frontDoor()
        elif choice == "no" or choice == "n":
            mainHall()
    elif keys != 3:
        print("Return when you have collected all 3 keys")
        mainHall()

def livingRoom():
    global key1
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        if key1 == False:
            print("You have entered the Living Room, You search around and have found a Golden Key")
            print("Would you like to pick up the Golden Key? ")
            choice = input().lower()
            if choice == "yes" or choice == "y":
                global keys
                keys = keys + 1
                key1 = True
            elif choice == "no" or choice == "n":
                print("The Key was not collected you must move on")
            else:
                livingRoom()
            print("(1) Main Hall")
            print("(2) Downstairs Hallway")
            print("(3) Kitchen")
            choice = input().lower()
            if choice == "1":
                mainHall()
            elif choice == "2":
                downstairsHallway()
            elif choice == "3":
                kitchen()
        elif key1 == True:
            print("You have already searched this room, there is nothing else to be found")
            print("Where would you like to go now?")
            print("(1) Main Hall")
            print("(2) Downstairs Hallway")
            print("(3) Kitchen")
            choice = input().lower()
            if choice == "1":
                mainHall()
            elif choice == "2":
                downstairsHallway()
            elif choice == "3":
                kitchen()
            else:
                livingRoom()
            

def downstairsHallway():
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        print("You have entered the Downstairs Hallway, There is nothing to be found")
        print("Where would you like to go? ")
        print("(1) Living Room")
        print("(2) Main Hall")
        print("(3) Bathroom")
        print("(4) Kitchen")
        choice = input().lower()
        if choice == "1":
            livingRoom()
        elif choice == "2":
            mainHall()
        elif choice == "3":
            bathroom()
        elif choice == "4":
            kitchen()
        else:
            downstairsHallway()

def basement():
    print("Welcome to the Monster Lair, you died so go ahead and restart the game")
    print("Would you like to (1) restart or (2) end game? ")
    choice = input().lower()
    if choice == "1":
        welcome()
    elif choice == "2":
        print()
    else:
        basement()

def stairway():
    print("You have decided to go upstairs")
    print("Would you like to move to the Upstairs Hallway? ")
    choice = input().lower()
    if choice == "yes" or choice == "y":
        upstairsHallway()
    elif choice == "no" or choice == "n":
        mainHall()
    else:
        stairway()

def upstairsHallway():
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        print("You have entered the Upstairs Hallway, There is nothing to be found")
        print("Where to next? ")
        print("(1) Master Bedroom")
        print("(2) Guest Bedroom")
        print("(3) Attic")
        print("(4) Main Hall")
        choice = input().lower()
        if choice == "1":
            masterBedroom()
        elif choice == "2":
            guestBedroom()
        elif choice == "3":
            attic()
        elif choice == "4":
            mainHall()
        else:
            upstairsHallway()

def masterBedroom():
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        print("You have entered the Master Bedroom, but there is nothing to be found. You must continue on!")
        print("Time is of the essence, Where to now? ")
        print("(1) Attic")
        print("(2) Upstairs Hallway")
        choice = input().lower()
        if choice == "1":
            attic()
        elif choice == "2":
            upstairsHallway()
        else:
            masterBedroom()

def guestBedroom():
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        print("You have entered the Guest Bedroom, but there is nothing to be found, continue on!")
        print("Where to now? ")
        print("(1) Attic")
        print("(2) Upstairs Hallway")
        choice = input().lower()
        if choice == "1":
            attic()
        elif choice == "2":
            upstairsHallway()
        else:
            guestBedroom()

def attic():
    global key2
    if key2 == False:
        print("You have entered the Attic this is a safe space fromt the monster, You search around and have found a Golden Key in a draw")
        print("Would you like to pick up the Golden Key? ")
        choice = input().lower()
        if choice == "yes" or choice == "y":
            global keys
            keys = keys + 1
            key2 = True
        elif choice == "no" or choice == "n":
            print("The Key was not collected you must move on")
        else:
            attic()
        print("(1) Master Bedroom")
        print("(2) Upstairs Hallway")
        print("(3) Guest Bedroom")
        choice = input().lower()
        if choice == "1":
            masterBedroom()
        elif choice == "2":
            upstairsHallway()
        elif choice == "3":
            guestBedroom()
    elif key2 == True:
        print("You have already searched this room, there is nothing else to be found")
        print("Where would you like to go now?")
        print("(1) Master Bedroom")
        print("(2) Upstairs Hallway")
        print("(3) Guest Bedroom")
        choice = input().lower()
        if choice == "1":
            masterBedroom()
        elif choice == "2":
            upstairsHallway()
        elif choice == "3":
            guestBedroom()

def kitchen():
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if monsterchance <= 15:
        print("You have been captured and taken to the basement, you have been killed")
    elif monsterchance > 15:
        print("You have entered the Kitchen, there is nothing to be found")
        print("Continue on")
        print("(1) Living Room")
        print("(2) Downstairs Hallway")
        choice = input().lower()
        if choice == "1":
            livingRoom()
        elif choice == "2":
            downstairsHallway()
        else:
            kitchen()

def bathroom():
    global key3
    monsterchance = random.randint(0,100)
    print(monsterchance)
    time.sleep(1)
    if key3 == False:
        if monsterchance <= 15:
            print("You have been captured and taken to the basement, you have been killed")
        elif monsterchance > 15:
            print("You have entered the Bathroom, You search around and have found a Golden Key in a draw")
            print("Would you like to pick up the Golden Key? ")
            choice = input().lower()
            if choice == "yes" or choice == "y":
                global keys
                keys = keys + 1
                key3 = True
            elif choice == "no" or choice == "n":
                print("The Key was not collected you must move on, you move back to the Downstairs Hallway")
                downstairsHallway()
            else:
                bathroom()
            print("(1) Downstairs Hallway")
            choice = input().lower()
            if choice == "1":
                downstairsHallway()
    elif key3 == True:
        print("You have already searched this room, there is nothing else to be found")
        print("You proceed to the Downstairs Hallway")
        downstairsHallway()
        

welcome()
