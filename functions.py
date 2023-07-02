# Function ==> functions is a block of code which perform a specific Task

# 1 . normal Function
# 2 . lambda Function

# creating a function

def hello():
    print("Hello World!")

hello() # call

#output ==>
# Hello World!

# function with parameter

def double(x):
    return x*2

double = double(8)
print(double)

#output ==>
# 16

# function to check no. is even or odd

def even_odd(x):
    if x%2==0:
        print("number is even")
    elif x == 0:
        print("number is equal to 0")
    else:
        print("number is odd")

even_odd(5)

#output ==>
# number is odd

#lambda function

cube = lambda x:x*x*x
print(cube(9))

#output ==>
# 729

