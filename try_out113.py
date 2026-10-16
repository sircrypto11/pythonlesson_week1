##Write a program that generates a random number between 1 and 100. The user has to guess the number in a limited number of attempts. Provide feedback after each guess (higher, lower, or correct).

import random
random.random=random.randint(1,3)
input("Man your guess:")
input("Gal input your guess:")

print("The Random number is:",random.random)


def math(numb1,numb2):
  fn=int(input("Input your{numb1} and {numb2} numbers:"))


print("Your: {fn}")