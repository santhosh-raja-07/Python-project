
#list of tuples
items = [(105 , "ddd", 2000) , (102 , "aaa", 4000) , (101 , "ccc", 1000) , (104 , "zzz", 20000) , (104 , "bbb", 6000)]
items.sort()
print(items)

items.sort(key=lambda x : x[1]) #sort with key
print(items)

items.sort(key=lambda i : i[2] , reverse= True)
print(items)

#tuple of tuples
items = ((105 , "ddd", 2000) , (102 , "aaa", 4000) , (101 , "ccc", 1000) , (104 , "zzz", 20000) , (104 , "bbb", 6000))
print(sorted(items))
print(sorted(items , key=lambda i : i[2]))

#Map (function , iterable)
item = [(105 , "ddd", 2000) , (102 , "aaa", 4000) , (101 , "ccc", 1000) , (104 , "zzz", 20000) , (104 , "bbb", 6000)]
multi_with_ten = lambda x : (x[1] , int("{:.0f}".format(x[2]/5)))
res = list(map(multi_with_ten , item))
print(res)

nums = [2,3,4,5,6,7]
def sqroot(nums):
    return nums * nums
result = list(map(sqroot , nums))
print(result)

#filter (function , iterable)
student = [(105 , "santhosh", 2000) , (102 , "sathish", 4000) , (101 , "jeeva", 1000) , (104 , "sham", 20000) , (104 , "hussain", 6000)]
stud_name = list(filter(lambda x : x[1][0]=='s' , student))
print(stud_name)

#reduce (function , iterable)
import functools

vals = [(105 , "santhosh", 2000) , (102 , "sathish", 4000) , (101 , "jeeva", 1000) , (104 , "sham", 20000) , (104 , "hussain", 6000)]
MethMap = list(map(lambda x : x[2] , vals))
MethRedu = functools.reduce(lambda i , j : i + j , MethMap)
print(MethRedu)

