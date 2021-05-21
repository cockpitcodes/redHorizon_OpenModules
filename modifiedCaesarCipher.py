"""
Author: Rahul Sarkar
Licenced Under GPL 2.0

Program Based On Caesar Cipher Algorithm To Encrypt And Decrypt Any Given String. The Program Is Not Meant For Any Sort
Of Professional Use Unless Modified To An Appropriate Extent.
"""

# LETTERREPO = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "|", "\\", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", ":", ";", "+", " ", ".", "~", "`", "-", "_", "*", "/", "=", "\"", "\'", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\\", "|", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", ":", ";", "+", " ", ".", "~", "`", "-", "_", "*", "/", "=", "\"", "\'", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\\", "|", ",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", ":", ";", "+", " ", ".", "~", "`", "-", "_", "*", "/", "=", "\"", "\'"]
LETTERREPO = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "<", ",", ">", ".", "?", "/","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "< ", ",", ">", ".", "?", "/","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "< ", ",", ">", ".", "?", "/","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encrypt(text, step):
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
    print(f"The \"Encrypted\" String Is: " + "\""+encryptedstring+"\"")
    print("*" * 75)
    print("Copy The String/Text Within/Excluding The Double Quotes (\").")
    print("*" * 75)


def decrypt(text, step):
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

    print("*"* 75)
    print("The \"Decrypted\" String Is: "+"\""+decryptedstring+"\"")
    print("*" * 75)
    print("Copy The Text (Within/Excluding) The Double Quotes (\").")
    print("*" * 75)


def levelcalculation(cryptlevel):
    conditionbreak = True
    approxresultantlevel = encryptionlevel // 160
    while conditionbreak:
        approxresultantlevel //= 160
        if approxresultantlevel < 25:
            conditionbreak = False

    remresultantlevel = encryptionlevel % 25
    resultantlevel = approxresultantlevel + remresultantlevel
    return resultantlevel


# Main Function Body Starts Here


print("*"*100)
print("\n")

print("*"* 75)
print("A Program To Encrypt And Decrypt Your Message.")
print("*"* 75)
print("\n")


# print(listUserInput)
userInput = input("Would You Like To Encrypt Or Decrypt, Type (e/E/Encrypt/encrypt) Or (d/D/decrypt/Decrypt): ").lower()
if userInput == "encrypt" or userInput == "e":

    conditioncheck = True
    while conditioncheck:
        try:
            encryptionlevel = int(input("Enter The Encryption Level (Type An Integer): "))
            print("\n")
            conditioncheck = False
        except ValueError as valerr:
            print("Invalid Input! Please Try An Integer...! ", valerr)
            continue
        except:
            print("Invalid Input! Please Try An Integer...!")
            continue
    print("*" * 75)
    textInput = input("Enter The Text That You Want To Encrypt: ")
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
    textInput = input("Enter The Text That You Want To Decrypt: ")
    print("*" * 75)
    decryptvalue = levelcalculation(encryptionlevel)
    decrypt(textInput, decryptvalue)

else:
    print("\nInvalid Input! Terminating Program...!")
