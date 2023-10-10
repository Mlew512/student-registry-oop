import re


class Student:
    def __init__(self, name: str, age: int, grade: str, id: int):
        self._id = id
        self._name = name
        self._age = age
        self._grade = grade
        self._subjects = []

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age

    @property
    def get_grade(self):
        return self._grade

    @get_name.setter
    def set_name(self, name: str):
        if type(name) == str:
            pattern = "^[A-Z][a-z]{2,}$"
            if re.match(pattern, name):
                self._name = name

    @get_age.setter
    def set_age(self, age: int):
        if type(age) == int:
            if age > 11 and age < 18:
                self._age = age

    @get_grade.setter
    def set_grade(self, grade: str):
        if type(grade) == str:
            pattern = "^(9|10|11|12)th$"
            if re.match(pattern, grade):
                self._grade = grade

    def __str__(self):
        return f"Student {self._id}, Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    def study(self, subject: str):
        self._subjects.append(subject)
        return f"{self._name} is studying {', '.join(self._subjects)}"

    def advance(self, years: int):
        current_grade = self.get_grade
        if len(current_grade) == 3:
            self.set_grade = str(int(current_grade[0]) + years) + "th"
        if len(current_grade) == 4:
            self.set_grade = str(int(current_grade[0:2]) + years) + "th"
        return f"{self._name} has advanced to the {self._grade} grade"


student1 = Student("Megan", 38, "10th", 1)
student1.set_name = "Megan Buck"
print(student1.advance(1))
