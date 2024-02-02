# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: MULTIPLICATION TABLE
#
# NAME:         Jennie
# ASSIGNMENT:   Project 3: Arrays & Maps

# Write a function called multiplication_table that
# takes a width, height, & scaling factor as parameters
# and returns a two-dimensional array multiplication
# table scaled by the scaling factor.
# You should not be using any functions other than range.
def multiplication_table(w, h, s):
    # check if w or h is 0
    if w == 0 or h == 0:
        return None
    
    # Create a 2D array filled with zeros
    table = [[0 for _ in range(w)] for _ in range(h)]
    
    # multiplication values
    for i in range(h):
        for j in range(w):
            table[i][j] = (i + 1) * (j + 1) * s
            
    return table

def print_2D(b):
    for i in range(len(b)):
        print(b[i])

def main():
    print("5 3 1:")
    print_2D(multiplication_table(5, 3, 1))
    print("5 3 2:")
    print_2D(multiplication_table(5, 3, 2))

# Don't run main on import
if __name__ == "__main__":
    main()

