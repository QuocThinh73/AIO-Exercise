from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.__name = name
        self.__yob = yob

    def get_name(self):
        return self.__name

    def get_yob(self):
        return self.__yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name : {self.get_name()} - YoB : {self.get_yob()} - Grade : {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name : {self.get_name()} - YoB : {self.get_yob()} - Subject : {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name : {self.get_name()} - YoB : {self.get_yob()} - Specialist : {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []

    def add_person(self, person: Person):
        self.__person_list.append(person)

    def describe(self):
        print(f"Ward Name : {self.__name}")
        for person in self.__person_list:
            person.describe()

    def count_doctor(self):
        res = 0
        for person in self.__person_list:
            if isinstance(person, Doctor):
                res += 1
        return res

    def sort_age(self):
        for i in range(len(self.__person_list) - 1):
            for j in range(i + 1, len(self.__person_list)):
                if (self.__person_list[i].get_yob() < self.__person_list[j].get_yob()):
                    person_temp = self.__person_list[i]
                    self.__person_list[i] = self.__person_list[j]
                    self.__person_list[j] = person_temp

    def compute_average(self):
        total_age = 0
        count = 0
        for person in self.__person_list:
            if isinstance(person, Teacher):
                total_age += person.get_yob()
                count += 1
        return total_age / count


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA ", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.add_person(teacher2)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
