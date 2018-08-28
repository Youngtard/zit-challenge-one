asterisk = "*"
maxAsterisksToBePrinted = 5
currentNumberOfAsterisksToPrint = 1
numberOfAsterisksPrinted = 0

for i in range(maxAsterisksToBePrinted):
    print(asterisk * currentNumberOfAsterisksToPrint)
    currentNumberOfAsterisksToPrint += 1
    numberOfAsterisksPrinted += 1

    # Outer loop iterates 5 times printing out the relevant number of asterisk(s)
    # At the first four iterations, the enclosed if statement doesn't execute because it's condition evaluates to false
    # At the fifth iteration, the if statement is now executed because the condition is now true (asterisks printed
    # equals the maximum to be printed per iteration). Therefore, the nested loop can now run printing the remaining
    # asterisks in reverse order

    if numberOfAsterisksPrinted == maxAsterisksToBePrinted:
        currentNumberOfAsterisksToPrint = 4

        for j in range(currentNumberOfAsterisksToPrint):
            print(asterisk * currentNumberOfAsterisksToPrint)
            currentNumberOfAsterisksToPrint -= 1
