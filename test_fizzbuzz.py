import pytest 
from fizzbuzz import fizzbuzz

def test_fizzbuzz_is_num():
    #if not divisible by 3 or 5 return number 
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2

def test_fizzbuzz_is_fizz():
    #if divisible by 3 return Fizz
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'

def test_fizzbuzz_is_buzz():
    #if divisible by 5 return Buzz
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_is_fizzbuzz():
    #if divisible by both 3 and 5 return FizzBuzz
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
