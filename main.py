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
    print('Rock...\nPaper...\nScissors/nShoot')
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
#