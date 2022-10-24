#!/usr/bin/env python3

def hello():
    print('Hello, World')

if __name__ == '__main__':
    hello()
# -- // Program which asks for the user's name then proceeds to greet them

try:
    name = str(input("Hello, what is your name?"))
    print("Hello," + name + ", nice to meet you!")
except:
    print("Hello, Stranger")
    
