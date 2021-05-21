"""
Author: Rahul Sarkar
Licenced Under GPL 2.0

Program Based On Caesar Cipher Algorithm To Encrypt And Decrypt Any Given String. The Program Is Not Meant For Any Sort
Of Professional Use Unless Modified To An Appropriate Extent.

Accuracy: Precision Starts Falling Substantially Beyond 500000 Encryption Level/Encryption Key
Known Bug: Single Quote (') Does Cause Trouble When (Copy+Paste)d Directly From Other Text Source.
"""
LETTERREPO = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "<", ",", ">", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "<", ",", ">", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "<", ",", ">", ".", "?", "/","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def encrypt(text, step=7):
    """ Function To Generate A List Out Of User Input  (As Plain Text String To Encrypt i.e. textinput & encryptiolevel)
    ---> Leit Elements Are Mapped With The LETTERREPO To Generate Encryption Using The "levelcalculation()"
    --> Concatenated Into String As An Output"""

    indexlist = []
    steppedindexlist = []
    encryptedstring = ""
    listtextinput = list(textInput)

    for chars in listtextinput:
        indexcontainer = LETTERREPO.index(chars)
        indexlist.append(indexcontainer + encryptvalue)

    # List Encryption

    for encText in indexlist:
        steppedindexlist.append(LETTERREPO[encText])

    for encelements in steppedindexlist:
        encryptedstring += str(encelements)

    print("*" * 75)
    print(f"The Encrypted String Is: " + "\""+encryptedstring+"\"")
    print("*" * 75)
    print("Please Copy The Text (Within Or Excluding) The Extreme End Double Quotes (\"___\").")
    print("*" * 75)


def decrypt(text, step=7):
    """ Function To Generate A List Out Of User Input  (As Encrypted String To Decrypt i.e. textinput & encryptiolevel)
    ---> List Elements Are Mapped With The LETTERREPO To Generate Decryption Using The "levelcalculation()"
    --> Concatenated Into String As An Output"""

    indexlist = []
    steppedindexlist = []
    decryptedstring = ""
    listtextinput = list(textInput)
    # print(listTextInput)
    for chars in listtextinput:
        indexcontainer = LETTERREPO.index(chars)
        indexlist.append(indexcontainer - decryptvalue)

    # List Decryption

    for encText in indexlist:
        steppedindexlist.append(LETTERREPO[encText])

    for encelements in steppedindexlist:
        decryptedstring += str(encelements)

    print("*" * 75)
    print("The Decrypted String Is: "+"\""+decryptedstring+"\"")
    print("*" * 75)
    print("Please Copy The Text (Within Or Excluding) The Extreme End Double Quotes (\"___\").")
    print("*" * 75)


def levelcalculation(cryptlevel):
    """Method Used For Encryption Level Calculation"""

    conditionbreak = True
    approxresultantlevel = encryptionlevel // 163
    while conditionbreak:
        approxresultantlevel //= 163
        if approxresultantlevel <= 163:
            conditionbreak = False

    if encryptionlevel % 157 != 0:
        remresultantlevel = encryptionlevel % 157
    else:
        remresultantlevel = 7
    resultantlevel = approxresultantlevel + remresultantlevel
    return resultantlevel


# Main Function Body Starts Here


print("*"*100)
print("\n")

print("*" * 75)
print("A Program To Encrypt And Decrypt Your Message.")
print("*" * 75)
print("\n")


# print(listUserInput)
print("Would You Like To Encrypt Or Decrypt ?")
userInput = input("Type (e/E/Encrypt/encrypt) Or (d/D/decrypt/Decrypt): ").lower()
if userInput == "encrypt" or userInput == "e":

    conditioncheck = True
    while conditioncheck:
        try:
            encryptionlevel = int(input("Enter The Encryption Level (Type An Integer): "))
            print("""\nPlease Note! Encryption Level Will Be Used As An Encryption Key, 
So Take A Note Of Encryption Key To Decrypt The Text  In Future!""")
            print("\n")
            conditioncheck = False
        except ValueError as valerr:
            print("Invalid Input! Please Try An Integer...! ", valerr)
            continue
        except:
            print("Invalid Input! Please Try An Integer...!")
            continue
    print("*" * 75)

    inputcheckenc = True
    while inputcheckenc:
        try:
            textInput = input("Enter The Text That You Want To Encrypt: ")
            inputcheckenc = False
        except ValueError:
            print("Please Remove Unconventional Special Characters From The Text And Try Again!")
            continue
        except:
            print("Please Remove Unnecessary Special Characters!")

    print("*" * 75)
    encryptvalue = levelcalculation(encryptionlevel)
    encrypt(textInput, encryptvalue)

elif userInput == "decrypt" or userInput == "d":

    conditioncheck = True
    while conditioncheck:
        try:
            encryptionlevel = int(input("Enter The Decryption Level (Type An Integer): "))
            print("\n")
            conditioncheck = False
        except ValueError as valerr:
            print("Invalid Input! Please Try An Integer...! ", valerr)
            continue
        except:
            print("Invalid Input! Please Try An Integer...!")
            continue

    print("*" * 75)
    # textInput = input("Enter The Text That You Want To Decrypt: ")
    inputcheckdec = True
    while inputcheckdec:
        try:
            textInput = input("Enter The Text That You Want To Encrypt: ")
            inputcheckdec = False
        except ValueError:
            print("Encryption String Corrupted, Try Removing Non-Keyboard Special Characters, If Any!")
            continue
        except:
            print("Corrupt Encryption String!")
            continue

    print("*" * 75)
    decryptvalue = levelcalculation(encryptionlevel)
    decrypt(textInput, decryptvalue)

else:
    print("\nInvalid Input! Terminating Program...!")
