import pyfiglet
import random
import termcolor

BANNER = pyfiglet.figlet_format("Z_Cipher",font="slant")
COLOR = termcolor.colored(BANNER, "blue")
print(COLOR)

def key_gen(l):
    if l < 1:
        raise ValueError("Key length should be at least 1 byte.")
    key = bytearray(random.getrandbits(8) for _ in range(l))  # Generate a random byte string
    return key

def encrypt(text, key):
    encrypted_text = bytearray()
    key_index = 0
    
    for char in text:
        # XOR the character with the corresponding key byte
        encrypted_char = chr(ord(char) ^ key[key_index])
        encrypted_text.append(ord(encrypted_char))
        
        # Move to the next character in the key
        key_index = (key_index + 1) % len(key)
        
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    
    for char in encrypted_text:
        # XOR the character with the corresponding key byte
        decrypted_char = chr(char ^ key[key_index])
        decrypted_text += decrypted_char
        
        # Move to the next character in the key
        key_index = (key_index + 1) % len(key)
        
    return decrypted_text

def main():
    text = input("Enter the text: ")
    if not text:
        print("Text cannot be empty. Please enter some text.")
        return
    
    l = input("Enter the number of bytes for the key length: ")
    try:
        l = int(l)
        key = key_gen(l)
    except ValueError:
        print("Key length should be a positive integer.")
        return

    encrypted_text = encrypt(text, key)

    print("Encrypted text (hex):", ''.join('\\x{:02x}'.format(b) for b in encrypted_text))

    
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()