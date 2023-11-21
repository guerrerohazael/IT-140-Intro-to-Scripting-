#Hazael Guerrero
# A dictionary for the rooms and direction commands
rooms = {
    'Foyer': {'East': 'Dining Hall'},
    'Dining Hall': {'North': 'Kitchen', 'East': 'Library', 'South': 'Secret Passage'},
    'Kitchen': {'East': 'Study Room', 'South': 'Dining Hall'},
    'Study Room': {'West': 'Kitchen'},
    'Library': {'West': 'Dining Hall', 'North': 'Bedroom'},
    'Bedroom': {'South': 'Library'},
    'Secret Passage': {'East': 'Treasure Room', 'North': 'Dining Hall'},
    'Treasure Room': {'West': 'Secret Passage'}
}

# Defines valid moves within the game
valid_moves = ["North", "South", "East", "West", "Exit"]

current_room = 'Foyer'

def game_instructions():
    print("-------------------------------------------------------------------")
    print("Move commands: North, South, East, West, and Exit (Case Sensitive!)")
    print("-------------------------------------------------------------------")

def move(direction):
    global current_room
    possible_directions = rooms[current_room].keys()

    if direction in possible_directions:
        current_room = rooms[current_room][direction]
    else:
        print("You can't go that way!")
        print("Try instead:", *possible_directions)
        print("-------------------------------------------------------------------")

game_instructions()

# Game loop
while True:
    print("You are in the", current_room + ".\n")
    user_input = input("Enter your move: ").capitalize()
    print("###################################################################")

    if user_input == "Exit":
        break
    elif user_input in valid_moves:
        if user_input != "Exit":
            move(user_input)
    else:
        print("Invalid Command:", user_input)
        game_instructions()

# End of game message
print("Thanks for playing the game. Hope you enjoyed it!")
print("-------------------------------------------------------------------")