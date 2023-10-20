import math

cipher = ""     # will hold the ciphertext

text = input("Please enter the text to be encrypted:\n").upper()

# If text is uneven pad it with an X at the end
if len(text) % 2 != 0:
    text += 'X'

key = input("Please enter the encryption key (4 LETTERS):\n").upper()

i = 0

while i < len(text):

    # Convert each key letter to appropriate number
    key_pos_0 = ord(key[0]) % ord('A')
    key_pos_1 = ord(key[1]) % ord('A')
    key_pos_2 = ord(key[2]) % ord('A')
    key_pos_3 = ord(key[3]) % ord('A')

    # Convert the text letters to appropriate number
    txt_1 = ord(text[i]) % ord('A')
    txt_2 = ord(text[i+1]) % ord('A')

    # Find letter 1 and convert to relevant ascii value
    letter1 = ((txt_1 * key_pos_0 +
                txt_2 * key_pos_1) % 26) + ord('A')

    # Find letter 2 and convert to relevant ascii value
    letter2 = ((txt_1 * key_pos_2 +
                txt_2 * key_pos_3) % 26) + ord('A')

    # Add letters to cipher
    cipher = cipher + chr(letter1) + chr(letter2)

    # Move on to the next 2 letters in the plaintext
    i += 2

print("Cipher text is: " + cipher)