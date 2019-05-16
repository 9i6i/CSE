class Room(object):
    def __init__(self, deception=None, name=None, north=None, south=None, east=None, west=None, up=None, down=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.deception = deception


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the
        room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)


R19A = Room("Mr. Wiebe's Room")
parking_lot = Room("The Parking Lot", None, R19A)
underground = Room
the_runes = Room

R19A.north = parking_lot
parking_lot.south = R19A
underground.east = parking_lot
the_runes.west = underground

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
