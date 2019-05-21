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


class Inventory(object):
    def __init__(self, items=()):
        self.items = items


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
Phone = Phone("Phone")

R19A = Room("This is a room.", "Mr.Wiebe's room")
parking_lot = Room("This is where you can park your car", "This is the parking lot")
Mt_Abbot = Room("This is a mountain where monsters live", "This Mt. Abbot")
The_Ruins = Room("You fell into the hole now you are in a room that has golden flowers???",
                 "You are now in the underground")
Toriel_house = Room("as you were walking in the ruins you see a small house and the door was open so you walk "
                    "in", "Toriel's house")
Snowdin = Room("There is snow in this room??", "You just past the ruins now you are in snowdin")
Sans_and_Papy_house = Room("As you walked through Snowdin you spotted a house with two"
                           " mailbox and both of them have a name on both sans and "
                           "papyrus", "you are in front of a monster house who have a lab in the back")
Water_Fall = Room("There are blue flowers that repeat what you say", " You are now in Waterfall")
Gaster_door = Room("there is a weird door in the middle of waterfall "
                   "wall you stared at it for a good 20 second "
                   "and it disappear", "Le gasters door")
Hotland = Room("You look around and you see lava and you question how is this possible then "
               "stop caring and you move on to the next area", "You are in hotland")
The_core = Room("There are wired everywhere you see you wonder"
                " what this place use to be", "You are in the core now")
True_lab = Room("You see ghost like monsters that creep you out", "This is true lab")
New_home = Room("You look around there building everywhere some nice some doesn't"
                " anyway you move on", "You are in new home")
Judgement_hall = Room("There windows everywhere and it looked very nice", "Judgement hall")
Throne_room = Room("you walk pass the hall and you see 2 garden bed of sunflowers and a big "
                   "Chair in front", "Your in the throne room, you are also almost to the barrier")
The_Barrier = Room("You have reached the barrier this is where the humans trapped the monsters"
                   " years ago. You want to set them free?!?!?!?!?!", "The barrier where it all ends")
The_Surface = Room("You have broken the Barrier now all the monsters "
                   "are free and abel to live with the "
                   "humans oh so they thought.", "The Surface.Is this the end?")

R19A.items = monstercandy
parking_lot.items = Phone
Mt_Abbot.items = knife


R19A.n = parking_lot
parking_lot.s = Mt_Abbot
Mt_Abbot.u = The_Ruins
The_Ruins.u = Toriel_house
Toriel_house.n = Snowdin
Snowdin.w = Sans_and_Papy_house
Sans_and_Papy_house.u = Water_Fall
Water_Fall.u = Gaster_door
Gaster_door.d = Water_Fall
Water_Fall.d = Hotland
Hotland.e = The_core
The_core.n = New_home
New_home.e = Judgement_hall
Judgement_hall.w = Throne_room
Throne_room.w = The_Barrier
The_Barrier.u = The_Surface

player = Player(R19A)

directions = ['n', 's', 'e', 'w', 'u', 'd']
playing = True

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.items is not None:
        print("There is %s here" % player.current_location.items.name)

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
    elif "pick up " in command:
        item_name = command[8:]

        found_item = None
        if player.current_location.items.name == item_name:
            found_item = player.current_location.items

        if found_item is None:
            print("i don't see anything in here.")
        else:
            player.inventory.append(found_item)
            print("grabs %s" % item_name)
            player.current_location.items = None
    else:
        print("Command not recognized.")
