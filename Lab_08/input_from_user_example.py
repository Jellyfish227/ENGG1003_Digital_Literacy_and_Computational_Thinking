#!/usr/bin/env python3

# test interactively: exec(open("input_from_user.py").read())

# User may input some text (string) using input( )
name = input("What's your name? ")
print("Hi,", name, "!")

# User may input an integer, with int( ) conversion
age = int(input("What's your age? "))
print('You will be', (age+1), "years old")

# User may input a real number, with float( ) conversion
bodyWeight = float(input("What's your weight in kg? "))
print('Your weight is', bodyWeight, "kg")
