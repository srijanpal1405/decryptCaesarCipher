

for i in range(1,26):
    file = open('encrypt.txt', 'r')
    file2=open('decrypt_Shift_'+str(26-i)+'.txt','w')
    int(i)
    while 1:
        # read by character
        char = file.read(1)
        if char.isalpha():
            if char.isupper():
                file2.write(chr((ord(char) + i - 65) % 26 + 65))
            else:
                file2.write(chr((ord(char) + i - 97) % 26 + 97))
        elif not char:
            break
        else:
            file2.write(char)

    file.close()
    file2.close()


