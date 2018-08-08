from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("--Outside--", "There is a blue 'police box' to the north of you. It is the about the size of an old phone box. There is a light on the top. The door is open", [Item('Key', "This key opens something")]),

    'inside':    Room("--Console Room--", """It's bigger on the inside!!! There is a large device in the middle with screens and lights and buttons. Go north to look closer. There are also doorways to your left and right.""", [Item('Lantern', 'Use this lantern to light the way ahead')]),

    'console': Room("--TARDIS Console--", """Description of console""", [Item('Sword', 'It is dangerous to go alone. Take this sword')]),

    'bedroom':   Room("--Bedroom with Bunk Beds--", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [Item('Coins', 'These coins look like they are worth a lot of money')]),

    'wardrobe': Room("--Wardrobe--", """You've found the long-lost wardrobe chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Potion', 'An unknown potion. Use at your own risk')]),

    'pool': Room("--Swimming Pool--", "", []),

    'garden': Room("--Garden--", "", []),

    'library': Room("--Library--", """Shhhhhhh.""", [Item('Book', 'Relax and look at this book')]),
}

# Link rooms together

room['outside'].n_to = room['inside']
room['inside'].s_to = room['outside']
room['inside'].n_to = room['console']
room['console'].s_to = room['inside']
room['inside'].e_to = room['bedroom']
room['bedroom'].w_to = room['inside']
room['bedroom'].s_to = room['wardrobe']
room['wardrobe'].n_to = room['bedroom']
room['console'].w_to = room['library']
room['library'].e_to = room['console']

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

    dir = input("------------------\nPlease enter a direction... n, s, e, w OR q to quit the game. \nPress m for more options. \n---------\n").lower()
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
                print("xx--That direction is a de ad end.--xx")
        elif dir == "i" or dir == "inventory":
            print("Inventory:")
            for item in player.inventory:
                print("\t" + item.name)
        elif dir == "m" or dir == "menu":
            print("Move North   | n \nMove South   | s \nMove East    | e \nMove West    | w \nPick Up Item | get (item name) \nDrop Item    | drop (item name) \nInventory    | i\nQuit         | q")        
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
