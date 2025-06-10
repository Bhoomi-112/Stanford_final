class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def link_room(self, room, direction):
        self.exits[direction] = room

    def get_details(self):
        print(f"\n{self.name}")
        print(self.description)
        for direction in self.exits:
            print(f"To the {direction} is {self.exits[direction].name}")
        if self.items:
            print("You see:", ", ".join(self.items))

class Game:
    def __init__(self):
        self.rooms = self.create_world()
        self.current_room = self.rooms['hall']
        self.inventory = []

    def create_world(self):
        # Initialize the game world
       
        # Create rooms and link them
        hall = Room("Hall", "A long, dimly lit hallway.")
        kitchen = Room("Kitchen", "A kitchen with a strange smell.")
        bedroom = Room("Bedroom", "A cozy bedroom with a soft bed.")

        hall.link_room(kitchen, "east")
        kitchen.link_room(hall, "west")
        
        hall.link_room(bedroom, "south")
        bedroom.link_room(hall, "north")

        kitchen.items.append("key")
        bedroom.items.append("note")

        return {'hall': hall, 'kitchen': kitchen, 'bedroom': bedroom}

    def play(self):
        print("Welcome to the Adventure Game!", end ="\n\n")
        
        print("Instructions:")
        print("Type 'go <direction>' to move (e.g., 'go east').")
        print("Type 'take <item>' to pick up an item (e.g., 'take key').")
        print("Type 'inventory' to see what you're carrying.")
        print("Type 'quit' or 'exit' to end the game.\n")
        while True:
            self.current_room.get_details()
            command = input("\n> ").strip().lower()
            if command in ["quit", "exit"]:
                print("Thanks for playing!")
                break
            elif command.startswith("go "):
                direction = command[3:]
                if direction in self.current_room.exits:
                    self.current_room = self.current_room.exits[direction]
                else:
                    print("You can't go that way.")
            elif command.startswith("take "):
                item = command[5:]
                if item in self.current_room.items:
                    self.current_room.items.remove(item)
                    self.inventory.append(item)
                    print(f"You took the {item}.")
                else:
                    print("That item isn't here.")
            elif command == "inventory":
                print("Inventory:", ", ".join(self.inventory) if self.inventory else "Empty")
            else:
                print("Unknown command.")

if __name__ == "__main__":
    Game().play()
