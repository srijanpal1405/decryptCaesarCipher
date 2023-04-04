# # A python program to illustrate Caesar Cipher Technique

# to read file character by character
file = open('original.txt', 'r')
file2 = open('encrypt.txt', 'w')

shift = int(input("Enter shift(integer): "))
while 1:
    # read by character
    char = file.read(1)
    if char.isalpha():
        if char.isupper():
            file2.write(chr((ord(char) + shift - 65) % 26 + 65))
        else:
            file2.write(chr((ord(char) + shift - 97) % 26 + 97))
    elif not char:
        break
    else:
        file2.write(char)

file.close()
file2.close()
