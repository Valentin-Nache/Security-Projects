sbox = (
    ('63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'),
    ('ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '90', 'a4', '72', 'c0'),
    ('b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'),
    ('04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'),
    ('09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', 'af', '84'),
    ('53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'),
    ('d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'),
    ('51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'),
    ('cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'),
    ('60', '81', '47', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'),
    ('e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'),
    ('e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'),
    ('ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'),
    ('70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'),
    ('e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'),
    ('8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16')
)

rcon = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10,
        0x20, 0x40, 0x80, 0x1b, 0x36]


def keyExpansion(key, w):
    # Fill first four keywords based on the key
    for i in range(4):
        w[i] = [key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]]

    # Generate the rest of the keywords
    for i in range(4, 44):
        temp = w[i - 1]

        if i % 4 == 0:
            temp = SubWord(RotWord(temp))
            temp[0] = temp[0] ^ rcon[i//4]

        temp_word = [0, 0, 0, 0]
        for x in range(4):
            temp_word[x] = w[i-4][x] ^ temp[x]
        w[i] = temp_word
    return w

# Rotates the input word one position to the left
def RotWord(word):
    return word[1:] + word[:1]

# Return corresponding sbox value
def SubWord(word):
    sWord = []
    for i in range(4):
        word_as_hex = hex(word[i])
        if len(word_as_hex) == 3:
            word_as_hex = word_as_hex[:2] + "0" + word_as_hex[2:]
        new_value = sbox[int(word_as_hex[2], 16)][int(word_as_hex[3], 16)]
        sWord.append(int(new_value, 16))

    return sWord


# Predetermined key
key = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59, 0x0c, 0xb7, 0xad, 0xd6, 0xaf, 0x7f, 0x67, 0x98]

w = [[]] * 44   # Hold 44 keywords

w_out = keyExpansion(key, w)    # expand key

# Print out the keywords generated
for index, word in enumerate(w_out):
    print("Word", index + 1, ": ", end="")
    print("{:02x}".format(word[0]),
          "{:02x}".format(word[1]),
          "{:02x}".format(word[2]),
          "{:02x}".format(word[3]))

input("Insert any character to exit: ")
