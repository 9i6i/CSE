class Room(object):
    def __init__(self, description="INSERT DESCRIPTION HERE", name=None, north=None, south=None,
                 east=None, west=None, up=None, down=None, items=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.items = items


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


monstercandy = MonsterCandy("Monster Candy")
knife = Knife("Le knife")

R19A = Room("This is a room.", "Mr.Wiebe's room")
parking_lot = Room("This is where you can park your car", "This is the parking lot")
Mt_Abbot = Room("This is a mountain where monsters live", "This Mt. Abbot")
The_Ruins = Room("You fell into the hole now you are in a room that has golden flowers???",
                 "You are now in the underground")
Snowdin = Room("There is snow in this room??", "You just past the ruins now you are in snowdin")
Water_Fall = Room("There are blue flowers that repeat what you say", " You are now in Waterfall")
Hotland = Room("You look around and you see lava and you question how is this possible then "
               "stop caring and you move on to the next area", "You are in hotland")
The_core = Room("There are wired everywhere you see you wonder what this place use to be", "You are in the core now")
New_home = Room("You look around there building everywhere some nice some doesn't"
                " anyway you move on", "You are in new home")
Judgement_hall = Room("There windows everywhere and it looked very nice", "Judgement hall")
Throne_room = Room("you walk pass the hall and you see 2 garden bed of "
                   "sunflowers and a big Chair in front", "Your in the throne "
                                                          "room, you are also almost to the barrier")
The_Barrier = Room("You have reached the barrier this is where "
                   "the humans trapped the monsters"
                   " years ago. you want to set them free?!?!?!?!?!", "The barrier where it all ends")

R19A.items = monstercandy
The_Ruins.items = knife

R19A.north = parking_lot
parking_lot.south = Mt_Abbot
Mt_Abbot.up = The_Ruins
The_Ruins.up = Snowdin
Snowdin.west = Water_Fall
Water_Fall.down = Hotland
Hotland.east = The_core
The_core.north = New_home
New_home.east = Judgement_hall
Judgement_hall.west = The_Barrier


player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.items is not None:
        print("There is  %s here" % player.current_location.items.name)

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
