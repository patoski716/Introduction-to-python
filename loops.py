# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['John','Paul','Efemena','Tobechukwu']

#Simple loop
# for person in people:
    # print(f'My name is {person}') 

#Break
# for person in people:
#     if person == 'Efemena':
#         break
#     print(f'My name is {person}')

#Continue
# for person in people:
#     if person == 'Efemena':
#         continue
#     print(f'My name is {person}')

# While loops execute a set of statements as long as a condition is true.
count= 0
while count < 10:
    print(f'i am number {count}')
    count+=1