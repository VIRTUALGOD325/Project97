import random 

guess = input("Please Guess: ")

number = random.randrange(1,10)

chance = 5

if (guess == number):
    print("You Won")
elif(chance == 0):
    print("Game Over")
else:
    print("Guess Again")
    chance = chance - 1


'''
for number in user_input:
    if(number == user_input):
        print("You Have Won")
    elif():
        print(num)
'''
    