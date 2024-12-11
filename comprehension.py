#list comprehension
sq_list = [x*x for x in range(1,11)]
print(sq_list)

arr = [1,2,3,4,5]
even = [i for i in arr if i%2 == 0]
print(even)

odd= [i if i%2 != 0 else "Not OddNumber" for i in arr]
print(odd)

#Dictionary comprehension

vals = {"phone" : 20000.0 , "lamp" : 1000.0 , "pen" : 10.0 , "bag" : 750.0}
result = {K.title() : round(V) for K,V in vals.items() if V < 1000}
print(result)

# Zip
items = ["books" , "pen" , "table" , "bag"]
price = [250 , 10 , 1500 , 700]
zipVal = dict(zip(items , price))
print(zipVal)
