import random
def encryption(text, key):
    enc=""
    for ch in text:
        if (ch.isupper()):
            enc+=chr((ord(ch)+key-65)%26+65)
        else:
            enc+=chr((ord(ch)+key-97)%26+97)
    print(f"Encrypted text: {enc}\t",end="")
    print("Key: ",key)
    print("======================================")

def decryption(text, key):
    dec=""
    for ch in text:
        if (ch.isupper()):
            dec+=chr((ord(ch)-key-65)%26+65)
        else:
            dec+=chr((ord(ch)-key-97)%26+97)
    print(f"Decrypted text: {dec}\t", end="")
    print("Key: ",key)
    print("======================================")

def decryptiontable(text):
    for i in range(0,25):
        decryption(text,i)

def main():
    while(True):
        print("1. Standard Encryption")
        print("2. Random Key Standard Encryption")
        print("3. Encryption with user key")
        print("4. Standard Decryption")
        print("5. Decryption 0-25")
        print("6. Decryption with user key")
        print("Enter your choice: ",end="")
        ch=int(input())
        if(ch>6):
            print("Program Terminated")
            break
        print("Enter the text: ",end="")
        text=input()
        if(ch==1):
            encryption(text,3)
        if(ch==2):
            encryption(text,random.randint(0,25))
        if(ch==3):
            print("Enter the key: ",end="")
            key=int(input())
            encryption(text,key)
        if(ch==4):
            decryption(text,3)
        if(ch==5):
            decryptiontable(text)
        if(ch==6):
            print("Enter the key: ",end="")
            key=int(input())
            decryption(text,key)
main()


