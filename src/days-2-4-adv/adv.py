from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("--Outside--", "There is a blue 'police box' in front of you. It is the about the size of an old telephone booth. There is a light on the top. The door is open.", [Item('Key', "This key opens something")]),

    'inside':    Room("--Console Room--", """It's bigger on the inside!!!  You are in a large room with white circles on the walls. There is a console in front of you. There are doorways to either side.""", [Item('Lantern', 'Use this lantern to light the way ahead.')]),

    'console': Room("--TARDIS Console--", """The console is metal and rolling lights.  There are screens and buttons and levers. Do you go forward to push a button or take a step back?""", [Item('Screwdriver', 'It is dangerous to go alone. Take this sonic screwdriver.')]),

    'past': Room("--Dinosaurs!?!--", """There is a clunky, whirring noise. The police box shakes. You open the door and see ... dinosaurs!?! And the sky is purple. You did not sign up for this. Go back to safety.""", [Item('Fez', 'How is there a fez in this wild place? You put in on your head - just in case. ')]),

    'bedroom':   Room("--Bedroom--", """You enter a bedroom with twin-size bunk beds along one wall. It's not exactly the honeymoon suite, but does this mean someone lives in this thing? There is a door in front of you. Do you dare continue on or do you chicken out and go back?""", [Item('Coins', 'These coins look like they are worth a lot of money! $$$')]),

    'garden': Room("--Garden--", """You are now deep inside the box and have discovered a garden. There are flowers bigger than your head and some menacing vines swaying back and forth in the still air.  Do you go back or check out the door to your left?""", [Item('Potion', 'An unknown potion. Use at your own risk')]),

    'pool': Room("--Swimming Pool--", """There is a large swimming pool with crystal blue water and floaty toys. There are fluffy towels on lounge chairs on the deck. There is a door in front of you or would you like to go back he way you came?""", [Item('Scarf', 'Who needs a super-long, multi-colored scarf at the pool?')]),

    'library': Room("--Library--", """You walk into a ginormous library filled with millions of books. There is a note tacked to a nearby shelf. It reads: \n'You want weapons? You're in a library. Books are the best weapon in the world. This room's the greatest arsenal you could have. Arm yourself.' \nThere is a doorway to your right and behind you. Or would you like to stay and read a while?""", [Item('Book', 'This book has a metallic cover. You open it up and see a language you don\'t recognize. It was published in the year 8575.')]),
}

# Link rooms together

room['outside'].f_to = room['inside']
room['inside'].b_to = room['outside']

room['inside'].f_to = room['console']
room['console'].b_to = room['inside']

room['console'].f_to = room['past']
room['past'].b_to = room['console']

room['inside'].r_to = room['bedroom']
room['bedroom'].l_to = room['inside']

room['library'].r_to = room['inside']
room['inside'].l_to = room['library']

room['library'].b_to = room['pool']
room['pool'].f_to = room['library']

room['bedroom'].f_to = room['garden']
room['garden'].b_to = room['bedroom']

room['garden'].l_to = room['pool']
room['pool'].r_to = room['garden']

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

    dir = input("------------------\nPlease enter a direction... f-(forward), b-(backwards), l-(left), r-(right) OR q to quit the game. \nPress m for more options. \n---------\n").lower()
    parsed_dir = dir.lower().split()

    if len(parsed_dir) is 1:
        # directional inputs
        if dir == "f" or dir == "b" or dir == "l" or dir == "r":
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
            print("Move Forward   | f \nMove Backwards | b \nMove Right     | r \nMove Left      | l \nPick Up Item   | get (item name) \nDrop Item      | drop (item name) \nInventory      | i\nQuit           | q")        
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
print("You quit the adventure! You step outside the box. There is a whoop-whoop noise and the box disappears. Maybe some day you will see the box again and can explore further.  :( ")
"Exit"
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
