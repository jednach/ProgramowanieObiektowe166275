class Car(object):
    def __init__(self, init_w, init_p):
        self.wydajnosc = init_w
        self.pojemnosc = init_p
        self.paliwo = 0

    def drive(self, ile):
        zasieg = self.paliwo * self.wydajnosc * 1000
        if zasieg < ile:
            print("nie masz wystarczajaco paliwa")
            return
        self.paliwo = (zasieg - ile) / (self.wydajnosc * 1000)

    def add_fuel(self, dolewka):
        if self.paliwo + dolewka > self.pojemnosc:
            self.paliwo = self.pojemnosc
        else:
            self.paliwo += dolewka

    def get_fuel_level(self):
        return self.paliwo

def main():
    my_car = Car(20, 40)
    my_car.add_fuel(30)
    my_car.drive(100)
    print(my_car.get_fuel_level())

if __name__ == '__main__':
    main()
