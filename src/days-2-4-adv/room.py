# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __repr__(self):
        return f"{self.name}"    

    # def view_items(self):
    #     print("Items found in this room")
    #     if len(self.items) == 0:
    #         print("none")
    #     else:
    #         for i in self.items:
    #             print("\t" + i)
