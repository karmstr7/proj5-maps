import logging


def process(raw):
    address_book = []
    for line in raw:
        if line[0] != '#':
            place = line.split("    ")
            address_book.append(place)
    return address_book


def main():
    f = open("data/pois.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
