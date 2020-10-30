from random import randint

Alphabet = "abcdefghijklmnopqrstuvwxyz"

#mehrere Textdateien mit zufälligen Nummern generieren
#generate_otp( , )
def generate_otp(sheets,length):
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt","w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")
                
#aufrufen einer Textdatei
#sheet = load_sheet("otp .txt")
#print(sheet)
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

#Input der Nachricht + alles in Kleinbuchstaben konvertieren
def get_plaintext():
    plaintext = input("Geben sie ihre Nachricht ein: ")
    return plaintext.lower()

#Nachricht öffne
def load_file(filename):
    with open(filename,"r") as f:
        contents = f.read()
    return contents

#Nachricht speichern
def save_file(filename,data):
    with open(filename, "w") as f:
        f.write(data)
        
#Text einzeln mit Zahlenblatt verschlüsseln
#sheet = load_sheet("otp .txt")
#ciphertext = encrypt(" ... ", sheet)
#ciphertext
def encrypt(plaintext,sheet):
    ciphertext = ""
    for position, character in enumerate(plaintext):
        if character not in Alphabet:
            ciphertext += character
        else:
            encrypted = (Alphabet.index(character) + int(sheet[position])) %26
            ciphertext += Alphabet[encrypted]
    return ciphertext

#Text entschlüsseln
#decrypt(ciphertext,sheet)
def decrypt(ciphertext,sheet):
    plaintext = ""
    for position, character in enumerate(ciphertext):
        if character not in Alphabet:
            plaintext += character
        else:
            decrypted = (Alphabet.index(character) - int(sheet[position])) % 26
            plaintext += Alphabet[decrypted]
    return plaintext

#Menü mit Auswahlmöglichkeit der einzelnen Funktionen zur leichteren Bedienung
def menu():
    choices = ["1","2","3","4"]
    choice = "0"
    while True:
        while choice not in choices:
            print("What would you like to do?")
            print("1. Generate one-time pads")
            print("2. Encrypt a message")
            print("3. Decrypt a message")
            print("4. Quit the program")
            choice = input("Please type 1, 2, 3 or 4 and press Enter: ")
        
            if choice == "1":
                sheets = int(input("How many one-time pads would you like to generate? "))
                length = int(input("What will be your maximum message length? "))
                generate_otp(sheets, length)
            
            elif choice == "2":
                filename = "otp" + input("Type in the number of the OTP you want to use ") + ".txt"
                sheet = load_sheet(filename)
                plaintext = get_plaintext()
                ciphertext = encrypt(plaintext, sheet)
                filename = input("What will be the name of the encrypted file? ") + ".txt"
                save_file(filename, ciphertext)
                
            elif choice == "3":
                filename = "otp" + input("Type in the number of the OTP you want to use ") + ".txt"
                sheet = load_sheet(filename)
                filename = input("Type in the name of the file to be decrypted ") + ".txt"
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print("The message reads:")
                print("")
                print(plaintext)
                print("")
                
            elif choice == "4":
                exit()
            
            choice = "0"
            
menu()
