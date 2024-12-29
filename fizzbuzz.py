"""Fizz buzz program"""
#looping from 1 to 100
def fizzbuzz(n):
    #checking if number is divisible by 3 and 5
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    #if number is divisible by 3, return "Fizz"
    elif n % 3 == 0:
        return "Fizz"
    #if number is divisible by 5, return "Buzz"
    elif n % 5 == 0:    
        return "Buzz"
    else:
        return n

print(fizzbuzz(45))