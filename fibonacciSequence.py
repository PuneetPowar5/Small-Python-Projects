print("Welcome to the Fibonacci Sequence Generator\n")

maxNum = int(input("How many numbers of the sequence do you want to see? \n"))

maxNum = int(maxNum)

a = 0

b = 1

c = 0

print("\n")

for num in range(0, maxNum):
    if(num <= 1):
        c = num
    else:
        c = a + b
        a = b
        b = c
    print(c)