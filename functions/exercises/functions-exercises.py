# Part 1 A -- Make a Line
def make_line(size):
    line =""
    for i in range(size):
        line += "#"
    return line

#print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for i in range(size):
        square += "\n" + make_line(size) 
    return square

print(make_square(9))
    





# Part 1 C -- Make a Rectangle





# Part 2 A -- Make a Stairs





# Part 2 B -- Make Space-Line 





# Part 2 C -- Make Isosceles Triangle





# Part 3 -- Make a Diamond






