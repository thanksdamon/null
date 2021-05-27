total = 0
homePrices = [["Carson", 125900], ["Smith", 115000], ["Jackson", 105900], ["Swanson", 85000],
              ["Perry", 150000], ["Beufort", 155249], ["Anderson", 97500]]


def findAverage(total):
    for value, element in enumerate(homePrices):
        total += (element[1])

    average = total/len(homePrices)

    print("The total home sales were: $", format(total, ",.2f"))
    print("The average home sales were: $", format(average, ",.2f" ))
    return average

def findHighest():
    highest = 0

    for value, element in enumerate(homePrices):
        if (element[1]) > highest:
            highest = (element[1])
            highestname = element[0]

    print("The highest home selling price was: $", format(highest, ",.2f"),
          "Owned by: ", highestname)
    return highest

def findLowest(highest):
    lowest = highest

    for value, element in enumerate(homePrices):
        if (element[1]) < lowest:
            lowest = (element[1])
            lowestname = element[0]

    print("The lowest selling price was: $", format(lowest, ",.2f"),
          "Owned by: ", lowestname)

def aboveAndBelowAvg(average):
    aboveavg = 0
    belowavg = 0


    for value, element in enumerate(homePrices):
        if (element[1]) < average:
            belowavg += 1

    for value, element in enumerate(homePrices):
        if (element[1]) > average:
            aboveavg += 1

    print("Number of homes sold above average: ", aboveavg)
    print("Number of homes sold below average: ", belowavg)

def main():
    print("Botany Bay Home Sales")
    print("****************")
    print("1.  $",homePrices[0])
    print("2.  $",homePrices[1])
    print("3.  $",homePrices[2])
    print("4.  $",homePrices[3])
    print("5.  $",homePrices[4])
    print("6.  $",homePrices[5])
    print("7.  $",homePrices[6])
    average = findAverage(total)
    highest = findHighest()
    findLowest(highest)
    aboveAndBelowAvg(average)
    

main()
