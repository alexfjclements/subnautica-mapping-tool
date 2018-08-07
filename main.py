import numpy as np

print("\nWelcome to the Subnautica map positioning tool.\n" +
      "This tool converts distance to lifepod 5 and bearing to measurements from the lifepod on a map.\n" +
      "These take the form of a North/South coordinate, and an East/West coordinate.\n" +
      "North and East are given as positive.\n" +
      "This tool uses a scale of 20m/mm, or 50mm/km.\n\n")

# Number of coordinates to convert
loops = int(input("How many coordinates would you like to convert?\n"))


# Define bearing from Lifepod 5
def bearingcalc(direc, finedirec):

    # Bearing from current position to lifepod 5
    negbearing = 0

    # Define bearing from Lifepod 5:
    truebearing = 0

    if direc == "N":
        negbearing = 0

    elif direc == "NE":
        negbearing = 45

    elif direc == "E":
        negbearing = 90

    elif direc == "SE":
        negbearing = 135

    elif direc == "S":
        negbearing = 180

    elif direc == "SW":
        negbearing = 225

    elif direc == "W":
        negbearing = 270

    elif direc == "NW":
        negbearing = 315

    finedirec = finedirec * 7.5
    negbearing = negbearing + finedirec

    if 0 <= negbearing < 90:
        truebearing = negbearing + 180

    elif 90 <= negbearing < 180:
        intangle = negbearing - 90
        truebearing = intangle + 270

    elif 180 <= negbearing < 270:
        truebearing = negbearing - 180

    else:
        intangle = negbearing - 270
        truebearing = intangle + 90

    truebearing = np.radians(truebearing)
    return truebearing


# Define function to calculate North/East distances.
def northeast(truebearing, lp5dist):

    east = lp5dist * np.sin(truebearing)
    north = lp5dist * np.cos(truebearing)

    return north, east


# Functional code

n = 0

while n < loops:


    direction = str.upper(input("Please input the closest marked sub-division initials (N, NE, SW, etc.)\n"))
    finedirection = float(input("Please input the number of scale divisions from the marked sub division.\n" +
                      "EG: if the closest direction is NE and the bearing is 1 1/2 scale divisions towards the East,\n" +
                      "the entry would be 1.5. If it was 1 1/2 scale divisions to the North the entry would be -1.5.\n"))
    lp5distance = float(input("Please input distance to lifepod 5 in metres.\n"))

    bearing = bearingcalc(direction, finedirection)
    northdist, eastdist = northeast(bearing, lp5distance)

    northmeas = northdist / 20
    eastmeas = eastdist / 20

    print("The required position from Lifepod 5 is:\n" +
        "\033[1m" + "%.0f" % northdist + " metres North by " + "%.0f" % eastdist + " metres East.\n" +
        "This translates to " + "%.0f" % northmeas + "mm North by " + "%.0f" % eastmeas + "mm East\n\n" + "\033[0m")
    n = n + 1
