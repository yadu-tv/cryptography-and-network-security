from math import sqrt
from secrets import choice
from secrets import token_hex

def is_prime(number:int) -> bool:
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number < 2:
        return False
    
    for current_number in range(3 , int(sqrt(number)) + 1, 2):
        if number % current_number == 0:
            return False
    return True

def generate_prime_number(min_value=0, max_value=300):
    primes = [number for number in range(min_value,max_value) if is_prime(number)]
    return choice(primes)

def save(p:int, g:int, a:int, b:int, A:int, B:int, a_s:int, b_s:int, path:str="exchange.txt"):
    print(f"Prime(p) and base(g):\n\tp = {p}\n\tg = {g}\n\n")
    print(f"Alice and bob's private key (a and b respectively):\n\ta = {a}\n\tb = {b}\n\n")
    print(f"Alice and Bob's public key and exchange (A and B respectively): \n\tA = g^a mod p = {A}\n\tB = g^b mod p = {B}\n\n")
    print(f"Alice and Bob calculate common secret key for encryption: \n\tAlice's Calculation: \n\t\ts = B^a mod p = {a_s} \n\tBob's Calculation: \n\t\ts = A^b mod p = {b_s}")

if __name__ == "__main__":
    shared_prime = generate_prime_number() # p value
    shared_base = int(token_hex(2), 16) # g value
    alice_secret = int(token_hex(2), 16)
    bob_secret = int(token_hex(2), 16)
    # a value
    # b value
    # Public key generation & exchange
    alice_public = (shared_base ** alice_secret) % shared_prime
    bob_public = (shared_base ** bob_secret) % shared_prime
    # Common Secret Calculation
    alice_calculated_secret = (bob_public ** alice_secret) % shared_prime
    bob_calculated_secret = (alice_public ** bob_secret) % shared_prime
    save(shared_prime, shared_base, alice_secret, bob_secret, alice_public, bob_public,
    alice_calculated_secret, bob_calculated_secret)