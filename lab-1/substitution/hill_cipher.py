def row_column_transposition_encrypt(plaintext, key):
    plaintext = ''.join(plaintext.split()).upper()
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (len(plaintext) % num_cols > 0)
    
    plaintext = plaintext.ljust(num_cols * num_rows, 'X')
    
    grid = [plaintext[i:i+num_cols] for i in range(0, len(plaintext), num_cols)]
    
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    
    ciphertext = ''.join(''.join(row[i] for row in grid) for i in sorted_key_indices)
    return ciphertext

plaintext = "WE ARE DISCOVERED FLEE AT ONCE"
key = "4312567"
ciphertext = row_column_transposition_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
