
print("Hello Universe")

# strings methods
    
message = "happy brithday"
first_name = 'ram'
last_name = 'KUMAR'
name = "santhoshraja"

full_name  = first_name + last_name

print(message.title() +" "+ first_name.title() + last_name.lower())
print(first_name.upper())

print("hello \n everyone")
print("hello \t everyone")

# find the length of the string
print(len(message));

# find the index of the value (indexOF instend of find)
print(message.find('b'))

#count the letters
print(name.count('a'))

#replace the value
print(message.replace('i' , 'u'))

#check the value is all in alphabet or not
print(name.isalpha())

#check the value is all in digits or not
print(first_name.isdigit())

#print the value more than time use with  * in one line
print(first_name*5)

# check the value is upper or not
print(last_name.isupper())

#check the value is lower or not
print(message.islower())

#multiple variables and values assgin in one line
name , age , likesubject = "santhosh" , 19 , "problemSolving"
print(age)

like = dislike = 100
print(dislike)
print(like)

#TYPE CASTING
#change the integer value to string value
print("my age is " + str(age))

#change the string value to integer value
other_age="31"
print(age + int(other_age))

year=2024
print("Dear "+ last_name +", \n You have "+ str(age) +" days of leave balance for this \n year ("+ str(year) + ")")

#take the input and show the output
# name = input("What is your name :")
# print("Hello" + name)

# height = int(input("What is your height :"))
# height_inches = "{:.2f}".format(height/2.54)
# print("You are " + str(height) +" CM")
# print("You are " + str(height_inches) + " inches tall")

#Math Operations
a=20
b=3
print(a+b)
print(round(a/b))
print(abs(a-b))
print(pow(a,2))
print(b**5)

import math
c=4.55
print(math.floor(c))
print(math.ceil(c))
print(math.factorial(5))

#IF ELSE statement

pwd = True
if pwd:
    print("succesfully logged in")
else:
    print("incorrect pwd")

a=20
b=10
if a%2==0 and b%2==0:
    print("yes")
else :
    print("no")
    
name = "raja"
print(name[0])
print(name[:2])
print(name[:3])
print(name[:4])

print(name[::-1])
print(name[-1])

#List
nameOfstudents = ["kottai" , "karthikeyan" , "sheriff" , "shriram" , "hussain" , "jeeva" , "sham"]
print(nameOfstudents[5])

#append the new value in the end of the list
nameOfstudents.append("naveen")
print(nameOfstudents)

#insert the new value in the center of the list
nameOfstudents.insert(4,"krishna")
print(nameOfstudents)

#delete any element in the list " this is only a key word"
del nameOfstudents[0]
print(nameOfstudents)

#delete any element in the list using index of the value 
print(nameOfstudents.pop())

#remove any element in the list using value 
nameOfstudents.remove("shriram")
print(nameOfstudents)

# temoporary sort
unSortedNum = [5,8,3,11,1,4,2,79]
print(sorted(unSortedNum))
print(sorted(nameOfstudents))
print(nameOfstudents)
print(unSortedNum)

#permanent sort
nameOfstudents.sort()
print(nameOfstudents)

# reverse the element in ths list
unSortedNum.reverse();
print(unSortedNum)

#loops

num = 1
while num <= 10:
    print(num , end=" ")
    num+=1
print("end")

#nested loop
n = 3
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=' ')
    print('')
    

# palinrome = "Madam"
# str1 = ""
# for i in range(1,len(palinrome)+1):
#     str1 += palinrome.pop()
#     break
# if str1 == palinrome:
#     print(True)
# else:
#     print(False)

palinrome = "Madam"
str1 = ""
# Reverse the string by iterating backward
for i in range(len(palinrome) - 1, -1, -1):
    str1 += palinrome[i]

# Check if the reversed string matches the original string (case-insensitive)
if str1.lower() == palinrome.lower():
    print(True)
else:
    print(False)
    
#break

# continue  
str1 = "R,A,J,A"
str2 = ""
for i in str1:
    if i == ',':
        continue
    str2 += i
print(str2)

#pass 
str1 = "J-E-E-V-A"
str2 = ""
for i in str1:
    if i == '-':
        pass
    else:
       str2 += i
print(str2)

#Walrus operator :=

print(name := "sathish")
print(name)
