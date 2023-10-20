menu_input = 0  #Used to select what the user wants to do
text = ""       #Will hold the plain text
cipher = ""     #Will hold the ciphertext
key = 0         #Will hold the key
key_pos = 0     #Keeps track of which letter in the key we are currently using

while menu_input != 3:
    print("choose a menu option")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    #ensure valid menu option is chosen
    while menu_input not in range(1, 4):
        menu_input = int(input())
        if menu_input not in range(1, 4):
            print("Invalid Option Please Try Again")

    #encrypt
    if menu_input == 1:
        text = input("Please enter the text to be encrypted:\n")
        text = text.upper()     #for uniformity

        key = input("Please enter the key:\n")
        key = key.upper()       #for uniformity

        for i in text:

            # if encountering blank space
            if i == ' ':
                cipher += ' '
                continue
            temp = ord(i) + (ord(key[key_pos]) % 26)        #Decide on new letter to be used
            if temp > ord('Z'):                             #If the letter goes past Z
                temp = (temp % ord('Z')) + ord('A')         #Start again at A and add the remainder

            cipher += chr(temp)
            key_pos = (key_pos + 1) % len(key)              #Move on to the next letter in the key

        print("Your cipher text is:" + cipher)

    #decrypt
    if menu_input == 2:
        text = input("Please enter the text to be decrypted:\n")
        text = text.upper()

        key = input("Please enter the key:\n")
        key = key.upper()

        for i in text:

            #if encountering blank space
            if i == ' ':
                cipher += ' '
                continue
            temp = ord(i) - (ord(key[key_pos]) % 26)        #Decide on new letter to be used
            if temp < ord('A'):                             #If the letter goes under A
                temp = ord('Z') - (ord('A') - temp)         #Start again at Z and substract the remainder

            cipher += chr(temp)
            key_pos = (key_pos + 1) % len(key)

        print("Your plain text is:" + cipher)

    #if not exiting reset the variables
    if menu_input != 3:
        menu_input = 0
        cipher = ""
        key_pos = 0
