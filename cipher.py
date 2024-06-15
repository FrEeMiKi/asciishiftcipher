from sys import argv, stdout

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char)+ s) % 128)
    return result

def __main__():
    if len(argv) < 3:
        print("Usage: python3 cipher.py <shift> <text>")
        return

    text = argv[2]
    try:    
        s = int(argv[1])
    except ValueError:
        print("Invalid shift value")
    
    encrypted = encrypt(text, s)
    encrypted_ord = [ord(c) for c in encrypted]


    stdout.reconfigure(encoding='utf-8')
    print("Text  : " + "\"" + text + "\"")
    print("Shift : " + str(s))
    print("Cipher (ASCII): " + "\"" +  str(encrypted_ord) + "\"")
    print("Cipher (text): " + "\"" +  encrypted + "\"")
    stdout.flush()
        
if __name__ == "__main__":
    __main__()