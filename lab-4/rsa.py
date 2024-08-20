import random

# Function to check if a number is prime
def is_prime(num):
    if num in (2, 3):
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Function to generate a random prime number
def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Ensure it is of the required bit length and odd
    return p

def generate_large_prime(length=1024):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

# Function to compute the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse
def mod_inverse(e, phi):
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 != 1:
        q = x3 // y3
        y1, y2, y3, x1, x2, x3 = (x1 - q * y1), (x2 - q * y2), (x3 - q * y3), y1, y2, y3
    return y2 % phi

# RSA Key generation
def generate_rsa_keys(bit_length=1024):
    p = generate_large_prime(bit_length)
    q = generate_large_prime(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate d
    d = mod_inverse(e, phi)

    # Public and Private keys
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Function to encrypt the message
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    print("E and N values to encrypt the message: ", e, n)
    encrypted_message = [pow(ord(char), e, n) for char in plaintext]
    return encrypted_message

# Function to decrypt the message
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    print("D and N values to decrypt the message: ", d, n)
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

# Example usage
bit_length = 16  # Use a small bit length for demonstration purposes
public_key, private_key = generate_rsa_keys(bit_length)

message = "Hi"
print(f"Original message: {message}")

# Encryption
encrypted_msg = rsa_encrypt(message, public_key)
print(f"Encrypted message: {encrypted_msg}")

# Decryption
decrypted_msg = rsa_decrypt(encrypted_msg, private_key)
print(f"Decrypted message: {decrypted_msg}")
