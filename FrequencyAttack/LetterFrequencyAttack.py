# Letter frequency attack
def letter_attack(ciphertext, attempts):

    # English letter frequency list, ordered by most frequent to least frequent
    english_freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U',
                    'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

    # Get the length of the ciphertext
    ciphertext_length = len(ciphertext)

    # Initialize a list to store the frequency of each letter in the ciphertext
    freq_cipher = [0] * 26

    # Count the frequency of each letter in the ciphertext
    for i in range(ciphertext_length):
        freq_cipher[ord(ciphertext[i]) - 65] += 1

    # Sort the frequency list in descending order
    freq_sorted = freq_cipher.copy()
    freq_sorted.sort(reverse=True)

    for i in range(attempts):
        # Store this iteration's solution
        text = ""
        # Find the index of the most common letter in the ciphertext
        for j in range(26):
            if freq_sorted[i] == freq_cipher[j]:
                target = j
                break

        # Calculate the shift needed
        shift = ord(english_freq[i]) - 65 - target

        # Decode the ciphertext
        for letter in ciphertext:

            # Shift the letter
            new_letter = ord(letter) - 65
            new_letter += shift

            # Handle wrap-around
            if new_letter < 0:
                new_letter += 26
            if new_letter > 25:
                new_letter -= 26

            # Add the decoded letter to the solution
            text += chr(new_letter + 65)

        print("Attempt:", i, text)


# Test the function with a sample ciphertext
ciphertext = "JVKXJBFPSXIBKQFKXKAQEFPFPQEBIBQQBOCOBNRBKZVXQQXZHMOLDOXJQEXQFPMXOQLCJVXPPFDKJBKQCLOXASXKZBAPBZROFQV"
# Get the number of attempts from the user
attempts = int(input("Please enter how many attempts the program should make: "))

# Maximum number of attempts possible is 26, Minimum is 1
if attempts > 26:
    attempts = 26
if attempts < 1:
    attempts = 1

letter_attack(ciphertext, attempts)

input("Insert any character to exit: ")
