# Simple Python Code for computing the volume of a Cylinder
# 
# This code can be used in two different ways:
# Imported and used by another Python program
# Ran by itself

import math

# Function to calculate the volume of a sphere
# Formula: Volume = (4/3)πr^3
def volume(rad):
    volume = (4/3) * math.pi * (rad * rad * rad)
    return volume

# Function to prompt user for input and display the volume
# This function is only called if this file is run directly
def prompt():
    print()
    print("-----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME OF A sphere")
    print("-----------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))

    print("\nThe Volume of a sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()