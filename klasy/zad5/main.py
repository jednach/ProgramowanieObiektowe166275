class Student(object):
    def __init__(self, imie_, nazwisko_):
        self.imie = imie_
        self.nazwisko = nazwisko_
        self.wynik = 0
        self.ileq = 0

    def get_name(self):
        return f'{self.imie} {self.nazwisko}'

    def add_quiz(self, score):
        self.wynik += score
        self.ileq += 1

    def get_total_score(self):
        return self.wynik

    def get_average_score(self):
        return self.wynik / self.ileq

def main():
    s1 = Student("xxx", "yyy")
    print(s1.get_name())
    s1.add_quiz(2)
    s1.add_quiz(30)
    print(s1.get_total_score())
    print(s1.get_average_score())

if __name__ == '__main__':
    main()