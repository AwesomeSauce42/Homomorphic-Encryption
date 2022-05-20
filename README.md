# Homomorphic Encryption
Homomorphic encryption is a form of encryption that permits users to perform computations on its encrypted data without first decrypting it.
In this project, I have used a Partially Homomorphic Encryption Algorithm called Paillier's Cryptosystem Algorithm. It works as following:

## Public key encryption scheme
### The basic public key encryption scheme has three stages:
    1. Generate a public-private key pair
    2. Encrypt a number
    3. Decrypt a number

## Helper functions:
    1. gcd(a,b) outputs the greatest common divisor of a and b.
    2. lcm(a,b) outputs the least common multiple of a and b.

## Key generation
### Key generation works as follows:
    1. Pick two large prime numbers p and q, randomly and independently. Confirm that gcd(pq,(p−1)(q−1)) is 1. If not, start again.
    2. Compute n=pq.
    3. Define function L(x)=x−1n.
    4. Compute λ as lcm(p−1,q−1).
    5. Pick a random integer g in the set Z∗n2 (integers between 1 and n2).
    6. Calculate the modular multiplicative inverse μ=(L(gλmodn2))−1modn. If μ does not exist, start again from step 1.
    7. The public key is (n,g). Use this for encryption.
    8.The private key is λ. Use this for decryption.

## Encryption
### Encryption can work for any m in the range 0≤m<n:
    1. Pick a random number r in the range 0<r<n.
    2. Compute ciphertext c=gm⋅rnmodn2.
    
## Decryption
### Decryption presupposes a ciphertext created by the above encryption process, so that c is in the range 0<c<n2:
    1. Compute the plaintext m=L(cλmodn2)⋅μmodn. 
(Reminder: we can always recalculate μ from λ and the public key).

### This scheme allows two types of computation:
    1. Addition of two ciphertexts
    2. Multiplication of a ciphertext by a plaintext number

_______________________________

To implement this code in Python, We need the following modules:
math, random, sys, gympy2, time, Crypto.Util.number, numpy




