course = 'Python 101'

#indentation and Python formatting

if course == 'Python 101':
    print('correct course!')

course = 'Python 102'

print(course)

if course == 'Python 102':
    print('another correct course!')



# indexing and slicing

#offsets = count from zero??

lst = [1,2,3,4,5]

print(lst[-4:3])

#name = input('What is your name?')

#print('Hello, ', name)

grocery_list = tuple(('Apples', 'Oranges', 'Bananas'))

grocery_list = set(grocery_list)
print(type(grocery_list))

name = 'Miko'

wazzup = f"Hello {name}, wazzup?"



print(wazzup)

testingLambdas = lambda x,y : x * y

print(testingLambdas(5, 10))
print(testingLambdas(12.2, 2.5))

animal = ['cat', 'dog', 'bird']
#function definition

def myFunc():
    print('Hello,world')

myFunc()

def myFunc2(name, age, gender):
    print(f"Hello, my name is {name}, and I am {age} years old. I classify as a {gender}")

myFunc2('Miko', 20, 'male')

#TODO: download more extensions
