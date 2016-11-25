"""
Diffie-Hellman Key Exchange Algorithm Demonstration
This module is a demonstration of the Diffie-Hellman(-Merkle) Key Exchange
Algorithm.

For those unfamiliar, this algorithm is a system of two non-linear equations.
The first is used to find a user's, Alex, public key, A.

    A = base ^ secret_a _mod_ prime

_A_ is found by taking some shared _base_ integer and raising it to the Alex's
_secret_ integer, and taking the remainder of that product divided by
a shared modulus _prime_.

The second equation is used to find a pair of users', Alex and Bailey, shared
secret, one that some eavesdropper, Edward, would be unable to calculate
without either Alex's nor Bailey's secret integers.

    s = A ^ secret_b _mod_ prime

_s_ is found by taking Alex's public key, raising it to Bailey's secret integer,
and finding the remainder of that product divided by the same shared modulus
_prime_.

"""

import os
import sys


def generate():
    """generates random bytes and makes them into a usable integer

    >>> type(generate()) is int
    True
    >>> type(generate()) is not int
    False
    """
    num_bytes = os.urandom(3)
    num = int.from_bytes(num_bytes, sys.byteorder)
    return num


def gen_check(number):
    """checks generated integer for primality"""
    if aks(number):
        return number
    elif not aks(number):
        while not aks(number):
            print("Not using %d" % number)
            number = generate()
    gen_check(number)
    return number


def input_check(number):
    """checks user input primality"""
    if aks(number):
        return number
    elif not aks(number):
        while not aks(number):
            print("Sorry, that number isn't prime.")
            number = input("Please try another: ")
    input_check(number)
    return number


def aks(number):
    """check if integer number is a prime
    >>> aks(5)
    True
    >>> aks(12705198)
    False
    """
    # make sure n is a positive integer
    number = abs(int(number))
    # 0 and 1 are not primes
    if number < 2:
        return False
    # 2 is the only even prime number
    if number == 2:
        return True
    # all other even numbers are not primes
    if not number & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of number
    # for all odd numbers
    for x_range in range(3, int(number**0.5) + 1, 2):
        if number % x_range == 0:
            return False
    return True


def public_key():
    """generates a public key integer"""
    # gets or makes base integers
    resp = input("Do you have a shared base integer? (y/n): ")
    if resp.lower() == "y":
        base_prime = input("Please enter your shared base integer: ")
        input_check(base_prime)
    elif resp.lower() == "n":
        base_prime = generate()
        print("Your shared base integer is: ", gen_check(base_prime))
    # gets or makes secret integer
    resp = input("Do you have a secret integer? (y/n): ")
    if resp.lower() == "y":
        alex = input("Please enter your secret integer: ")
        input_check(alex)
    elif resp.lower() == "n":
        alex = generate()
        print("Your secret integer is: ", gen_check(alex))
    # gets or makes shared modulus
    resp = input("Do you have a shared modulus? (y/n): ")
    if resp.lower() == "y":
        mod_prime = input("Please enter your shared modulus: ")
        input_check(mod_prime)
    elif resp.lower() == "n":
        mod_prime = generate()
        print("Your shared modulus is: ", gen_check(mod_prime))

    pub_key = int(base_prime) ** int(alex) % int(mod_prime)
    return pub_key


def shared_secret():
    """generates a shared secret integer"""
    pub_key = input("Please enter your public key: ")
    mod_prime = input("Please enter your shared modulus: ")
    alex = input("Please enter your secret integer: ")
    shared_sec = (int(pub_key) ** int(alex)) % int(mod_prime)
    return shared_sec


def __main__():
    answer = input("Would you like to calculate a public key, or a shared secret? ")
    if answer.lower() == "public key":
        public = public_key()
        print("Your public key is: ", public)
    elif answer.lower() == "shared secret":
        shared = shared_secret()
        print("Your shared secret is: ", shared)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
