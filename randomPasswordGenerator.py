import random

print("*"*100)
print("\n")

# User Inputs

inputcondition = True
while inputcondition:
    try:
        letters = int(input("Enter The Number Of Letters You Want To Have In Your Password: "))
        numbers = int(input("How Many Numbers Would You Want To Attach In Your Password: "))
        specialCharacters = int(input("How Many Special Characters You Want In Your Password: "))
        inputcondition = False
    except ValueError as valerr:
        print("Only Integer Values Are Expected!", valerr)
        continue
    except:
        print("Only Integer Values Are Expected!")
        continue

# Password Character Repository

letterRepo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V","W", "X", "Y", "Z"]
numbersRepo = ["0", "1", "2", "3", "4," "5", "6", "7", "8", "9"]
specialCharactersRepo = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "+"]

charMix = []

# User Input Letters, Numbers & Special Characters Iteration To Randomize List Index And Append It To The List "charMix"

for i in range(0, letters):
    randomLetters = random.randint(0, (len(letterRepo) - 1))
    charMix.append(letterRepo[randomLetters])
for j in range(0, numbers):
    randomNumbers = random.randint(0, (len(numbersRepo) - 1))
    charMix.append(numbersRepo[randomNumbers])
for k in range(0, specialCharacters):
    randomSpecialCharacters = random.randint(0, (len(specialCharactersRepo) - 1))
    charMix.append(specialCharactersRepo[randomSpecialCharacters])

# print(charMix)

# Containment And String Generation Of The Generated List

charMass = random.sample(charMix, len(charMix))
passString = ""

for setString in charMass:
    passString += setString

# Output Formatting

print("\n")
print("*" * 75)
print(f"Your Randomized Password Is: "+"\""+passString+"\"")
print("Please Copy The Text (Within Or Excluding) The Extreme End Double Quotes(\"___\")")
print("*" * 75)
