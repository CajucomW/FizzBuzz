###        FizzBuzz        ###
# numbers divisible by 3 are Fizz
# numbers divisible by 5 are Buzz
# numbers divisible by both 3 and 5 are FizzBuzz

name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

fizz = number % 3
buzz = number % 5

if fizz == buzz == 0:
    print("FizzBuzz!")
elif fizz == 0:
    print("Fizz!")
elif buzz == 0:
    print("Buzz!")
else:
    print("Have a nice day!")
