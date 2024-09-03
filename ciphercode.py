alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continuous= "yes"
from cipherart import logo
print(logo)
def cipher(word,shift_number,encrypt_decrypt):
    cipher_text=""
    if encrypt_decrypt=="decrypt":
            shift_number*=-1
    for char in word:
        if char in alphabet:
             postion = alphabet.index(char)
             new_postion= (postion+shift_number)%25
             cipher_text+=alphabet[new_postion]
        else:
             cipher_text+=char
    print(cipher_text)
while continuous=="yes":
    encrypt_decrypt=input("you want to encrypt or decrypt: ")
    word=input(f"what is the word you want to {encrypt_decrypt}: ")
    shift_number=int(input("enter shift number: "))
    cipher(word,shift_number,encrypt_decrypt)
    continuous= input("do you want to countinue 'yes' or 'no': ")

    