class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the engine starts.")

    def move_forward(self):
        self.fuel -= 1
        print("You move forward.")

    def turn_left(self):
        self.fuel -= 1
        print("SHE'S MAKING A LEFT TURN!!!!")

    def turn_orr(self):
        self.engine_status = False
        print("You turn the engine off.")


class Viper(Car):
    def __init__(self):
        super(Viper, self).__init__("Viper")


class Tesla(Car):
    def __init__(self):
        super(Tesla, self).__init__("Tesla")

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the engine starts")


brisa_car = Viper()
brisa_car.start_engine()
brisa_car.move_forward()
brisa_car.turn_left()
brisa_car.move_forward()
brisa_car.turn_orr()
print()

bethany_car = Tesla()
bethany_car.start_engine()
bethany_car.move_forward()
