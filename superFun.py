class User:
    users = 0   #Class variable
    def __init__(self , user_name , password):
        self.user_name = user_name     #instance variable
        self.password = password
        User.users += 1
    
    def login(self):
        print("Succesfully Login ")
        return self 
    def sginup(self):
        print("Hello everyone")
        
user_1 = User("Santhosh" , "12345!Aa")
user_1.login()

print(user_1.user_name)
print(User.users)

class student(User): #student class inherits User class
    # User = Parent class , student = Child class
    def __init__(self, user_name, password , course , fee):
        super().__init__(user_name, password)
        self.course = course
        self.fee = fee
    def greet(self):
        super().sginup()
        print("Hello " + self.user_name)

try:
  stud_1 = student("raja" , "12345!Aa" , "B.tech" , 12000)
  stud_1.greet()
except Exception as e:
    print(e)
    
 # high order function
 
def happy():
     print("smiling...")

def sad():
    print("crying...")

joy = happy
joy()

def feeling(fun):
    fun()

feeling(joy)
feeling(sad)

# lambda function (anonymous function)
add = lambda i : i+10
print(add(10))

simpleInterest = lambda P , R , T : (P*R*T)/100
print(simpleInterest(2000,20,2))

checkBoolen = lambda x : x < 20 
print(checkBoolen(20))

checkIfElse = lambda x : "Yes" if x >= 20 else "No"
print(checkIfElse(20))

#F string

name = "kottai"
age = 62
print(f"He is name {name} and his age is {age}")