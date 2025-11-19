# list
employees = ['Ann', 'Joseph', 'Paul', 'Jay']
print(employees)
print(employees[2])
employees[1] = 'josephine'
print(employees)
# tuple
students = ('Dennis', "Andrew", 'Josephine', 'Queen')
print(students)
print(students[1])
# students[1] = 'Kylian'
# print(students) can not change a variable or value in a tuple
# set
fruits = {'orange', 'mangoe', 'banana', 'apple'}
print(fruits)
fruit = fruits
if fruit in fruits == 'mangoe':
    print(fruit)
# Dictionary
person = {
    'name':'Jay',
    'age': 21,
    'gender': 'male'
}
print(person)
print(person['name'])