# BFV SCHEME
Simple Python implementation of Brakerski/Fan-Vercauteren (BFV) homomorphic encryption scheme following the definitions in the [paper](https://eprint.iacr.org/2012/144.pdf).

The Fan-Vercauteren (FV) scheme, (also known as the Brakerski-Fan-Vercauteren (BFV) scheme) is considered as one of the second generation of FHE schemes that is constructed based on the Ring-Learning with Errors (RLWE) problem [LPR13]. BFV is instantiated over two rings: 1) the plaintext ring which includes encodings of unencrypted or intelligible messages and 2) the ciphertext ring which includes encrypted messages. Similar to any other FHE scheme, BFV allows an untrusted party to induce meaningful computation over encrypted data without access to the decryption key. This is possible due to the homomorphism property which offers a map (or function) between the plaintext and ciphertext spaces that preserves the operations in these two spaces.

### More info: [Link](https://inferati.com/blog/fhe-schemes-bfv).

The main program to run is BFV_FHE.py .
This code takes in 2 integer messages form the users and encrypts them, and also shows us the Homomorphic properties of the encrypted data (ciphertext)

 Rest of the files are used as libraries (modules).
