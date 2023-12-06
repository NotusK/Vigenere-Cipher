def text_to_bit(text, encoding='ascii'):
    encoded_text = text.encode(encoding)

    # Convert byte menjadi bit
    bit_result = ''.join(format(byte, '08b') for byte in encoded_text)

    return bit_result

def bit_to_text(bit_string, encoding='ascii'):
    # Split bit_string menjadi 8bit setiap bagiannya
    chunks = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]

    # Convert setiap bagian bit yang sudah dibagi menjadi string
    text_result = ''.join(chr(int(chunk, 2)) for chunk in chunks)

    return text_result

def xor_bit(message, key):
    # XOR setiap bit text dengan bit kunci
    result = ''.join(str(int(bit_msg) ^ int(bit_key)) for bit_msg, bit_key in zip(message, key))

    return result

def bit_to_hex(bit):
    # Pisah bit menjadi group of 4
    groups_of_4 = [bit[i:i + 4] for i in range(0, len(bit), 4)]

    # Convert bit menjadi bentuk hexa
    hex_result = ''.join(hex(int(group, 2))[2:] for group in groups_of_4)

    return hex_result

plaintext = input("Masukan Teks : ")
key = input("Masukan Kunci: ")

bit_plaintext = text_to_bit(plaintext)
bit_key = text_to_bit(key)

encrypted_result = xor_bit(bit_plaintext, bit_key)

text_of_encrypted_result = bit_to_hex(encrypted_result)

print("Bits dari Plaintext   :", bit_plaintext)
print("Bits dari Key         :", bit_key)
print("Hasil Enkripsi Bits   :", encrypted_result)
print("Hasil Enkripsi ke Text:", text_of_encrypted_result)

choice_decrypt = input("Decrypt? (y/n): ").lower() 

if(choice_decrypt == "y"):
    decrypted_result = xor_bit(encrypted_result, bit_key)

    decrypted_text = bit_to_text(decrypted_result)

    print("Hasil Dekripsi Bits:", decrypted_result)
    print("Hasil Dekripsi ke Text:", decrypted_text)


