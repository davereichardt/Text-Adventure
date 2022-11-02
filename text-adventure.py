import random

sword = False
torch = False
rem_inspect = "Options: backward / inspect"
dead_end_count = 0
shade_room_count = 0

def dead_end():
    directions = ["backward"]
    global sword
    global rem_inspect
    global dead_end_count
    if dead_end_count == 0:
        dead_end_count += 1
        print("You crossed the abyss to find... a dead end. You see a glint in the corner. What do you do?")
    else:
        rem_inspect = "Option: backward"
        print("Still a dead end...")
    user_input = ""
    while user_input not in directions:
        print(rem_inspect)
        user_input = input().lower()
        if user_input == "inspect":
            print("You inspect the glint further and find a sword and pick it up... May come in handy.")
            sword = True 
            rem_inspect = "Option: backward"
        elif user_input == "backward":
            abyss_path()
        else:
            print("Please enter a valid option.")

def shade_room():
    directions = ["fight", "run"]
    global sword
    global shade_room_count
    if shade_room_count == 0:
        shade_room_count += 1
        print("You enter a room and see a shade. Behind it, you see a path forward and another to the right.")
        print("You'll have to deal with the shade first. What do you do?")
    else:
        directions.append("forward", "right")
        print("There is no trace of the shade")
    user_input = ""
    while user_input not in directions:
        print("Options: fight/run")
        user_input = input().lower()
        rand_num = random.randrange(1,21)
        if user_input == "fight":
            if sword and rand_num >= 10:
                print(rand_num)
                print("You slay the shade with the sword you picked up earlier. Told you it would come in handy!")
                opening_scene()
            elif rand_num < 10:
                print(rand_num)
                print("You try to stab the shade, but it evades your attack and murders you. Game Over!")
                quit()
            else:
                print("You don't have a weapon to defend yourself and shade murks you. Game Over!")
                quit()
        elif user_input == "run" and rand_num >= 10:
            print("You successfully get away and run back the way you came!")
            opening_scene()
        elif user_input == "run" and rand_num < 10:
            print("You attempt to flee but the shade is faster and murks you. Game Over!")
            quit()
        else:
            print("Please enter a valid option.")

def abyss_path():
    directions = ["forward", "backward"]
    global dead_end_count
    print("You enter an empty chamber with a way forward. What do you do?")
    user_input = ""
    while user_input not in directions:
        print("Options: forward/backward")
        user_input = input().lower()
        if user_input == "forward":
            if dead_end_count == 0:
                print("Watch your step! You almost fell into an abyss! " \
                    "You see some wood lying conveniently nearby and fashion a rickety bridge out of it and make it safely across.")
                dead_end()
            else:
                print("You use your bridge to get across the abyss again.")
                dead_end()
        elif user_input == "backward":
            opening_scene()
        else:
            print("Please enter a valid option.")

def opening_scene():
    directions = ["left", "right", "forward"]
    global torch
    print("You enter a room with 4 paths, the one behind being the one you came from. You see a torch illuminating the room. What do you do?")
    user_input = ""
    while user_input not in directions:
        print("Options: left / right / forward / backward / take")
        user_input = input().lower()
        if user_input.lower() == "left":
            abyss_path()
        elif user_input == "right":
            print("This path appears to be completely caved in.")
        elif user_input == "forward":
            shade_room()
        elif user_input == "backward":
            print("You go back the way you came. Coward!")
            quit()
        elif user_input == "take":
            torch = True
            print("You take the torch.")
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    while True:
        print("Let us begin with your name: ")
        name = input()
        print("It's been 14 years of doing extensive research and searching high and low.")
        print("But...wait... you turn the book you were reading sideways...")
        print("You had thought you were sleep deprived, but the text on the page didn't appear to be legible. Now it is")
        print("This is it...you think you finally found the location of the fabled Magic Font. And now it is time to bring magic back to the world. " \
            "You hastily scribble some directions onto your parchment.")
        print("You travel to a dark forest trying your best to read your scribbled notes.")
        print("You've been traveling for days when the forest opens up a bit to reveal a small clearing.")
        print("There, in the middle, is a decrepit building almost blurred out of reality with how dark it is.")
        print("A yawning abyss of darkness to the entrance awaits.")
        print(f"Good luck, {name}.")
        opening_scene()