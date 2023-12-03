"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    number = 1
    while(len(list) < number_of_primes):
        number = number + 1
        if(isAPrime(number)):
            list.append(number)
    return list


def isAPrime(x):
    aPrime = True;
    for i in range(2,x):
        if(x % i ) == 0:
            aPrime = False;
    return aPrime
        


