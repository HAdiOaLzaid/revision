#loops

for x in range(11):
  print("value:",x)
#notice how the printing stops before the given range by 1 number
for x in range(1,15,5):
  print('second example',x)
#^if the range has multiple numbers seperated by commas: the first one is the starting point, the second one is ending point, and the last one is to indicate skipped numbers between the first output and the next.
#2: if statement
x=int(input("enter a number:"))
# if you do not assign x as an integer you would get a syntax error
if x%2==0:
  print('even')
else:
  print('odd')
#adding strings
x=str(1)+"abc"
print(x)
#^ if we dont assign 1 as a string will get a syntax error for adding integer and a string

#diffrence between / and // and %
a=2
b=5
x=b/a
y=b//a
z=b%a
print(x,y,z)
#^ as we can see / operates normal division, // operates floor (integer) division (whithout remainder) and %'s output is the remainder of the division
#other operations
x=int(input('solve the following equation for x: 2x-6=0  answer='))
if x!=3:
  print('incorrect')
else:
  print('correct')
#^ != means not equal

#triple quotation
print('''hi
my
name
is''')
# if we use single or double quotation for a multi-lined string we would get a syntax error, however we can use \n to get the same results
print('hi\nmy\nname\nis\n')
#we can slice strings using [] for example
x='python'
print(x[2])
print(x[0:3])
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
  
