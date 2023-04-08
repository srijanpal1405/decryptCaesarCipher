# from langdetect import detect
from langdetect import detect_langs

text="hello this is test"

all_conf=[]
shift_li=[]
for i in range(1,26):
    file2 = open('decrypt_Shift_' + str(i) + '.txt', 'r')
    fileContent=file2.readlines()
    strfile="".join(fileContent)
    all_conf.append(str(detect_langs(strfile)[0]))
    file2.close()
# print(all_conf)
for i in range(0,25):
    if float(all_conf[i][3:]) > 0.9:
        shift_li.append(all_conf[i][0:3]+str(i+1))

print("Probable shift keys: ")
print(shift_li)