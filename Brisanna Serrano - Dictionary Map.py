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
            'DOWN': 'Mt_Abbot',
            'WEST': 'Snowdin'
        }
    },
    'Snowdin': {
        'NAME': "Snowdin",
        'DESCRIPTION': "There's snow?",
        'PATHS': {
            'EAST': 'The_Ruins',
            'DOWN': 'Water_Fall'
        }
    },
    'Water_Fall': {
        'NAME': "Waterfall",
        'DESCRIPTION': "There are blue flowers that repeat what you say????",
        'PATHS': {
            'UP': 'Snowdin',
            'EAST': 'HOTLAND'
        }
    },
    'HOTLAND': {
        'NAME': "Hotland",
        'DESCRIPTION': "everything is hot oh well",
        'PATHS': {
            'WEST': 'Water_Fall',
            'NORTH': 'THE_CORE'
        }
    },
    'THE_CORE': {
        'NAME': "the core",
        'DESCRIPTION': "you see a lab and you wonder how that possible then you"
                       " realize there snow and lava here then you stop caring",
        'PATHS': {
            'SOUTH': 'HOTLAND',
            'EAST': 'NEW_HOME'
        }
    },
    'NEW_HOME': {
        'NAME': "new home",
        'DESCRIPTION': "you look around and all you see is gold"
    }
}


directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["R19A"]
playing = True


while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

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
