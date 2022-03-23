import re


class person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if healthRate >= 0 and healthRate <= 100:
            self.__healthRate = healthRate
        else:
            print("health rat must be between 0 to 100")

    def sleep(self, hours: int):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        elif hours > 7:
            self.mood = "lazy"

    def eat(self, meals: int):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"

    def buy(self, item: int):
        if item > 0:
            self.money -= item * 10


class Employee(person):
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
            self.__email = email
        else:
            print("not a valid email")

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        elif hours < 8:
            self.mood = "lazy"
        pass

    def drive(self, distance, time):
        # time = 30
        velocity = distance / time
        car.run(distance, velocity)

    def refuel(self, gasAmount=100):

        car.fuelRate += gasAmount

    def send_mail(self, subject, M_from, M_to, recever_name):

        emailcontet = [f"from:{M_from}\n", f"to:{M_to}\n\n", f"{subject}\n",
                       f"HI,{recever_name}\nthis is an email emplate\nthanks"]
        try:
            with open("email1.text", "w") as emailcontent:
                emailcontent.writelines(emailcontet)
        except Exception as e:
            print(e)


# emp1 = Employee(1, "car1", "n_ayman58@yahoo.com", 1500, 40)
# emp1.send_mail("testing", "ayman", "another Ayman", "Ayman")


class office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empid):
        pass

    def hire(self, Employee):
        pass

    def fir(self, emoid):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self, empid, deduction):
        pass

    def reword(self):
        pass


class car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        if velocity in range(0,200):
            self.__velocity = velocity
        elif velocity > 200:
            print(" cant exceed 200")
        elif velocity < 0:
            print("velocity cant be negative number ")

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuelRate):
        if fuelRate in range(0, 100):
            self.__fuelRate = fuelRate
        elif fuelRate > 100:
            print(" cant exceed 100%")
        elif fuelRate < 0:
            print("fuelRate cant be negative number ")

    def run(self, velocity, distance):
        self.velocity = velocity
        # self.fuelRate -= (distance * (0.1 * self.fuelRate)) / 10
        while self.fuelRate > 0 and distance > 0:
            distance -= 10
            self.fuelRate -= 0.1 * self.fuelRate
        if self.fuelRate <= 0 or distance == 0:
            car.stop(self,distance)
        # print(self.velocity)
        # print(distance)
        # print(self.fuelRate)

    def stop(self, distance):
        self.velocity = 0
        if distance > 0:
            print(f"run out of fuel and the remaining distance is {distance}")
        elif distance <= 0:
            print("you arrived the destination ")


# c = car("car1", 90, 50)
# c.run(90, 200)
