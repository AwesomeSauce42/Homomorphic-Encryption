import math
import random
from random import shuffle
import sys
import gmpy2
from time import time
from Crypto.Util.number import getPrime
import numpy as np


#Function to get Greatest Common Divisor
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

#Function to get Lowest Common Multiple
def lcm(a, b):
    return a * b // gcd(a, b)

def int_time():
    return int(round(time() * 1000))

#Created Private Key class
class PrivateKey(object):
    def __init__(self, p, q, n):
        self.l = lcm(p-1,q-1) 
        self.m = gmpy2.invert(self.l, n)
    def __repr__(self):
        return '<PrivateKey: %s %s>' % (self.l, self.m)

#Created Public Key class
class PublicKey(object):

    @classmethod
    def from_n(cls, n):
        return cls(n)
    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1
    def __repr__(self):
        return '<PublicKey: %s>' % self.n

#Fucntion to generate 2 prime numbers p and q and return Private and Public key
#Also returns the product of p and q
def generate_keypair(bits):
    p_equal_q = True
    while p_equal_q:
        p = getPrime(bits // 2)
        q = getPrime(bits // 2)
        if (p!=q):
            p_equal_q = False
    n = p * q
    return PrivateKey(p, q, n), PublicKey(n), n

#Function for Encryption of plaintext, ciphertext created here
def encrypt(pub, plain):
    one = gmpy2.mpz(1)
    state = gmpy2.random_state(int_time())
    r = gmpy2.mpz_random(state,pub.n)
    while gmpy2.gcd(r,pub.n) != one:
        state = gmpy2.random_state(int_time())
        r = gmpy2.mpz_random(state,pub.n)
    x = gmpy2.powmod(r,pub.n,pub.n_sq)
    cipher = gmpy2.f_mod(gmpy2.mul(gmpy2.powmod(pub.g,plain,pub.n_sq),x),pub.n_sq)
    return cipher

#Function for Encryption of ciphertext, plaintext created here
def decrypt(priv, pub, cipher):
    one = gmpy2.mpz(1)
    x = gmpy2.sub(gmpy2.powmod(cipher,priv.l,pub.n_sq),one)
    plain = gmpy2.f_mod(gmpy2.mul(gmpy2.f_div(x,pub.n),priv.m),pub.n)
    if plain >= gmpy2.f_div(pub.n,2):
        plain = plain - pub.n
    return plain

def main():
    x = generate_keypair(1024)
    pub = x[1]
    priv = x[0]
    plain = int(input("Enter first Message: "))
    plain2 = int(input("Enter second Message: "))
    cipher1 = encrypt(pub, plain)
    cipher2 = encrypt(pub, plain2)
    total = cipher1*cipher2
    power = cipher1**plain2
    print("")
    print("="*100)
    print("")
    print("Cipher1: ",cipher1)
    print("")
    print("Decrypted1: ",decrypt(priv, pub, cipher1))
    print("")
    print("="*100)
    print("")
    print("Cipher2: ",cipher2)
    print("")
    print("Decrypted2: ",decrypt(priv, pub, cipher2))
    print("")
    print("="*100)
    print("ADDITIVE PROPERTY: ",decrypt(priv, pub, total))
    print("Addition of the 2 plaintext: ",plain+plain2)
    print("MULTIPLICATIVE PROPERTY: ",decrypt(priv, pub, power))
    print("Multiplication of the 2 plaintext: ",plain*plain2)
    print("="*100)

main()


