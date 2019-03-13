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


class Character (object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because of the armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
            print("% has %d health left" % (self.name, self.health))

    def attack(self, target):
        print(" %s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


knife = Weapon("knife", 30)
monstercandy = Food("Monster Candy", 10)
