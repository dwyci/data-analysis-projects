# 1. Declare and assign the variables here:
shuttleName = "Determination"
shuttleSpeed = 17500
distanceToMars = 225000000
distanceToMoon = 384400
milesPerKm = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttleName))
print(type(shuttleSpeed))
print(type(distanceToMars))
print(type(distanceToMoon))
print(type(milesPerKm))

# Code your solution to exercises 3 and 4 here:
milesToMars = milesPerKm*distanceToMars
hoursToMars = milesToMars/shuttleSpeed
daysToMars = hoursToMars/24

print(shuttleName + " will take "  + str(daysToMars)+ " days to reach Mars.")

# Code your solution to exercise 5 here
milestoMoon = milesPerKm*distanceToMoon
hoursToMoon = milestoMoon/shuttleSpeed
daysToMoon = hoursToMoon/24

print(shuttleName + " will take " + str(daysToMoon) + " days to reach the Moon")