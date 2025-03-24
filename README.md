# Simple RSA Algorithm Implementation (Python)

This repository contains a basic implementation of the RSA algorithm in Python. It's designed for educational purposes to demonstrate the core concepts of RSA encryption and decryption.

**Important:**

* The key sizes and implementation are simplified for demonstration. [key size is generally 2048 bits in real-world applications]

**Code Explanation:**

The script performs the following steps:

1.  **Generates Prime Numbers (p and q):** Uses `Crypto.Util.number.getPrime()` to generate two large prime numbers.
2.  **Calculates Modulus (n):** Computes `n = p * q`.
3.  **Calculates Totient (phi):** Computes `phi = (p-1) * (q-1)`.
4.  **Chooses Public Exponent (e):** Uses a fixed value of `e = 65537`. 
5.  **Calculates Private Exponent (d):** Uses `Crypto.Util.number.inverse()` to find the modular inverse of `e` modulo `phi`.
6.  **Encrypts the Message:** Converts the message to an integer and calculates `c = m^e mod n`.
7.  **Decrypts the Message:** Calculates `m = c^d mod n` and converts it back to the original message.

**Disclaimer:**

This simplified implementation does not include padding or other security measures required for real-world applications. 
