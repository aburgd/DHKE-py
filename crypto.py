import random
import time

timestamp = int(time.time())
random.seed(timestamp)


def gen_check(n):
    if not isprime(n):
        while not isprime(n):
            n = random.randint(0, timestamp)


def input_check(n):
    if not isprime(n):
        n = input("Sorry, that number isn't prime. Please try another: ")


def isprime(n):
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
    resp = input("Do you have a shared base integer? (y/n): ")
    if resp.lower() == "y":
        b = input("Please enter your shared base integer: ")
        input_check(b)
    elif resp.lower() == "n":
        b = random.randint(0, timestamp)
        gen_check(b)
        print("Your shared base integer is: ", b)

    resp = input("Do you have a secret integer? (y/n): ")
    if resp.lower() == "y":
        alex = input("Please enter your secret integer: ")
        input_check(alex)
    elif resp.lower() == "n":
        alex = random.randint(0, timestamp)
        gen_check(alex)
        print("Your secret integer is: ", alex)

    resp = input("Do you have a shared modulus? (y/n): ")
    if resp.lower() == "y":
        mp = input("Please enter your shared modulus: ")
        input_check(mp)
    elif resp.lower() == "n":
        mp = random.randint(0, timestamp)
        gen_check(mp)
        print("Your shared modulus is: ", mp)

    b = int(b)
    alex = int(alex)
    mp = int(mp)
    pubKey = b ** alex
    pubKey = pubKey % mp
    return pubKey


def sharedSecret():
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
