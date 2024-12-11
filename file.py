with open("myfile.txt") as F:
    print(F.read())
print(F.closed)


with open("myfile.txt" , 'w') as f:
    f.write("Hello Krishna")
print(f.closed)

text = " how are you?"
with open("myfile.txt" , 'a') as fileName:
    fileName.write(text)