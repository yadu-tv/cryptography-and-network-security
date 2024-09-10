import struct
import math

# Constants for MD5
s = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

K = [
    int(abs(math.sin(i + 1)) * (2 ** 32)) for i in range(64)
]

def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

def md5(message):
    message = bytearray(message)  # Convert to bytearray
    orig_len_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF

    # Append the bit '1' to the message
    message.append(0x80)

    # Pad with zeros until message length is 64 bytes less than a multiple of 512
    while len(message) % 64 != 56:
        message.append(0)

    # Append the original length in bits
    message += struct.pack('<Q', orig_len_bits)

    # Initialize variables
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Process the message in 512-bit chunks
    for chunk_offset in range(0, len(message), 64):
        a, b, c, d = A, B, C, D
        chunk = message[chunk_offset:chunk_offset + 64]
        M = struct.unpack('<16I', chunk)

        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Produce the final hash value (digest)
    return struct.pack('<4I', A, B, C, D).hex()

# Example usage
val = input("Enter message to be encrypted: ")
message = bytearray(val, "utf-8")
hash_result = md5(message)
print(hash_result)

