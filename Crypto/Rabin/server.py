
from sympy import isprime
from Crypto.Util.number import *

def rabin_encrypt(plaintext, p, q):

    n = p * q
    ciphertext = pow(plaintext, 2, n)
    return ciphertext

p = "SECRET"
q = "SECRET"
plaintext = b'ckcscCTF{Fake_Flag}'
plaintext = bytes_to_long(plaintext)
ciphertext = rabin_encrypt(plaintext, p, q)

print("c=", ciphertext)
print("p=", p)
print("q=", q)
print("n=", p * q)
