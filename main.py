import time
#***PLEASE IGNORE TIME.SLEEP(1) IT IS JUST TO SLOWDOWN THE OUTPUTS**
#loops
for x in range(11):
  print("value:",x)
#notice how the printing stops before the given range by 1 number
for x in range(0,15,5):
  print('second example',x)
#^if the range has multiple numbers seperated by commas: the first one is the starting point, the second one is ending point, and the last one is to indicate skipped numbers between the first output and the next.
#2: if statement
print('---------------------------------------------------')
time.sleep(1)
x=int(input("enter a number:"))
# if you do not assign x as an integer you would get a syntax error
if x%2==0:
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
time.sleep(1)
def power3(num):
  return num*num*num
x=power3(4)+1
print(x)
print('----------------------------------------------------')
#user defined functions advanced
# We use user defined functions to make it easier and shorter to write certain programs
# For example: You are asked to make a grading program that shows lists of students according to thier letter grade. and you're required to make it for a single input and multiple inputs(loop) using 'while' once and using 'for' in another.
time.sleep(1)
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
print('-----------------------------')
#Dictionaries
#dictionaries are like a list but they have a value for each elemnt
time.sleep(1)
Cars={'Ferrari':'Red','Bugatti':['Black','Orange'],'Porsche':'Grey'}
#to add a key and a value we use dictionaryname[key]=value or dictionaryname.update()
Cars['McClaren']='Black'
print(Cars)
Cars.update({'G63':'Black'})
print(Cars)
#to print the value of acertain key use:
print(Cars['Ferrari'])
a=input("Enter the name of the car")
print(Cars[a])
time.sleep(1)
#or
print(Cars.get('Porsche'))
#to reassign a value of a key use:
Cars['Ferrari']='Yellow'
print(Cars['Ferrari'])
#to delete an item use:
Cars.pop('Bugatti')
print(Cars)
print('-----------------------------------------')
#OOP
time.sleep(2)
class Book():
#^class identification
  def __init__(self, title, author, content):
    self.title = title
    self.author = author
    self.content = content
#attributes^^
  #Methods:
  def read(self, page):
    a = self.content.split('\n')
    #^splitting text into pages *NOTE THAT \n IS A PAGE MARKER IN THE GIVEN TEXT.. IF THE TEXT DOES NOT HAVE \N IN IT IT WILL BE CONSIDERED 1 PAGE
    for i in range(0, page - 1):
      print(a[i])

  def __str__(self):
    return self.title + "by" + self.author

#inheritance:
class ComicBook(Book):
#^Child class(Takes Attributes from another class) *NOTICE HOW THE PARENT CLASS IS IN THE BRACKETS* you can inherit attributes from multiple parent classes simply add another parent class between the brackets and call for it's attributes
  def __init__(self, title, author, content, is_superhero):
    #^ you should put the parent class(inheritaded) attributes and the new attributes in the child class
    Book.__init__(self, title, author, content)
    #^calling Parent clas attributes
    self.is_superhero = is_superhero
    #^Assigning new attributes


c1 = ComicBook(
  'Spider-man', 'Stan Lee',
  'spider man was a kid from New York who was bitten by a spider and got the superpowers of a Spider.\n He lives with his aunt May and his uncle Ben. \n he is a student but he is also the hero of New York', True)
c1.read(2)
print('------------------------------------')
print(c1.is_superhero)
print('Please wait a few swconds')
time.sleep(3)
import tkinter as tk
#^ before anything we must import tkinter, this form of importing requires you to type .tk after almost everything but allows you the freedom to choose where to use tkinter and where not
window=tk.Tk()
#^ beginning of a window
window.title('Revision')
#^setting the title of the window
window.geometry('400x400')
#^setting the size of the window IN PIXELS
l1=tk.Label(window,text='I hope this revision was helpful',font='Times',bg='Blue')
#^creating a label 
l1.place(x=0,y=0)
#^ this is to set where in the window the text should be.. you can use grid() ir pack() but I think place is better. *THE LABEL WILL NOT SHOW IN THE WINDOW IF YOU DONT SET A PLACE FOR IT*
#YOU MUST USE THE SAME PLACEMENT FUNCTION(place,grid,packl)IN ALL ELEMENTS IN THE WINDOW
l2=tk.Label(window)
#^ creating an empty label to use in a function
l2.place(x=150,y=100)

tb=tk.Text(window,height=1,width=15)
#^creating a text box
tb.place(x=150,y=130)

def Copy():
  a=tb.get(0.0,tk.END)
  #^ this will assign a to be whatever is written inside the textbox
  l2.configure(text=f'The text box says: {a}')
  #^ this will display whats written in the box in the empty label we created

btn=tk.Button(window,text='Press here',height=1,width=10,command=lambda:Copy())
#^ this creats a button and command=lambda is a call for the function we created
btn.place(x=150,y=166)

window.mainloop()
#^closing the window.. this is very important or else the programm will NOT work