#loops

for x in range(11):
  print("value:",x)
#notice how the printing stops before the given range by 1 number
for x in range(1,15,5):
  print('second example',x)
#^if the range has multiple numbers seperated by commas: the first one is the starting point, the second one is ending point, and the last one is to indicate skipped numbers between the first output and the next.
#2: if statement
print('---------------------------------------------------')
x=int(input("enter a number:"))
# if you do not assign x as an integer you would get a syntax error
if x%2==0:
  print('even')
else:
  print('odd')
print('--------------------------------------------------')
#adding strings
x=str(1)+"abc"
print(x)
#^ if we dont assign 1 as a string will get a syntax error for adding integer and a string
print('-------------------------------------------------')
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
x=int(input('solve the following equation for x: 2x-6=0  answer='))
if x!=3:
  print('incorrect')
else:
  print('correct')
#^ != means not equal
print('--------------------------------------------------')

#triple quotation
print('''hi
my
name
is''')
# if we use single or double quotation for a multi-lined string we would get a syntax error, however we can use \n to get the same results
print('hi\nmy\nname\nis\n')
print('-------------------------------------------------')
#we can slice strings using [] for example
x='python'
print(x[2])
print(x[0:3])
print('--------------------------------------------------')
#try and except number of years bonus. note: this was added after the midterm.
try:
  x=float(input('number of years served:'))
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
fruitsBasket=['apple','orange','bannana','grapes']
for fruit in fruitsBasket:
  print(fruit,end=',')
# we use end=',' to print the values in the same line
#string play
print('\n------------------------------------------')
name='python'  
print(name[2])
print(name.upper())
print(name.lower())
print(name.replace('p','b'))
print(name[1:4])
#
#list operations
print('-------------------------------------------')
my_list=['apple','banana','cherry']
print(my_list)
print("list length is:",len(my_list))
if 'apple' in my_list:
  print("yes,'apple' is in my list")
#
#adding even numbers in a range
print('------------------------------------------')
Tot=0
for x in range(10):
  if x%2==0:
    Tot=Tot+x
print('total:',Tot)
# x%2==0 means the remainder of x/2 is 0 which is only true for even numbers
#printing a number and its square
print('-----------------------------')
for number in range(1,11):
  square=number**2
  print(number,'\t     ',square)