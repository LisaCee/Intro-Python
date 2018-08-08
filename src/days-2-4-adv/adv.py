from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("--Outside Cave Entrance--", "North of you, the cave mount beckons", [Item('Key', "This key opens something")]),
    'foyer':    Room("--Foyer--", """Dim light filters in from the south. Dusty passages run north and east.""", [Item('Lantern', 'Use this lantern to light the way ahead')]),
    'overlook': Room("--Grand Overlook--", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Sword', 'It is dangerous to go alone. Take this sword')]),
    'narrow':   Room("--Narrow Passage--", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [Item('Coins', 'These coins look like they are worth a lot of money')]),
    'treasure': Room("$$--Treasure Chamber--$$", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Potion', 'An unknown potion. Use at your own risk')]),
    'library': Room("--Library--", """Shhhhhhh.""", [Item('Book', 'Relax and look at this book')]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['overlook'].w_to = room['library']
room['library'].e_to = room['overlook']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Hello, player.  What is your name?  ')
player = Player( name, room['outside'], [ ])

print(f"\n***Welcome, {player.name}! Let's begin our adventure: ***\n")
print(player.room, "\n", player.room.description)
# Write a loop that:
while dir != "q" and dir != "quit":
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input *

    dir = input("------------------\nPlease enter a direction... n, s, e, w OR q to quit the game. Press m for more options. \n---------\n").lower()
    parsed_dir = dir.lower().split()

    if len(parsed_dir) is 1:
        # directional inputs
        if dir == "n" or dir == "e" or dir == "w" or dir == "s":
            if hasattr(player.room, dir + '_to'):
                player.room = getattr(player.room, dir + '_to')
                print(player.room, "\n", player.room.description, "\n") 
                print("Items in this room:")     
                if len(player.room.items) == 0:
                    print("none")   
                else:
                    for i in player.room.items:
                        print("\t" + i.name + ": " + i.description)
            else:
                print("xx--That direction is a dead end.--xx")
        elif dir == "i" or dir == "inventory":
            print("Inventory:")
            for item in player.inventory:
                print("\t" + item.name)
        elif dir == "m" or dir == "menu":
            print("Move North | n \nMove South | s \nMove East  | e \nMove West  | w \nPick Up Item      | get (item name) \n Drop Item  | drop (item name) \nInventory  | i\nQuit       | q")        
        elif dir != "q":
            print("**Invalid choice. m for options **")

        
    if len(parsed_dir) > 1:
        action = parsed_dir[0]
        item = ""
        for i in range(1, len(parsed_dir)):
            item += parsed_dir[i] + ' '
        item = item.strip()    

        if action == "g" or action == "get":
            for i in player.room.items:
                if parsed_dir[1] == i.name.lower():
                    print("Adding item to inventory")
                    # put item in player inventory
                    player.inventory.append(i)
                    # remove item from room inventory
                    player.room.items.remove(i)
        elif action == "d" or action == "drop":
            for i in player.inventory:
                if parsed_dir[1] == i.name.lower():
                    print("Removing item from inventory")
                    # put item in player inventory
                    player.inventory.remove(i)
                    # remove item from room inventory
                    player.room.items.append(i)
print("You quit the adventure!  :( ")
"Exit"
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
