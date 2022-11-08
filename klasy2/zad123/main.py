class Wymierna(object):
    def __init__(self, p_=0, q_=1):
        a = abs(p_)
        b = abs(q_)
        while b:
            a, b = b, a % b

        if q_ == 0:
            q_ = 1

        if q_ < 0:
            p_ *= -1
            q_ *= -1

        self.licznik = int(p_ / a)
        self.mianownik = int(q_ / a)

    def get_licznik(self):
        return self.licznik

    def get_mianownik(self):
        return self.mianownik

    def __repr__(self):
        return f'{self.licznik}/{self.mianownik}'

    def __float__(self):
        return self.licznik/self.mianownik

    def __add__(self, other):
        return Wymierna(self.licznik * other.mianownik + other.licznik * self.mianownik, self.mianownik * other.mianownik)

    def __sub__(self, other):
        return Wymierna(self.licznik * other.mianownik - other.licznik * self.mianownik, self.mianownik * other.mianownik)

    def __eq__(self, other):
        if self.licznik/self.mianownik == other.licznik/other.mianownik:
            return True
        return False

    def __ne__(self, other):
        if self.licznik/self.mianownik != other.licznik/other.mianownik:
            return True
        return False

    def __lt__(self, other):
        if self.licznik/self.mianownik < other.licznik/other.mianownik:
            return True
        return False

    def __le__(self, other):
        if self.licznik/self.mianownik <= other.licznik/other.mianownik:
            return True
        return False

    def __gt__(self, other):
        if self.licznik/self.mianownik > other.licznik/other.mianownik:
            return True
        return False

    def __ge__(self, other):
        if self.licznik/self.mianownik <= other.licznik/other.mianownik:
            return True
        return False

    def __mul__(self, other):
        return Wymierna(self.licznik*other.licznik,self.mianownik*other.mianownik)

    def __div__(self, other):
        return Wymierna(self.licznik*other.mianownik,self.mianownik*other.licznik)

    def __eq2__(self, other):
        if self > other or self < other:
            return False
        return True
w1 = Wymierna(4, 3)
print(w1.get_licznik())
print(w1.get_mianownik())
print(w1.__repr__())
print(w1.__float__())
w2 = Wymierna(-4,-3)
w3 = w1.__add__(w2)
print(w3.__repr__())
w4 = w1.__sub__(w2)
print(w4.__repr__())
print(w1.__eq__(w2))
print(w1.__eq2__(w2))