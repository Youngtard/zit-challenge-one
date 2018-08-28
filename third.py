def sqr_zeros():
    print("Enter a positive integer, then press Enter: ")
    inputted_value = input()

    if inputted_value.isnumeric():
        decimal_number = int(inputted_value)

        binary_number = bin(decimal_number)
        binary_string = str(binary_number)

        string_binary = binary_string[slice(2, len(binary_number))]
        print("Binary value:", string_binary)

        occurrences = string_binary.count("0")
        print("Occurrences of zero:", occurrences)

        print("Square of occurrences:", occurrences ** 2)
    else:
        print("Inputted value is not a numeric value")


sqr_zeros()
