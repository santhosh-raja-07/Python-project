import random

num = random.randint(1,20)
guess = int(input("Can you guess the number ? Its less than 20 : "))
count = 0

while num != guess:
    count +=1
    if count > 4:
        break
    if guess > num:
        print("your guess is higher")
    else:
        print("your guess is lower")
    guess = int(input("Guess again : "))
    
if count == 5:
    print("you Lose")
else:
    print("You won")