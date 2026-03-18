#normal function

def add(x,y):
    return x+y
print(add(2,3))

#lambda function
add=lambda x,y:x+y
print(add(2,3)) 

#square of a number
square=lambda x:x*x
print(square(10))


numbers = [1, 2, 3, 4]

for num in numbers:
    print(num)

for i, num in enumerate(numbers):
    print(i, num)


#dictionary items


student = {"name": "Ram", "age": 20}

for key, value in student.items():
   print(key, value)

#sort numbers
numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers))

print(sorted(numbers, reverse=True))


#sort students by age

students = [("Ram", 20), ("Shyam", 18), ("Hari", 22)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#even 
numb=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(lambda x:x%2==0,numb))
print(even_numbers)


#map function
numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))
print(squared)


a = [1, 2, 3]
b = [4, 5, 6]

result = list(map(lambda x, y: x + y, a, b))
print(result)


numbers = [1,2,3,4]

result = list(map(lambda x : x*2, numbers))

print(result)


numbers = [1,2,3,4,5,6]

even = list(filter(lambda x : x % 2 == 0, numbers))

print(even)



students = [
   ("Ram", 20),
   ("Shyam", 18),
   ("Hari", 22)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

#upper case

names = ["ram", "shyam", "hari"]

upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)

lower_names=list(map(lambda x:x.lower(),upper_names
                     ))
print(lower_names)
                 

students = [
   {"name": "Ram", "marks": 80},
   {"name": "Shyam", "marks": 50}
]

passed = list(filter(lambda s: s["marks"] >= 60, students))
print(passed)

#Lambda Returning Multiple Values
calc = lambda x: (x, x**2, x**3)

print(calc(3))

#Nested Lambda 
multiply = lambda x: lambda y: x * y

result = multiply(5)(3)
print(result)





