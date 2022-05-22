from BFV import *
from helper import *
from random import randint
from math import log,ceil

# Generate polynomial arithmetic tables
w_table    = [1]*n
wv_table   = [1]*n
psi_table  = [1]*n
psiv_table = [1]*n
for i in range(1,n):
    w_table[i]    = ((w_table[i-1]   *w)    % q)
    wv_table[i]   = ((wv_table[i-1]  *wv)   % q)
    psi_table[i]  = ((psi_table[i-1] *psi)  % q)
    psiv_table[i] = ((psiv_table[i-1]*psiv) % q)

qnp = [w_table,wv_table,psi_table,psiv_table]

print("******Starting BFV Scheme Algo******")

# Generate BFV evaluator
Evaluator = BFV(n, q, t, mu, sigma, qnp)

# Generate Keys
Evaluator.SecretKeyGen()
Evaluator.PublicKeyGen()
Evaluator.EvalKeyGenV1(T)
Evaluator.EvalKeyGenV2(p)

# print system parameters
print(Evaluator)

#Obtain 2 messages from user

n1 = int(input("Enter Message 1: "))
n2 = int(input("Enter Message 2: "))

print("--- Random integers n1 and n2 are generated.")
print("n1: ",n1)
print("n2: ",n2)
print("n1+n2: ",n1+n2)
print("n1-n2: ",n1-n2)
print("n1*n2: ",n1*n2)
print("")

# Encode random messages into plaintext polynomials
print("--- n1 and n2 are encoded as polynomials m1(x) and m2(x).")
m1 = Evaluator.IntEncode(n1)
m2 = Evaluator.IntEncode(n2)

print("m1(x): ",m1)
print("m2(x): ",m2)
print("")

# Encryption of plaintext to ciphertext
Cipher_text1 = Evaluator.Encryption(m1)
Cipher_text2 = Evaluator.Encryption(m2)

print("--- m1 and m2 are encrypted as Cipher_text1 and Cipher_text2.")
print("Cipher_text1[0]: ",Cipher_text1[0])
print("Cipher_text1[1]: ",Cipher_text1[1])
print("Cipher_text2[0]: ",Cipher_text2[0])
print("Cipher_text2[1]: ",Cipher_text2[1])
print("")


# Homomorphic Addition
Cipher_text = Evaluator.HomomorphicAddition(Cipher_text1,Cipher_text2)
mt = Evaluator.Decryption(Cipher_text)
nr = Evaluator.IntDecode(mt) 
ne = (n1+n2) 

print("--- Performing Homomorphic Addition: ")
print("Cipher_text_add[0] :",Cipher_text[0])
print("Cipher_text_add[1] :",Cipher_text[1])
print("Decrypted    :",mt)
print("Decoded    :",nr)

if nr == ne:
    print("Homomorphic addition works.")
else:
    print("Homomorphic addition does not work.")
print("")



# Homomorphic Multiplication (relinearization v1)
Cipher_text = Evaluator.HomomorphicMultiplication(Cipher_text1,Cipher_text2)
Cipher_text = Evaluator.RelinearizationV1(Cipher_text)
mt = Evaluator.Decryption(Cipher_text)

nr = Evaluator.IntDecode(mt)
ne = (n1*n2)

print("--- Performing Homomorphic Multiplication: (with relinearization v1)")
print("Cipher_text_mul[0] :",Cipher_text[0])
print("Cipher_text_mul[1] :",Cipher_text[1])
print("Decrypted    :",mt)
print("Decoded    :",nr)

if nr == ne:
    print("Homomorphic multiplication works.")
else:
    print("Homomorphic multiplication does not work.")
print("")
print("******ENDING BFV Scheme Algo******")
