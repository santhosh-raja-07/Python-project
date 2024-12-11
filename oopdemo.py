class User:
    # users = 0   #Class variable
    # def __init__(self , user_name , password):
    #     self.user_name = user_name     #instance variable
    #     self.password = password
    #     User.users += 1
    
    def login(self):
        print("Succesfully Login ")
        return self 
        
user_1 = User()
user_1.login()

# print(user_1.user_name)
# print(User.users)

class student(User): #student class inherits User class
    # User = Parent class , student = Child class
    def greet(self):
        print("Hello students")

try:
  stud_1 = student()
  stud_1.greet()
except Exception as e:
    print(e)
    
# stud_1.login()

class greetStudent(student):
    def greet(self): # Method Overriding
        #Multi level inherits
        print("Nice to meet you")

greetstud = greetStudent()
greetstud.greet()

stud_1.login().greet()  #Method Chaning (using return)