# 9.a
# The following line of code creates a sub class(customer) within class (person) or inherits it.

# 9.b
# The line of code defines the class attribute. like it helps in naming the person.

# 9.c

class Person:
    def __init__(self, name):
        self.name = name

    def alice(self):
        print("Hello, my name is", self.name)

person1 = Person("Alice")
person1.alice()


# 9.d


class Customer:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def greet(self):
        print(f"Hello, {self.name}! Welcome to our store.")


customer1 = Customer("John")
customer1.age = 30

customer1.greet()
