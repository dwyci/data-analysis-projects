#practice
# a_list = [4, 2, 8, 6, 5, 4]
# a_list[2] = True
# print(a_list)

# b_list = ['barber', 'baby', 'bubbles', 'bumblebee']
# b_list[3 : ] = ['B', 'b']
# print(b_list)

total_points = 0   #Loop by element
scores = [10, 25, 8, 33, 0]
# for score in scores:
#     total_points += score 
# print(total_points)

for index in range(len(scores)):  # loop by index
    total_points  += scores[index]
print(total_points)

# Create the adding_practice list with the following entry: 273.15
# Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.
adding_practice  = [273.15]
adding_practice.append(42)
adding_practice.append("hello")

print(adding_practice)


# Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].

adding_practice = adding_practice + [False, -4.6, '87']
print(adding_practice)


# Use the cargo_hold list for the next set of exercises.
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']

# Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.

cargo_hold[5] = 'space tether'

print(cargo_hold)

# Remove the last item from the list with pop. Print the element removed and the updated list.

removed_item = cargo_hold.pop(-1)
print(removed_item)
print(cargo_hold)


# Remove the first item from the list with pop. Print the element removed and the updated list.
removed_first = cargo_hold.pop(0)
print(removed_first)
print(cargo_hold)


# append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - 
# the number at the start and the string at the end. Print the updated list to confirm the changes.
cargo_hold.insert(0, 1138)
cargo_hold.append('20 meters')
print(cargo_hold)


# Use the remove method to take the parrot out of cargo_hold, then print the updated list.

cargo_hold.remove('parrot')
print(cargo_hold)


#Use .format() to print the final list and its length. "The list ___ contains ___ items."
y = len(cargo_hold)
print(y) 
text = "The list {x} contains {num} items."
print(text.format(x = cargo_hold, num= y))