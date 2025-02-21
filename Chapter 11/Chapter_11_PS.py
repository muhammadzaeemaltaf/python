# Q1. Create a class (2-D vector) and use it to create a class (3-D vector).

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"x: {self.x}, y: {self.y}")

# class Vector3D(Vector2D):
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z

#     def show(self):
#         print(f"x: {self.x}, y: {self.y}, z: {self.z}")
 
# v2 = Vector2D(1, 2)
# v3 = Vector3D(1, 5, 3) 

# v2.show()
# v3.show()

# Q2. Create a class Pets from a class Animals and further create a class Dogs from Pets.
# Add a method bark to class Dogs.

# class Animals: 
#      pass

# class Pets(Animals):
#     pass

# class Dogs(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")
#     pass

# dog = Dogs()
# dog.bark()



# Q3. Create a class Employee and add salary and increment properties to it.

# class Employee:
#     salary = 10000
#     increment = 1000
    
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.salaryAfterIncrement = salary/self.salary - 1

# emp = Employee()
# print(emp.salaryAfterIncrement)
# emp.increment = 12000
# print(emp.salaryAfterIncrement)



# Q4. Write a class complex to represent complex numbers, along with methods to add,
#  subtract and multiply two complex numbers.

# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c):
#         return Complex(self.r + c.r, self.i + c.i)
    
#     def __mul__(self, c):
#         return Complex(self.r * c.r - self.i * c.i, self.r * c.i + self.i * c.r)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)

# print(c1.__add__(c2))
# print(c1.__mul__(c2))


#  Q5. Write a class Vector to represent a vector of n dimension. Overload the + and * operators
#  which calculate the sum and dot product of two vectors.

# class Vector:
#     def __init__(self, *args):
#         self.v = args

#     def __add__(self, v):
#         return Vector(*[self.v[i] + v.v[i] for i in range(len(self.v))])
    
#     def __mul__(self, v):
#         return sum([self.v[i] * v.v[i] for i in range(len(self.v))])
    
#     def __str__(self):
#         return f"{self.v}" 

# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)

# print(v1+(v2))
# print(v1*(v2))


# Q6. Write __str__() method in the Vector class to display the vector as follows:
# 2i + 3j + 4k
# Assume that the vector is of 3 dimensions.

# class Vector:
#     unit = ['i', 'j', 'k']
#     def __init__(self, *args):
#         self.v = args

#     def __add__(self, v):
#         return Vector(*[self.v[i] + v.v[i] for i in range(len(self.v))])
    
#     def __mul__(self, v):
#         return sum([self.v[i] * v.v[i] for i in range(len(self.v))])
    
#     def __str__(self):
#         return " + ".join([f"{self.v[i]}{Vector.unit[i]}" for i in range(len(self.v))]) 

# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)

# print(v1+(v2))
# print(v1*(v2))


# Q7. Override a __len__() method on vector of problem 5 disply the dimension of the vector.

class Vector:
    unit = ['i', 'j', 'k']
    def __init__(self, *args):
        self.v = args

    def __add__(self, v):
        return Vector(*[self.v[i] + v.v[i] for i in range(len(self.v))])
    
    def __mul__(self, v):
        return sum([self.v[i] * v.v[i] for i in range(len(self.v))])
    
    def __str__(self):
        return " + ".join([f"{self.v[i]}{Vector.unit[i]}" for i in range(len(self.v))]) 
    
    def __len__(self):
        return len(self.v)

v1 = Vector(1, 2, 3)

print(len(v1))

