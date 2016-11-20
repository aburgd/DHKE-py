import random
answer = raw_input("Public key or shared secret: ")

class DHKE(object):
    def __init__(self, base, modPrime, aSecret):
        self.base = base
        self.modPrime = modPrime
        self.aSecret = aSecret
        self.publicKey = publicKey
    
    @classmethod
    def publicKey(self, base, modPrime, aSecret):
        publicKey = base ** aSecret % modPrime
        print(publicKey)
    
    @classmethod
    def sharedSecret(self, publicKey, modPrime, aSecret):
        sharedSecret = publicKey ** aSecret % modPrime
        print(sharedSecret)

if answer.lower() == "public key":
        print "Your shared base integer is: "
        base = random.randint(1, 1031)
        print base
        modPrime = input("What is your shared second prime? ")
        aSecret = input("What is your secret prime? ")
        pK = DHKE.publicKey(base, modPrime, aSecret)
        print(pK)
elif answer.lower() == "shared secret":
        publicKey = input("What is your public key? ")
        modPrime = input("What is your shared second prime? ")
        aSecret = input("What is your secret prime? ")
        sS = DHKE.sharedSecret(publicKey, modPrime, aSecret)
        print(sS)
else:
    print("Goodbye!")
