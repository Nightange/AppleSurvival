def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1 or num > 9:
                print("\nThat isn't a place on the map, try again!\n")
            else:
                return num
        except ValueError:
            print("\nThat isn't a place on the map, try again! \n")