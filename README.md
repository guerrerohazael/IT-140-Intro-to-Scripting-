# IT-140-Intro-to-Scripting-

#Hazael Guerrero
# Define the rooms and their connections
rooms = {
    'Foyer': {'East': 'Dining Hall'},
    'Dining Hall': {'North': 'Kitchen', 'East': 'Library', 'South': 'Secret Passage', 'item': 'Antique Mirror'},
    'Kitchen': {'East': 'Study Room', 'South': 'Dining Hall', 'item': 'Gold Key'},
    'Study Room': {'West': 'Kitchen', 'item': 'Valuable Painting'},
    'Library': {'West': 'Dining Hall', 'North': 'Bedroom', 'item': 'Candlestick'},
    'Bedroom': {'South': 'Library', 'item': 'Jewelry Box'},
    'Secret Passage': {'East': 'Treasure Room', 'North': 'Dining Hall', 'item': 'Old Diary'},
    'Treasure Room': {'West': 'Secret Passage'}
}

# List of valid moves
valid_moves = ["North", "South", "East", "West", "Exit"]

# Initialize the current room
current_room = 'Foyer'

# Display game instructions
def game_instructions():
    print("-------------------------------------------------------------------")
    print("Move commands:")
    print("North, South, East, West - to move to different rooms")
    print("Exit - to quit the game")
    print("-------------------------------------------------------------------")

# Display game instructions initially
game_instructions()

# Function to move the player to a new room
def move(direction):
    global current_room
    possible_directions = rooms[current_room].keys()

    if direction in possible_directions:
        current_room = rooms[current_room][direction]
    else:
        print("You can't go that way!")
        print("Try instead:", *possible_directions)
        print("-------------------------------------------------------------------")

# Display game instructions again
game_instructions()

# Display player's status
def display_status(inventory):
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if 'item' in rooms[current_room]:
        print("You see a", rooms[current_room]['item'])
        print("Type 'get' to pick up the item.")
    print("----------------------")

# Initialize player's inventory
inventory = []

# Game loop
while True:
    display_status(inventory)
    user_input = input("Enter your move: ").capitalize()
    print("###################################################################")

    if user_input == "Exit":
        break
    elif user_input in valid_moves:
        if user_input != "Exit":
            if user_input in ["North", "South", "East", "West"]:
                # Move the player and check if there's an item to pick up
                move(user_input)
                if 'item' in rooms[current_room]:
                    item = rooms[current_room]['item']
                    print(f"You picked up the {item}.")
                    inventory.append(item)
                    del rooms[current_room]['item']
            elif user_input == "Get" and 'item' in rooms[current_room]:
                # Pick up the item in the room
                item = rooms[current_room]['item']
                print(f"You picked up the {item}.")
                inventory.append(item)
                del rooms[current_room]['item']
            else:
                print("You can't go that way!")
        else:
            print("Invalid Command:", user_input)
            game_instructions()

# Check if the player has won or lost
if len(inventory) == 6:
    if current_room == 'Treasure Room':
        print("Congratulations! You have collected all items and won the game!")
    else:
        print("You collected all items, but you need to find the Treasure Room to win!")
else:
    print("NOM NOM...GAME OVER!")

print("Thanks for playing the game. Hope you enjoyed it!")
print("-------------------------------------------------------------------")
