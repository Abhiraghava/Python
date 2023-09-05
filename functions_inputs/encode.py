alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_value):
    cipher_txt=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_value
        new_letter=alphabet[new_position]
        cipher_txt+=new_letter
    print(f"The encoded txt is {cipher_txt}")

def decrypt(cipher_text,shift_value):
    plain_txt=""
    for letter in cipher_text:
         position=alphabet.index(letter)
         new_position=position-shift_value
         plain_txt+=alphabet[new_position]
    print(f"The decode value {plain_txt}")
if direction=="encode":
    encrypt(nrm_text=text,shift_value=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_value=shift)




    



