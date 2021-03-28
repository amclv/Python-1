# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)



# re-declaring the variable works
f = "abc"
print(f)


# ERROR: variables of different types cannot be combined
# print("this is a string " + 123) # will not work
print("this is a string " + str(123)) # will work


# Global vs. local variables in functions
def someFunction():
    # local variable
    # f = "def"
    # global variable change
    global f
    f = "def"
    print(f)

someFunction()
print(f)

del f
print(f)