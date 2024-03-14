# If/ Else conditions are used to decide to do something based on something being true or false

x=20
y=25

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x>y:
    print(f'yes {x} is greater than {y}')

# If/else
if x<y:
    print(f'yes {x} is lesser than {y}')
else:
    print(f'No {x} is not lesser than {y}')

# elif
if y>x:
    print(f'Yes {y} is greater than {x}')
elif y==x:
    print(f'yes {y} is equal to {x}')
else:
    print(f'Happy Women`s Day')

# Nested if

if x > 2:
    if x<50:
        print(f'{x} is greater than 2 and lessthan 50')

# Logical operators (and, or, not) - Used to combine conditional statements
#logical and
if x > 20 and x < 50:
    print(f'{x} is greater than 2 and lessthan 50')

#logical or
if x > 200 or x < 50:
    print(f'{x} is greater than 2 and lessthan 50')

# logical not
if not(x==y):
    print(f'{x} is not equal to {y}')

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x in numbers:
  print(x in numbers)

# not in
if x not in numbers:
  print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x is y:
  print(x is y)

# is not
if x is not y:
  print(x is not y)

