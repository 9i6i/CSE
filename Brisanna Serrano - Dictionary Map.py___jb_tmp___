world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's room",
        'DESCRIPTION': "This is the room that you are in.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "A Parking Lot",
        'DESCRIPTION': "There are a few cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A',
            'UP': 'Mt_Abbot'
        }
    },
    'Mt_Abbot': {
        'NAME': "Mt.Abbot",
        'DESCRIPTION': "There is a dark hole here.",
        'PATHS': {
            'DOWN': 'PARKING_LOT',
            'UP': 'The_Ruins'
        }
    },
    'The_Ruins': {
        'NAME': "The Underground.",
        'DESCRIPTION': "You landed on a bed of flowers.",
        'PATHS': {
            'UP': 'Mt_Abbot',
            'WEST': 'Snowdin'
        }
    },
    'Snowdin': {
        'NAME': "Snowdin",
        'DESCRIPTION': "There's snow?",
        'PATHS': {
            'UP': 'The_Ruins',
            'EAST': 'Water_Fall'
        }
    },
    'Water_Fall': {
        'NAME': "Waterfall",
        'DESCRIPTION': "There are blue flowers that repeat what you say????",
        'PATHS': {
            'UP': 'Snowdin',
            'NORTH': 'HOTLAND'
        }
    },
    'HOTLAND': {
        'NAME': "Hotland",
        'DESCRIPTION': "",
        'PATHS': {
            '': '',
            '': ''
        }
    }
}


directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]
playing = True


while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
