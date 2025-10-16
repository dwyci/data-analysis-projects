# Part 1 A -- Make a Line
def make_line(size):
    line =""
    for i in range(size):
        line += "#"
    return line

#print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
# def make_square(size):
#     square = ""
#     for i in range(size):
#         square += "\n" + make_line(size) 
#     return square

# print(make_square(9))
    

# # Part 1 C -- Make a Rectangle
# def make_rectangle(width, height):
#     rectangle =""
#     for i in range(height):
#         rectangle += "\n" + make_line(width)

#     return rectangle

# print(make_rectangle(9,2)) 

# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
    stairs =""
    for i in range(height):
        i = i+1
        stairs += "\n"+ make_line(i)
       
    return stairs

# print(make_downward_stairs(1))
# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    space_line= ""
    for i in range(numSpaces):
        space_line += " "
    for i in range(numChars):
        space_line +="#"
    for i in range(numSpaces):
        space_line += " "
    return space_line

#print(make_space_line(3, 5))

# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    isosceles =""
    for i in range(height):
        isosceles+= "\n" + make_space_line(height - i - 1,2 * i + 1 )
    return isosceles

print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond






