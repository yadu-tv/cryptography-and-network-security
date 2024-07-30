def generate_playfair_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = []
    used_chars = set()
    
    for char in key.upper():
        if char not in used_chars and char in alphabet:
            used_chars.add(char)
            key_matrix.append(char)
    
    for char in alphabet:
        if char not in used_chars:
            key_matrix.append(char)
    
    return [key_matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_cipher(text, key):
    matrix = generate_playfair_key_matrix(key)
    text = text.upper().replace("J", "I")
    text_pairs = []
    
    # Create pairs of letters
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
            if char1 == char2:
                text_pairs.append(char1 + 'X')
                i += 1
            else:
                text_pairs.append(char1 + char2)
                i += 2
        else:
            text_pairs.append(char1 + 'X')
            i += 1
    
    # Encrypt each pair
    result = ""
    for pair in text_pairs:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    
    return result

plaintext = "HELLO"
key = "KEYWORD"
ciphertext = playfair_cipher(plaintext, key)
print("Ciphertext:", ciphertext)