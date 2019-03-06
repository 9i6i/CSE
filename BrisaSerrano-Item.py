class Item(object):
    def __init__(self,name):
        self.name = name


class Phone(Item):
    def __init__(self, name):
        super(Phone, self).__init__(name)
        self.power = True
        self.batter_left = 100

    def power(self):
        self.power = True
        print("")