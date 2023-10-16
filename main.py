# In this file I want to run some examples, exceptions that may occur
# At first importing my bike class
from bike2 import Bike

# Using try blocks to raise the exception that may occur
try:
    # Let's start with myBike
    myBike = Bike(numGears=20, currentGear=1, numWheels=2, brakeType="electric")
    # Updating the current gear to 10
    myBike.updateCurrentGear(10)

    # Printing examples for myBike
    print(f"Number of Gears: {myBike.getNumberOfGears()}")
    print(f"Current Gear: {myBike.getCurrentGear()}")
    print(f"Number of Wheels: {myBike.getNumberOfWheels()}")
    print(f"Brake Type: {myBike.getBreakType()}")
    #print(f"update gear: {myBike.updateCurrentGear()}")

    # A blank line
    print()
    # A little break
    input("Press ENTER to continue")

    # It's for you..
    newGear = int(input("What is the new gear? "))
    myBike.updateCurrentGear(newGear)

    # Code for increasing, decreasing, and resetting the gear.
    myBike.increaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")

    myBike.decreaseGear()
    print(f"Current Gear: {myBike.getCurrentGear()}")

    myBike.resetGears()
    print(f"Current Gear: {myBike.getCurrentGear()}")

    # trying to set and get break type electric
    myBike.setBrakeType("electric")
    print(f"Brake Type: {myBike.getBreakType()}")

except Exception as e:
    print(f"Error creating the bike: {str(e)}")

    # A blank line, and a break
    print()
    input("Press ENTER to continue")

# try and exception again
try:
    # Creating limaBike by instantiating another Bike object
    limaBike = Bike()
    limaBike.setNumberOfGears(12)
    limaBike.setCurrentGear(1)
    limaBike.updateCurrentGear(3)
    limaBike.setNumberOfWheels(4)
    limaBike.setBreakType("foot brakes")

    # It's all about limaBike
    print(f"Properties of limaBike")
    print(f"My bike has {limaBike.getNumberOfGears()} gears.")
    print(f"Current Gear: {limaBike.getCurrentGear()}")
    print(f"Number of Wheels: {limaBike.getNumberOfWheels()}")
    print(f"Brake Type: {limaBike.getBreakType()}")


except ValueError as ve:
    print(f"Value Error when setting properties for limaBike: {str(ve)}")
except Exception as e:
    print(f"Error creating limaBike: {str(e)}")
