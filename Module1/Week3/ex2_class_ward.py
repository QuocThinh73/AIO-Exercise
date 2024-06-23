class Student:
    def __init__(self, name: str, yob: int, grade: str):
        self.name = name
        self.yob = yob
        self.grade = grade
        self.job = "Student"

    def describe(self):
        print(
            f"Student - Name : {self.name} - YoB : {self.yob} - Grade : {self.grade}")


class Teacher:
    def __init__(self, name: str, yob: int, subject: str):
        self.name = name
        self.yob = yob
        self.subject = subject
        self.job = "Teacher"

    def describe(self):
        print(
            f"Teacher - Name : {self.name} - YoB : {self.yob} - Subject : {self.subject}")


class Doctor:
    def __init__(self, name: str, yob: int, specialist: str):
        self.name = name
        self.yob = yob
        self.specialist = specialist
        self.job = "Doctor"

    def describe(self):
        print(
            f"Student - Name : {self.name} - YoB : {self.yob} - Specialist : {self.specialist}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.person_list = []

    def add_person(self, student):
        self.person_list.append(student)

    def add_person(self, teacher):
        self.person_list.append(teacher)

    def add_person(self, doctor):
        self.person_list.append(doctor)

    def describe(self):
        print(f"Ward Name : {self.name}")
        for person in self.person_list:
            person.describe()

    def count_doctor(self):
        res = 0
        for person in self.person_list:
            if person.job == "Doctor":
                res += 1
        return res

    def sort_age(self):
        for i in range(len(self.person_list) - 1):
            for j in range(i + 1, len(self.person_list)):
                if (self.person_list[i].yob < self.person_list[j].yob):
                    person_temp = self.person_list[i]
                    self.person_list[i] = self.person_list[j]
                    self.person_list[j] = person_temp

    def compute_average(self):
        total_age = 0
        count = 0
        for person in self.person_list:
            if person.job == "Teacher":
                total_age += person.yob
                count += 1
        return total_age / count


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name=" teacherA ", yob=1969, subject="Math")
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
