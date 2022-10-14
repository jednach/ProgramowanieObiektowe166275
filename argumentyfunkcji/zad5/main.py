# zad5

def make_car(firma, model, **kwargs):
    dict = {}
    dict["Firma"] = firma
    dict["Model"] = model
    dict.update(kwargs)
    return dict


def main():
    print(make_car("Kia", "Picanto", pojemnosc_silnika=900, kolor="cafe mocca"))


if __name__ == '__main__':
    main()
