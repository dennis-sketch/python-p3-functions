#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    greet_programmer()

def greet(name):
    print("Hello, {name}!")
    greet("Sunny")

def greet_with_default(name="programmer"):
    print("Hello, {name}!")
    greet_with_default("Sunny")
    greet_with_default()

def add(num1, num2):
    result=(2 + 2)
    print(4)

def halve(number):
    result=(4/2)
    print(2)
