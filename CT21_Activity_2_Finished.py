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
def readData (pFile):
    theFile = open (pFile, "r")         # Open the file
    for line in theFile:                # Process every line
        line = line.strip ()
        print (line)

    theFile.close ()

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
print ("Welcome to the sprouting seed program.")
readData (INPUT_FILE)

