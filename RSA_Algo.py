import random
import sys
import math
from Gen_prime import *
from Crypto.Util import number



#Calculate GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


#Calculate Multiplicative inverse
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




#Generate Public and Private keys
def generate_key_pair(p, q):
    
    n = p*q
    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

#Generating ciphertext (Encryption)
def encrypt(pk, plaintext):
    key, n = pk
    cipher = pow(plaintext,key,n)
    return cipher

#Generating plaintext (Decryption)
def decrypt(pk, ciphertext):
    key, n = pk
    plain = pow(ciphertext,key,n)
    return plain


def main():

    print("====== RSA Encryptor / Decrypter ======")
    print(" ")

    while True:
        try:
            p = generateLargePrime(10)
            q = generateLargePrime(10)
        except TypeError: 
            continue
        else:
            break


    while(p==q):
        q = generateLargePrime(10)


    n = p*q
    

    public, private = generate_key_pair(p, q)

    print(" - P is: ",p)
    print(" - Q is: ",q)
    print(" - N is: ",n)

    print(" - Public key is: ", public)
    print(" - Private key is ", private)

    message1 = int(input(" - Enter a message 1 to encrypt with your public key: "))
    message2 = int(input(" - Enter a message 2 to encrypt with your public key: "))

    actual_product = message1*message2

    encrypted_msg1 = encrypt(public, message1)
    encrypted_msg2 = encrypt(public, message2)
    encrypted_msg3 = encrypt(public, actual_product) #RHS

    product = encrypted_msg1*encrypted_msg2 #LHS

    decrypted_msg1 = decrypt(private, encrypted_msg1)
    decrypted_msg2 = decrypt(private, encrypted_msg2)
    decrypted_msg3 = decrypt(private, product)

    print(" - Your encrypted message 1 is: ", encrypted_msg1)
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypted_msg1)

    print(" - Your encrypted message 2 is: ", encrypted_msg2)
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypted_msg2)

    print("="*50)

    print(" - Your message is (decrypted from product of ciphertext): ", decrypted_msg3)
    print(" - YOur message product is: ",message1*message2)
    if(decrypted_msg3 == message1*message2):
        print(" - Homomorphic Multiplication Works!")
    
    else:
        print(" - Homomorphic Multiplication Doesnt Work.")

    print("====================== END =======================")


main()
