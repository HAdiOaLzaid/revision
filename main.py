import time
#***PLEASE IGNORE TIME.SLEEP(1) IT IS JUST TO SLOWDOWN THE OUTPUTS**
#loops
for x in range(11):
  print("value:",x)
#notice how the printing stops before the given range by 1 number
for x in range(1,15,5):
  print('second example',x)
#^if the range has multiple numbers seperated by commas: the first one is the starting point, the second one is ending point, and the last one is to indicate skipped numbers between the first output and the next.
#2: if statement
print('---------------------------------------------------')
time.sleep(1)
x=int(input("enter a number:"))
# if you do not assign x as an integer you would get a syntax error
if x%2==1:
   print('even')
else:
  print('odd')
print('--------------------------------------------------')
time.sleep(1)
#adding strings
x=str(1)+"abc"
print(x)
#^ if we dont assign 1 as a string will get a syntax error for adding integer and a string
print('-------------------------------------------------')
time.sleep(1)
#diffrence between / and // and %
a=2
b=5
x=b/a
y=b//a
z=b%a
print(x,y,z)
print('--------------------------------------------------')
#^ as we can see / operates normal division, // operates floor (integer) division (whithout remainder) and %'s output is the remainder of the division
#other operations
time.sleep(1)
x=int(input('solve the following equation for x: 2x-6=0  answer='))
if x!=3:
  print('incorrect')
else:
  print('correct')
#^ != means not equal
print('--------------------------------------------------')

#triple quotation
time.sleep(1)
print('''hi
my
name
is''')
# if we use single or double quotation for a multi-lined string we would get a syntax error, however we can use \n to get the same results
print('hi\nmy\nname\nis\n')
print('-------------------------------------------------')
#we can slice strings using [] for example
time.sleep(1)
x='python'
print(x[2])
print(x[0:3])
print('--------------------------------------------------')
#try and except number of years bonus. note: this was added after the midterm.
time.sleep(1)
try:
  x=float(input('Enter number of years served:'))
  if x<1:
    print('Bonus is:',"0%")
  elif x>=2 and x<6:
    print('Bonus is:',"2%")
  elif x>=6:
    print('Bonus is:',"3%")
except:
   print("Number of years must be in numbers")
print('-----------------------------------------------')
# IMPORTANT:the except block will only be executed if the error is within the try block. meaning that if you assign the value x *before* the try function (not inside the try: indentation), and the input was not a number, the except block won't be executed and you would get an error

#importing, if, and loop in one program
time.sleep(1)
import random 
x=['rock','paper','scissors']
y=random.choice(x)
z=input('Enter rock, paper, or scissors:   ')
while z!='rock' and z!='paper' and z!='scissors':
  print('Invalid entry,\nplease try again')
  z=input('Choose rock, paper, or scissors:   ')
else:
  if z=='rock' and y=='scissors':
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'YOU WIN!')
  elif z=='scisoors' and y=='paper':
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'YOU WIN!')
  elif z=='paper' and y=='rock':
    print('Rock...\nPaper...\nScissor\nShoot')
    print(z,'VS',y,'YOU WIN!')
  elif z=='paper' and y=='scissors':
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'YOU LOSE!')
  elif z=='scissors' and y=='rock':
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'YOU LOSE!')
  elif z=='rock' and y=='paper':
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'YOU LOSE!')
  elif z==y:
    print('Rock...\nPaper...\nScissors\nShoot')
    print(z,'VS',y,'DRAW!')
#
#finding a letter in a text
print('----------------------------------')
y=input('Enter a text:')
x=0
z=input('Enter a letter:')
for b in y:
   if b==z:
     x=x+1
print('the letter',z,'appeaqred',x,'times')
#^ uppercase of the same letter won't count i.e: the text is cccccC it will only count 5 times
#printing in 1 line for 'for loops'
print('----------------------------------------')
time.sleep(1)
fruitsBasket=['apple','orange','bannana','grapes']
for fruit in fruitsBasket:
  print(fruit,end=',')
# we use end=',' to print the values in the same line
#string play
print('\n------------------------------------------')
time.sleep(1)
name='python'  
print(name[2])
print(name.upper())
print(name.lower())
print(name.replace('p','b'))
print(name[1:4])
#
#list operations
print('-------------------------------------------')
time.sleep(1)
my_list=['apple','banana','cherry']
print(my_list)
print("list length is:",len(my_list))
if 'apple' in my_list:
  print("yes,'apple' is in my list")
#
#adding even numbers in a range
print('------------------------------------------')
time.sleep(1)
Tot=0
for x in range(10):
  if x%2==0:
    Tot=Tot+x
print('total:',Tot)
# x%2==0 means the remainder of x/2 is 0 which is only true for even numbers
#printing a number and its square
print('-----------------------------')
time.sleep(1)
for number in range(1,11):
  square=number**2
  print(number,'\t     ',square)
#
print('--------------------------------------------')
#for and while loops for the same problem
#for loop
numbers=[1,2,8,4,14]
for i in numbers:
  print(i)
#while loop
print('-----------------------------------------')
x=0
while x<len(numbers):
  print(numbers[x])
  x+=1
print('------------------------------------------')
#
#User defined functions basic
#create a function that calculates the third power of a number
def power3(num):
  return num*num*num
x=power3(4)+1
print(x)
print('----------------------------------------------------')
#user defined functions advanced
# We use user defined functions to make it easier and shorter to write certain programs
# For example: You are asked to make a grading program that shows lists of students according to thier letter grade. and you're required to make it for a single input and multiple inputs(loop) using 'while' once and using 'for' in another.
A_students=[]
B_students=[]
C_students=[]
D_students=[]
F_students=[]
# ^We create empty lists to catagorize students in
def Grade():
  name=str(input("Enter Student's Name: "))
  grade=float(input("Enter Student's Grade: "))
  if grade>=90:
    A_students.append(name)
  elif grade>=80:
    B_students.append(name)
  elif grade>=70:
    C_students.append(name)
  elif grade>=60:
    D_students.append(name)
  else:
    F_students.append(name)
#^ We write the grading program and we define it under a function so we can use it multiple times without rewriting it all over again each time
def PrintAll():
  print('A students are',A_students)
  print('B students are',B_students)
  print('C students are',C_students)
  print('D students are',D_students)
  print('F students are',F_students)
#^ I also defined a function to print all the lists to save time and space
Grade()
PrintAll()
#^ single input
student_count=int(input('Enter the number of students: '))
#^ number of inputs the user wishes to make
for i in range(0,student_count):
  Grade()
PrintAll()
#^ for loop
repeats=0
while repeats<student_count:
  Grade()
  repeats=repeats+1
PrintAll()
#^ while loop
# Each loop without the defined function would have taken 18 lines at least.. now, each takes 3-5 lines