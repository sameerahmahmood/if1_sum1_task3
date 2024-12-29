from fizzbuzz import fizzbuzz

def test_fizzbuzz_num():
    #number is not divisible by 3 nor 5 nor both
    assert fizzbuzz(1) == 1
    assert fizzbuzz(4) == 4
    assert fizzbuzz(7) == 7
    
def test_fizzbuzz_fizz():
    #number is divisible by 3, return "Fizz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_fizzbuzz_buzz():
    #number is divisible by 5, return "Buzz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(50) == "Buzz"
    
def test_fizzbuzz_fizzbuzz():
    #number is divisible by 3 and 5, return "FizzBuzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    