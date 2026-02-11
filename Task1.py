#Task 1 of Assignment 3 -Calculate Factorial using a Function

def factorial(num):         #non-recursive function calculating factorial
    f = 1
    for i in range(1,num+1):
        f *= i
    return f

def rec_factorial(num):     #recursive function calculating factorial
    if num == 1:
        return 1
    else:
        return num * rec_factorial(num-1)

n1 = int(input("Enter a number : "))
fact1 = factorial(n1)
print(f"Factorial of {n1} is : {fact1}")

n2 = int(input("Enter a number : "))
fact2 = rec_factorial(n2)
print(f"Factorial of {n2} is : {fact2}")

#end of program