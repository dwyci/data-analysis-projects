engine_indicator_light = 'red blinking'
fuel_level = 21000
engine_temperature = 1200


# 5) Implement the following checks using if/else if/else statements:

# a) If fuel_level is above 20000 AND engine_temperature is at or below 2500, print "Full tank. Engines good."

if fuel_level > 20000 and engine_temperature <= 2500:
    print("Full tank.  Engines good.")

# b) If fuel_level is above 10000 AND engine_temperature is at or below 2500, print "Fuel level above 50%.  Engines good."
elif fuel_level > 10000 and engine_temperature <= 2500:
    print("Fuel level above 50%.  Engines good.")


# c) If fuel_level is above 5000 AND engine_temperature is at or below 2500, print "Fuel level above 25%. Engines good."
elif fuel_level > 5000 and engine_temperature <= 2500:
    print("Fuel level above 25%.  Engines good.")

# d) If fuel_level is at or below 5000 OR engine_temperature is above 2500, print "Check fuel level. Engines running hot."
elif fuel_level <= 5000 and engine_temperature > 2500:
    print("Check fuel level. Engines running hot")
# e) If fuel_level is below 1000 OR engine_temperature is above 3500 OR engine_indicator_light is red blinking print "ENGINE FAILURE IMMINENT!" 
elif fuel_level < 1000 and engine_temperature > 3500 or engine_indicator_light == 'red blinking':
    print("ENGINE FAILURE IMMINENT!")
# f) Otherwise, print "Fuel and engine status pending..." 
else: 
    print("Fuel and engine status pending...")

# Code 5a - 5f here:



# 6) a) Create the variable command_override, and set it to be true or false. 
# If command_override is false, then the shuttle should only launch if the fuel and engine check are OK. 
# If command_override is true, then the shuttle will launch regardless of the fuel and engine status.
command_override = False

# 6) b) Code the following if/else check:

# If fuel_level is above 20000 AND engine_indicator_light is NOT red blinking OR command_override is 
# true print "Cleared to launch!" Else print "Launch scrubbed!"
if (fuel_level > 20000 and engine_indicator_light != 'red blinking') or command_override == True:
    print("Launch scrubbed!")
else: 
    print("Lets git it on")
