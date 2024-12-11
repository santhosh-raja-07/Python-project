
#Split
string = "How-are-you-?"
str_list = string.split('-')
print(str_list)

#Join
str_join = ' '.join(str_list)
print(str_join)

#tuple (immutable)
tup = (1,4,5,3,5,4,2,2,3,2,2)
print(tup.count(2))

for i in tup:
    print(i , end=" ")
print(" ")
    
if 6 in tup:
    print("Yes")
else:
    print("No")
    
# dictionary (object)

student = {"Name" : "Santhosh" , "Age" : 26, "Gender" : "male"}
print(student["Name"])

student["city"] = "Cuddalore"
print(student)

student["Age"] = 19
print(student)

del student["city"]
print(student)

for key,val in student.items():
    print(key , val)
    
    
#List of dictionary
users_list = [ {"Name" : "Santhosh" , "Age" : 19, "Gender" : "Male" , "City" : "Coimbatore"}]
user_details= {"Name" : "Jeeva", "Age" : 21, "Gender" : "Male", "City" : "Coimbatore"}
users_list.append(user_details)
user_details= {"Name" : "Hussain", "Age" : 20, "Gender" : "Male", "City" : "Chennai"}
users_list.append(user_details)
user_details= {"Name" : "Sham", "Age" : 21, "Gender" : "Male", "City" : "Chennai"}

for i in range(0 , len(users_list)):
    print(users_list[i]["Name"])
    
#Sets
foods = {"Briyani" , "Dosa" , "Chappathi" , "Sambar" , "Rasam" , "Vegrice", "Dosa"}
print(foods)
foods_list = list(foods)
foods_sets = set(foods_list)

print(foods_list)

#String formating

Sentence = 'Iam {} from {} and My age is {}'
name = "santhosh"
city = "cuddalore"
age = 19
print(Sentence.format(name , city , age))

print(foods_sets)

#Function
def addNum(n):
    arr = []
    for i in n:
      add = i + i
      arr.append(add)
    print(arr)
addNum([1,2,3,4,5,6])
    
    
#Variable length arrgument (*args is change the parameter to tuple)
def multipleNum(*array):
    arr = []
    multi = 0
    for x in array:
        multi = x * x
        arr.append(multi)
    return arr
print(multipleNum(1,2,3,4,5,6))   
    
    
# (**kwargs is change the parameter to dictionary)
def studentsdetail(**data):
    for key,val in data.items():
        print(key , val)
studentsdetail(Name = "Jeeva", Age = 21, Gender = "Male", City = "Coimbatore")

#recursion
def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
print(fact(5))

