class Item:
    def __init__( self, name, description ):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name} : {self.description}"

    def on_grab(self, player):  
        if not player.room.is_light and not player.light:
            print('Good luck finding items in the dark. Go to another room and find a light, then try again.')
        else:
            print("Adding item to inventory")
            # put item in player inventory
            player.inventory.append(self)
            # remove item from room inventory
            player.room.items.remove(self)

    def on_drop(self, player):
        print("Removing item from inventory")
         # put item in player inventory
        player.inventory.remove(self)
        # remove item from room inventory
        player.room.items.append(self)

class Treasure( Item ):
    def __init__( self, name, description, value ): 
        super().__init__(name, description)
        # Item.__init__(self, name, description)
        self.value = value  
        self.picked_up = False      

    def on_grab(self, player):
        super().on_grab(player)
        if not self.picked_up:
            player.score += self.value
            #if not i.picked_up
            #update score
            self.picked_up = True

class LightSource( Item ):
    def __init__( self, name, description):
        super().__init__(name, description)

    def on_grab(self, player):
        if not player.room.is_light and not player.light:
            print(
                'Good luck finding that in the dark. Go to another room and find a light, then try again.')
        else:
            print("Adding light to inventory")
            # put item in player inventory
            player.inventory.append(self)
            # remove item from room inventory
            player.room.items.remove(self)
            player.light = True
        
    def on_drop(self, player):
        light = input("Are you sure you want to explore in the dark? Y/N \n")
        if light.lower() == "y":
            print("Dropping light")
            # remove item in player inventory
            player.inventory.remove(self)
            player.light = False
            # add item to room inventory
            player.room.items.append(self)