asterik = "*"
maxAsteriksToBePrinted = 5
numberOfAsteriksPrinted = 0
currentNumberOfAsteriksToPrint = 1

for i in range(maxAsteriksToBePrinted):
    print(asterik * currentNumberOfAsteriksToPrint)
    currentNumberOfAsteriksToPrint += 1
    numberOfAsteriksPrinted += 1

    if numberOfAsteriksPrinted == maxAsteriksToBePrinted:
        currentNumberOfAsteriksToPrint = 4
        for i in range(currentNumberOfAsteriksToPrint):
            print(asterik * currentNumberOfAsteriksToPrint)
            currentNumberOfAsteriksToPrint -= 1











