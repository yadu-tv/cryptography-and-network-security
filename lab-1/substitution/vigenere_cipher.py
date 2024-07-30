def vigenere_cipher(text, keyword):
    result = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0
    
    for char in text:
        if char.isalpha():
            shift_amount = ord(keyword[keyword_index]) - ord('A')
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            keyword_index = (keyword_index + 1) % keyword_length
        else:
            result += char
    return result

plaintext = "HELLO, WORLD!"
keyword = "KEY"
ciphertext = vigenere_cipher(plaintext, keyword)
print("Ciphertext:", ciphertext) 