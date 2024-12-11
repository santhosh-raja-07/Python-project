print("vanakam chennai")

arr =[2, 3, 6 ,6 ,5]
firstMax = 0
SecondMax = 0
    
for i in arr:
    if i > firstMax:
        firstMax = i
for x in arr:
    if x > SecondMax and x != firstMax:
        SecondMax = x
            
print(SecondMax)

array = [1,3,45,6,7,8]
array[2]= 10
print(array)

#Modules
import split
print(split.fact(5))