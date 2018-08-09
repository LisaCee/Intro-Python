class Item:
    def __init__( self, name, description ):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name} : {self.description}"

    def on_grab(self, player):    
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
        if self.picked_up == False:
            player.score += self.value
            #if not i.picked_up
            #update score
            self.picked_up = True
