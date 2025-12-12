# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
INPUT_FILE = "Seeds.txt"

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
seedTable = []

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def readData (pFile, pTable):
    splitLine = []
    price = 0.0

    theFile = open (pFile, "r")         # Open the file
    for line in theFile:                # Process every line
        line = line.strip ()
        splitLine = line.split (",")    # Separate into fields

        # Create the record as a list
        record = []
        record.append (splitLine[0])
        record.append (int (splitLine[1]))
        record.append (float (splitLine[2]))

        # Price per gram, rounded to currency
        price = record[2] / record[1] * 10
        price = round (price, 2)
        record.append (price)

        # Add to the table
        pTable.append (record)

    theFile.close ()

def displayTable (pTable):
    layout = "{:<15} {:^6} {:^5} {:^8}"

    print (layout.format ("Name", "Weight", "Price",
                          "10 grams"))
    print ("-" * 40)

    layout = "{:<15} {:^6} {:^5.2f} {:^8.2f}"
    for seed in pTable:
        print (layout.format (seed[0], seed[1],
                              seed[2], seed[3]))

def findCheapest (pTable):
    layout = "The cheapest seed is {} with a price for 10 grams of {:4.2f}"
    cheapest = pTable[0]        # Point to first record

    for seed in pTable:
        if (seed[3] < cheapest[3]):
            cheapest = seed

    print (layout.format (cheapest[0], cheapest[3]))

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
print ("Welcome to the sprouting seed program.")
readData (INPUT_FILE, seedTable)
displayTable (seedTable)
findCheapest (seedTable)