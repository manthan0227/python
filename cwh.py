print("Enter the first number::")
num1 = input()
print("Enter the second number::")
num2 = input()
result = int(num1) + int(num2)
print("Addition of two numbers:: ",result)


mystr = "Manthan is a good boy"
print(mystr[::-1])
print(len(mystr))
print(mystr.count("a"))
print(mystr.endswith("boy"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.find("g"))
print(mystr.upper())
print(mystr.replace("good","great"))


mylist = ["harpic","vimbar","deodrant","Bhindi","Lollypop"]
print(mylist)
numbers = [2,3,15,6,8]
print(numbers[::-1])
numbers.reverse()
numbers.append(23)
numbers.append(24)
numbers.append(25)
numbers.insert(2,4)
numbers.remove(15)

print(numbers)

tp = (12,23,45,34)

print(tp)

a = 1
b = 8
a,b = b,a
print(a,b)


d1 = {"harry":"burger","Rohan":"Fish"}
del d1["harry"]
print(d1.keys())
print(d1.items())


d = {"Manthan":"Boy","Brinda":"Girl","Shubham":"Boy","Jigar":"Boy","Ami":"Girl"}
print(d.items())
print(d.keys())
print(d.values())
print(d.clear())
print(d)

s = set()
s.add(1)
s.add(2)
s = {1,2}
print(s)
s1 = s.intersection({1,2,3})
print(s1)

age = int(input())

if age>18 and age<100:
    print("You can drive")
elif age==18:
    print("We cannot decide wheater you can drive or not")
else:
    print("You cannot drive pele apna khada karke aao")


num1 = int(input())
num2 = int(input())
result = 0
if (num1==55 and num2==29) or (num1==20 and num2==50) or (num1==10 and num2==90):
    result = num1 + num2 - 67
else:
    result = num1 + num2
print(result)


dict2 = {'Harry':"1",'Larry':"2",'Carry':"3"}
dict1 = dict(list1)
for i in dict2.keys():
    print(i)

i=0
while(i<29):
    print(i,end=" ")
    if i==20:
        break
    i=i+1

num1 = int(input())
while(1):
    if num1<100:
        num1 = int(input())
        continue
    if num1>100:
        break


A = int(input())
B = int(input())
if A>B: print("A is greater than B")



def func1():
    '''This is the function that return value '''
    print("You are in fun1 ")
    return 1
v = func1()
print(v)

n = int(input())
b = input()

if b=="true":
    for i in range(n):
        for j in range(n):
            if(i>=j):
                print("*",end = " ")
            
        print()
else:
    for i in range(n):
        for j in range(n):
            if(i<=j):
                print("*",end = " ")
            
        print()

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

p = factorial(5)
print(p)

def fibbonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibbonacci(n-2) + fibbonacci(n-1)
x = fibbonacci(5)
print(x)


import random
user_score = 0
computer_score = 0
lst = ["Stone","Paper","Scissor"]
print("Welcome to my Stone, Paper And Scissor Game XX")
print("*"*50)
user_choice = input("Do you play game??")
while user_choice == "Y" or user_choice == 'y':
    user_turn = input("Please Choose one of Stone, Paper and Scissor------->>>>")
    computer_turn = random.choice(lst)
    print("Choice of user:: ",user_turn)
    print("Choice of computer:: ",computer_turn)
    if user_turn == "Stone" or user_turn == "stone":
        if computer_turn=="Stone":
            print("It's tie.")
        elif computer_turn=="Paper":
            computer_score+=1
            print("You loss. Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")
    elif user_turn == "Paper" or user_turn == "paper":
        if computer_turn == "Paper":
            print("It's tie.")
        elif computer_turn=="Scissor":
            computer_score+=1
            print("You loss.Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")
    else:
        if computer_turn == "Scissor":
            print("It's tie.")
        elif computer_turn == "Stone":
            computer_score+=1
            print("You loss.Computer is winner. Better luck for next time.")
        else:
            user_score+=1
            print("You win.Great Achievement.")

    print("Do you play game again???")
    user_choice = input("Y/N--->>>")

print("X"*50)
print("Computer's Score == ",computer_score)
print("User's Score == ",user_score)
if computer_score > user_score:
    print("Sorry!!!!!!!!,Computer win.")
elif computer_score < user_score:
    print("User win.")
else:
    print("Tie game.")


import datetime
name = "manthan"
surname = "nagpurkar"
t = datetime.datetime.now()
a = f"My name is {name} {surname}"
print(a)
print(t)
print(datetime.datetime.now()-t)


def print_name(*args,**kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        a =  f"{key} is a {value}"
        print(a)


lst = ["manthan","jigar","shubham","sanidhya"]
dt = {"manthan":"leader","jigar":"assistant","shubham":"Programmer","sanidhya":"Instructor"}
print_name(*lst,**dt)

import time

t = time.time()
print(t)
i = 0
while(i<34):
    print("HI")
    i+=1

print(time.time()-t)


l1 = [1,2,3,4]
for index, value in enumerate(l1):
    if index%2 is 0:
        print(index, value)

print(__name__)
if __name__ == "__main__":
    print("My name is manthan")


ls = ["manthan","shubham","jigar","sanidhya"]
s = ", ".join(ls)
print(s)



ls = ["2","4","5","6"]
ls = list(map(int,ls))
ls[2] = ls[2] + 1
print(ls[2])


ls = [1,2,3,4]
a = list(map(lambda x: x*x,ls))
print(a)

def greater_than_5(num):
    return num>5

ls = [1,2,3,4,5,6,7,8,9]
f = list(filter(lambda x:x>5 , ls))
print(f)

from functools import reduce
r = reduce(lambda x,y: x+y, ls)
print(r)


from pygame import mixer
from playsound import playsound
# mixer.init()
# # mixer.music.load("water.mp3")
# mixer.music.set_volume(0.7)
# mixer.music.play()
playsound("water.mp3")
mixer.Sound();
while True:
    print("Press p for pause")
    print("Press r for resume")
    print("Press s for stop")
    q = input(" ")
    if q == 'p':
        mixer.music.pause()
    elif q == 'r':
        mixer.music.unpause()
    else:
        mixer.music.stop()
        break


def fun():
    print("Sun")

fun3 = fun
del fun
fun3()


class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(A,C):
    pass