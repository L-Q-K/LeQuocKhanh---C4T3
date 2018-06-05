import random

maps = [["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]

door_pos = [random.randint(0, 3),random.randint(0, 3)]
key_pos = [random.randint(0, 3),random.randint(0, 3)]
while key_pos == door_pos:
    key_pos = [random.randint(0, 3),random.randint(0, 3)]
player_pos = [random.randint(0, 3),random.randint(0, 3)]
while player_pos == door_pos or player_pos == key_pos:
    player_pos = [random.randint(0, 3),random.randint(0, 3)]

maps [door_pos[0]][door_pos[1]] = "E"
maps [key_pos[0]][key_pos[1]] = "K"
maps [player_pos[0]][player_pos[1]] = "P"

inventory = False

def maps_change():
    maps [door_pos[0]][door_pos[1]] = "E"
    maps [key_pos[0]][key_pos[1]] = "K"
    if inventory == True:
        maps [key_pos[0]][key_pos[1]] = "_"
    maps [player_pos[0]][player_pos[1]] = "P"
def inventory(inventory):
    if player_pos == key_pos:
        inventory = True
    if inventory == True:
        return True
    else:
        return False
def print_maps():          
    for i in range(4):
        print (maps[i])

print_maps()

while True:
    action = input ("Your move? ")
    if action == "W":
        player_pos[0] = player_pos[0]-1
        if player_pos == key_pos:
            print("Oh It's a keyyyy")
            inventory = True
            maps [player_pos[0] + 1][player_pos[1]] = "_"
            maps_change()
            print_maps()
            
        elif player_pos == door_pos:
            if inventory == True:
                print ("Bing bing bing!!! You win")
                maps [player_pos[0] + 1][player_pos[1]] = "_"
                maps_change()
                print_maps()
                input("Enter to quit game")
                break
            else:
                print ("Pick up the key first")
                player_pos[0] = player_pos[0] + 1
                maps_change()
                print_maps()
        else:
            maps [player_pos[0] + 1][player_pos[1]] = "_"
            maps_change()
            print_maps()
            
    elif action == "S":
        player_pos[0] = player_pos[0] + 1
        if player_pos == key_pos:
            print("Oh It's a keyyyy")
            inventory = True
            maps [player_pos[0] - 1][player_pos[1]] = "_"
            maps_change()
            print_maps()
            
        elif player_pos == door_pos:
            if  inventory == True:
                print ("Bing bing bing!!! You win")
                maps [player_pos[0] - 1][player_pos[1]] = "_"
                maps_change()
                print_maps()
                input("Enter to quit game")
                break
            else:
                print ("Pick up the key first")
                player_pos[0] = player_pos[0] - 1
                maps_change()
                print_maps()
        else:
            maps [player_pos[0] - 1][player_pos[1]] = "_"
            maps_change()
            print_maps()
            
    elif action == "A":
        player_pos[1] = player_pos[1] - 1
        if player_pos == key_pos:
            print("Oh It's a keyyyy")
            inventory = True
            maps [player_pos[0]][player_pos[1] + 1] = "_"
            maps_change()
            print_maps()
            
        elif player_pos == door_pos:
            if inventory == True:
                print("Bing bing bing!!! You win")
                maps [player_pos[0]][player_pos[1] + 1] = "_"
                maps_change()
                print_maps()
                input("Enter to quit game")
                break
            else:
                print ("Pick up the key first")
                player_pos[1] = player_pos[1] + 1
                maps_change()
                print_maps()
        else:
            maps [player_pos[0]][player_pos[1] + 1] = "_"
            maps_change()
            print_maps()
            
    elif action == "D":
        player_pos[1] = player_pos[1] + 1
        if player_pos == key_pos:
            print("Oh It's a keyyyy")
            inventory = True
            maps [player_pos[0]][player_pos[1] - 1] = "_"
            maps_change()
            print_maps()
            
        elif player_pos == door_pos:
            if inventory == True:
                print("Bing bing bing!!! You win")
                maps [player_pos[0]][player_pos[1] - 1] = "_"
                maps_change()
                print_maps()
                input("Enter to quit game")
                break
            else:
                print ("Pick up the key first")
                player_pos[1] = player_pos[1] - 1
                maps_change()
                print_maps()
        else:
            maps[player_pos[0]][player_pos[1] - 1] = "_"
            maps_change()
            print_maps()

    
