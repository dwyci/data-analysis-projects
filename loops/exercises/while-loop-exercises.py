# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

startingFuelLevel = 0
numberOfAstronauts = 0
shuttleAltitude = 0



# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 



while(startingFuelLevel < 5000 or startingFuelLevel > 30000):
    startingFuelLevel =  int(input("What is your starting fuel level?"  ))
    print("Please enter a fuel level between 5000 and 30000")

print("You have the right amount of fuel for take off")

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.

while(numberOfAstronauts >7 or numberOfAstronauts<1):
    numberOfAstronauts = int(input("How many astronauts are on board?  "))  
    print("You have too many or too few astronauts.  Please select a differnt amount")

print("You have the right amount of astronauts for take off")  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. 
# Each iteration, decrease the fuel level by 100 units for each astronaut aboard. 
# Also, increase the altitude by 50 kilometers.
i=0
while(startingFuelLevel >100*numberOfAstronauts):
    startingFuelLevel = startingFuelLevel -100*numberOfAstronauts
    shuttleAltitude = shuttleAltitude + 50
    # i= i +1
    # print(i)
    # print(shuttleAltitude)
    


# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
print("The shuttle gained an altitude of " + str(shuttleAltitude) + "km and has " + str(startingFuelLevel)+ "kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

if(int(shuttleAltitude) >= 2000):
    print("Orbit achieved!")
else:
    print("Failed to reach orbit.")