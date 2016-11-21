import os
import sys


def generate():
    num_bytes = os.urandom(3)
    num = int.from_bytes(num_bytes, sys.byteorder)
    return num


def gen_check(n):
    '''checks generated integer for primality'''
    if aks(n):
        return n
    elif not aks(n):
        while not aks(n):
            print("Not using %d" % n)
            n = generate()
    gen_check(n)
    return n


def input_check(n):
    '''checks user input primality'''
    if aks(n):
        return n
    elif not aks(n):
        while not aks(n):
            print("Sorry, that number isn't prime.")
            n = input("Please try another: ")
    input_check(n)
    return n


def aks(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def publicKey():
    '''generates a public key integer'''
    # gets or makes base integers
    resp = input("Do you have a shared base integer? (y/n): ")
    if resp.lower() == "y":
        b = input("Please enter your shared base integer: ")
        input_check(b)
    elif resp.lower() == "n":
        b = generate()
        print("Your shared base integer is: ", gen_check(b))
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
        mp = input("Please enter your shared modulus: ")
        input_check(mp)
    elif resp.lower() == "n":
        mp = generate()
        print("Your shared modulus is: ", gen_check(mp))

    pubKey = int(b) ** int(alex) % int(mp)
    return pubKey


def sharedSecret():
    '''generates a shared secret integer'''
    pK = input("Please enter your public key: ")
    mp = input("Please enter your shared modulus: ")
    alex = input("Please enter your secret integer: ")
    sharedSec = (int(pK) ** int(alex)) % int(mp)
    return sharedSec


answer = input("Would you like to calculate a public key, or a shared secret? ")
if answer.lower() == "public key":
    public = publicKey()
    print("Your public key is: ", public)
elif answer.lower() == "shared secret":
    shared = sharedSecret()
    print("Your shared secret is: ", shared)
