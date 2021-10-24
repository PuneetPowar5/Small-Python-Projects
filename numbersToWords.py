import math

def ones(x):
    x = x % 10
    return str(x)

def tens(y):
    y = math.floor(y/10)
    return str(y)

print("Welcome to the Numbers to Words converter")

num = input("Please enter a number between 1 and 99: \n")
num = int(num)

while(num < 1 or num > 99):
    num = input("Please enter a number between 1 and 99: \n")
    num = int(num)

print("There are " + tens(num) + " tens and " + ones(num) + " ones\n")