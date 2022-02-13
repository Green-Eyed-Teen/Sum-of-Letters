def taking_input():
    char = ""
    try:
        char = str(input("Enter the word: "))
    except ValueError:
        print("Invalid Input!")
        exit()
    char = char.lower()
    return char
