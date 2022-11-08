class Adres(object):
    def __init__(self, nrdomu, ulica, miasto, kod, nrmieszkania=None):
        self.nrdomu = nrdomu
        self.ulica = ulica
        self.miasto = miasto
        self.kod = kod
        if nrmieszkania is not None:
            self.nrmieszkania = nrmieszkania

    def show(self):
        if hasattr(self, "nrmieszkania"):
            print(f'ul. {self.ulica} {self.nrdomu}/{self.nrmieszkania}')
        else:
            print(f'ul. {self.ulica} {self.nrdomu}')
        print(f'{self.kod} {self.miasto}')

    def comes_before(self, other):
        if self.kod > other.kod:
            return True
        return False


def main():
    ad1 = Adres(10, "Warszawska", "Olsztyn", "10-500", 2)
    ad2 = Adres(15, "Pstrowskiego", "Olsztyn", "10-499")
    ad1.show()
    ad2.show()
    print(ad1.comes_before(ad2))


if __name__ == '__main__':
    main()
