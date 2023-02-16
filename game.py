#This program demonstrates a guesing 
#game


#1.get usre input

player=input("whats your name?")
print("hello there " + player+" are you ready to play")

#generate random number

ID_number=randint(10,50)

 counter=0
while counter<5:
    ID_number=eval(input("enter a number:"))

# 2.using while loop
#
# 3.generate user number
# check if user input is equal to generate number