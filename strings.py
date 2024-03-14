name = 'Patrick'
surname = "Chukwudifu"
age = 29
# print(type(surname))

#Concatenation
# print('The name of my tutor in web developement class is ' + name + " " + surname)

#String Formatting

#Argument by position
# print('The name of my tutor is {name} {surname} and he is {age} year old'.format(name=name,surname=surname,age=age))

# F-String
# print(f'the name of my facilitator for sid program is Mr {name} {surname} and he his {age} year old')

s = 'Solution is here'

# String Method

#capitalise
# print(s.capitalize())

#uppercase
# print(s.upper())

#lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())