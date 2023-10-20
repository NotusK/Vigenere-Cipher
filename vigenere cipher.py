// IDK if it's allowed to work at original vigenere cipher, So to be sure I work on Autokey vigerene cipher instead

def encrypt(text, key):
    encrypted_text = ""

    for i in range(len(text)):
        char = text[i]

        if char.isalpha():
            shift = ord(key[i].upper()) - ord('A')
            encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""

    for i in range(len(encrypted_text)):
        encrypted_char = encrypted_text[i]

        shift = ord(key[i].upper()) - ord('A')
        decrypted_char = chr((ord(encrypted_char.upper()) - ord('A') - shift) % 26 + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text
    
while(True):
    choice = int(input("Ketik Pilihan Anda:\n1.Untuk Encrypt \n2.Untuk Decrypt \n3.Untuk Exit \nInput: "))
    if(choice == 1):
        text = input("Masukan Teks: ")
        while True:
            key = input("Masukan Kunci (Panjang kunci harus lebih dari atau sama dengan teks, panjang teks = {}): ".format(len(text)))
            if len(key) >= len(text):
                break
            else:
                print("Jumlah Karakter Kunci Terlalu Sedikit!!")

        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text, "\n")

    elif(choice == 2):
        text = input("Masukan Teks Yang Terenkripsi: ")
        while True:
            key = input("Masukan Kunci (Panjang kunci harus lebih dari atau sama dengan teks, panjang teks = {}): ".format(len(text)))
            if len(key) >= len(text):
                break
            else:
                print("Jumlah Karakter Kunci Terlalu Sedikit!!")

        decrypted_text = decrypt(text, key)
        print("Decrypted text:", decrypted_text, "\n")

    else:
        print("Exiting Program")
        break
    

    


