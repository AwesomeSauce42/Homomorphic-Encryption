import random
import sys
import math
from Gen_prime import *
from Crypto.Util import number


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''
Tests to see if a number is prime.
'''


def generate_key_pair(p, q):
    
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choosing an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Using Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Using Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Returning public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    #Unpacking the key into it's components
    key, n = pk
    #Converting each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = pow(plaintext,key,n)
    #Returning the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpacking the key into its components
    key, n = pk
    #Generating the plaintext based on the ciphertext and key using a^b mod m
    plain = pow(ciphertext,key,n)
    #Returning the array of bytes as a string
    return plain


def main():
    '''
    Detect if the script is being run directly by the user
    '''
    print("===========================================================================================================")
    print("================================== RSA Encryptor / Decrypter ==============================================")
    print(" ")

    n_length = 4

    p = generateLargePrime(1024)
    q = generateLargePrime(1024)

    while(p==q):
        q = generateLargePrime(1024)
    print(p)
    print(q)
    
    print(" - Generating your public / private key-pairs now . . .")

    public, private = generate_key_pair(p, q)

    print(" - Your public key is ", public, " and your private key is ", private)

    message1 = int(input(" - Enter a message 1 to encrypt with your public key: "))
    message2 = int(input(" - Enter a message 2 to encrypt with your public key: "))

    encrypted_msg1 = encrypt(public, message1)
    encrypted_msg2 = encrypt(public, message2)
    total = encrypted_msg1+encrypted_msg2
    total_sum = encrypt(public, total)
    actual_product = encrypted_msg1*encrypted_msg2
    product = encrypt(public, actual_product)

    print(" - Your encrypted message 1 is: ", encrypted_msg1)
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, encrypted_msg1))

    print(" - Your encrypted message 2 is: ", encrypted_msg2)
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, encrypted_msg2))

    print(" - Your encrypted message sum is: ",total_sum)
    print(" - Your sum decryption is: ", decrypt(private, total_sum))
    print(" - Sum of messages is: ",message1+message2)


    print(" - Your encrypted message product is: ",product)
    print(" - Your product decryption is: ", decrypt(private, product))
    print(" - Product of messages is: ",message1*message2)

    print(" ")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")


main()
