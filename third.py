def sqrtBin():
    print("Enter a positive integer, then press Enter: ")
    inputtedValue = input()
    inputtedValue.isnumeric()
    if inputtedValue.isdigit():
        number = int(inputtedValue)
        binary = bin(number)


        binaryString = str(binary)

        stringBinary = binaryString[slice(2, len(binary))]
        print(stringBinary)

        occurences = stringBinary.count("0")
        print(occurences)
        print(occurences ** 2)
    else:
        print("Not an integer")

sqrtBin()