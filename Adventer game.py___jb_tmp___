class Room(object):
    def __init__(self, deception="INSERT DESCRIPTION HERE", name=None, north=None, south=None,
                 east=None, west=None, up=None, down=None):
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
        """

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """

        :param direction: direction: A String (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)


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
            'EAST': 'Hotland'
        }
    },
    'Hotland': {
        'NAME': "Hotland",
        'DESCRIPTION': "everything is hot oh well",
        'PATHS': {
            'WEST': 'Water_Fall',
            'NORTH': 'The_Core'
        }
    },
    'The_Core': {
        'NAME': "the core",
        'DESCRIPTION': "you see a lab and you wonder how that possible then you"
                       " realize there snow and lava here then you stop caring",
        'PATHS': {
            'SOUTH': 'Hotland',
            'EAST': 'New_Home'
        }
    },
    'New_Home': {
        'NAME': "new home"
    }
}


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Food(Item):
    def __init__(self, name, heath):
        super(Food, self).__init__(name)
        self.food = heath


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name)
        self.power = True
        self.battery_left = 100

    def power_on(self):
        self.power = True
        print("You turn on the phone")


class Knife(Item):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.attack_damage = 30
        self.take_damage = 10


class MonsterCandy(Item):
    def __init__(self, name):
        super(MonsterCandy, self).__init__(name)
        self.health = 10
        self.level = 0.5


R19A = Room
parking_lot = Room
Mt_Abbot = Room
The_Ruins = Room
Snowdin = Room
Water_Fall = Room
Hotland = Room
The_core = Room
New_home = Room

R19A.north = parking_lot
parking_lot.south = R19A
Mt_Abbot.up
The_Ruins.up
Snowdin.west
Water_Fall.down
Hotland.east
The_core.north
New_home.east


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
