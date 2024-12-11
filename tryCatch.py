#Exception Handling

try:
    num  = int(input("Enter the numerator : "))
    den = int(input("Enter the denominator : "))
    result = num/den
    
except ZeroDivisionError:
    print("ypu can't divide by zero")
except ValueError:
    print("Enter numbers only")
else:
    print(result)
finally:
    print("this is always executes")
  
print("bye")

