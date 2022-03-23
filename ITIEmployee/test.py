import re


class Employee:
    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("salary must be more than 1000")

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            self.__email= email
        else:
            print("not a valid email")
emp1= Employee(1,"car","n_ayman58",44,22)
# print(emp1.email)