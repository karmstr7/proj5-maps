def process(raw):
    '''
    Goes through pois.txt in the data directory and find the useful bits.
    :param raw:
    :return: string
    '''
    address_book = ""
    for line in raw:
        if line[0] != '#' and line[0] != '\n':
            line = line.replace("\n", "")
            line = line.replace("Description: ", "")
            line = line.replace("Latitude: ", "")
            line = line.replace("Longitude: ", "")
            place = line.split("    ")
            address_book = address_book + place[0] + ", " + place[1] + ", " + place[2] + ", "
    return address_book


def main():
    f = open("data/pois.txt")
    parsed = process(f)
    print(parsed)


if __name__ == "__main__":
    main()
