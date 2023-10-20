menu_input = 0  #Used to select what the user wants to do
text = ""       #Will hold the plain text
cypher = ""     #Will hold the ciphertext
key = 0         #Will hold the key

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

    #Encrypt
    if menu_input == 1:
        text = input("Please enter the text to be encrypted:\n")
        text = text.upper()     #for uniformity

        key = int(input("Please enter the key:\n"))
        key = key % 26      #Key should be up to 25

        for i in text:
            if i == ' ':
                cypher += ' '
                continue
            temp = ord(i) + key                         #Decide on new letter to be used
            if temp > ord('Z'):                         #If the letter goes past Z
                temp = (temp % ord('Z')) + ord('A')     #Start again at A and add the remainder

            cypher += chr(temp)

        print("Your cypher text is:" + cypher)

    #Decrypt
    if menu_input == 2:
        text = input("Please enter the text to be decrypted:\n")
        text = text.upper()

        key = int(input("Please enter the key:\n"))
        key = key % 26

        for i in text:
            if i == ' ':
                cypher += ' '
                continue
            temp = ord(i) - key                         #Decide on new letter to be used
            if temp < ord('A'):                         #If the letter goes under A
                temp = ord('Z') - (ord('A') - temp)     #Start again at Z and substract the remainder

            cypher += chr(temp)

        print("Your plain text is:" + cypher)

    # if not exiting reset the variables
    if menu_input != 3:
        menu_input = 0
        cypher = ""
