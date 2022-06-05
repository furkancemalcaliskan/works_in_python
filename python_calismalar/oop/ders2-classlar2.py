

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Engin","Demiroğ",33)
print(person1.firstName)


class Worker:
    def __init__(self,salary):
        self.salary = salary

class Customer:
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber

ahmet = Worker()
mehmet = Customer()

