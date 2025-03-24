from Crypto.Util import number
import math
import random


#Generate p and q
bits=512 
p= number.getPrime(bits)
q= number.getPrime(bits)

#Compute n
n = p*q

#Compute φ(n)
phi = (p-1)*(q-1)

#Generate e with 1 < e < φ(n) and GCD(e, φ(n)) = 1


e= 65537
if math.gcd(e, phi) != 1:
    while True:
        e = number.getPrime(16)
        if math.gcd(e, phi) ==1:
            break
            

#Compute d such that (d * e) mod φ(n) = 1
d = number.inverse(e, phi)

#Display the keys
print(f" PUBLIC KEY (n, e) \nn = {n}\ne = {e}\n")
print(f" PRIVATE KEY (n, d) \nn = {n}\nd = {d}")

#Message to encrypt and decrypt
message= input("Enter the message to encrypt: ")

m= int.from_bytes(message, 'big')
print(f"m:{m}")

#Encrypt: c = m^e mod n
c = pow(m,e,n)

print(f"Encrypted Message in integer form:\n{c}")

#Decrypt: m = c^d mod n
cc = pow(c,d,n)

decrypted_message = cc.to_bytes((cc.bit_length() + 7) // 8, 'big')

print("\nDecrypted Message:")
print(decrypted_message.decode('utf-8'))
