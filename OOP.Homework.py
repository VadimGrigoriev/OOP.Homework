class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _rating(self):
        res = [num for val in self.grades.values() for num in val]
        return round(sum(res) / len(res), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {self._rating()}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка! Классы не соответствуют!")
            return
        if self._rating() == other._rating():
            return 'Средний балл одинаковый\n'
        return self._rating() < other._rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _rating(self):
        res = [num for val in self.grades.values() for num in val]
        return round(sum(res) / len(res), 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self._rating()}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка! Классы не соответствуют!")
            return
        if self._rating() == other._rating():
            return 'Средний балл одинаковый\n'
        return self._rating() < other._rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


def average_stud_score(list_stud, course):
    result = []
    for student in list_stud:
        for st_course, score in student.grades.items():
            if st_course == course:
                result += score
    if not result:
        return f'У студентов нет курса "{course}"\n'
    else:
        return f'Средняя оценка за ДЗ по всем студентам - {round(sum(result) / len(result), 1)}, по курсу "{course}"\n'


def average_lect_score(list_lect, course):
    result = []
    for lecturer in list_lect:
        for lect_course, score in lecturer.grades.items():
            if lect_course == course:
                result += score
    if not result:
        return f'У лекторов нет курса "{course}"\n'
    else:
        return f'Средняя оценка за лекции по всем лекторам - {round(sum(result) / len(result), 1)}, ' \
               f'по курсу "{course}"\n'


student_1 = Student('Andrey', 'Burtsev', 'male')
student_1.finished_courses += ['Java', 'PHP']
student_1.courses_in_progress += ['Python', 'Go']

student_2 = Student('Vadim', 'Grigoriev', 'male')
student_2.finished_courses += ['C++', 'JavaScript']
student_2.courses_in_progress += ['Python', 'C#']

lecturer_1 = Lecturer('Dmitry', 'Vasiliev')
lecturer_1.courses_attached += ['Python', 'Go']

lecturer_2 = Lecturer('Pavel', 'Ivanov')
lecturer_2.courses_attached += ['Python', 'C#']

reviewer_1 = Reviewer('Alexander', 'Ilyin')
reviewer_1.courses_attached += ['Python', 'Go', 'C#']

reviewer_2 = Reviewer('Oleg', 'Ivanov')
reviewer_2.courses_attached += ['Python', 'Go', 'C#']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Go', 8.7)
reviewer_1.rate_hw(student_2, 'C#', 8.1)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'C#', 9.8)
reviewer_2.rate_hw(student_1, 'Go', 8.6)

student_1.rate_lect(lecturer_2, 'Python', 10)
student_1.rate_lect(lecturer_1, 'Go', 8.9)
student_1.rate_lect(lecturer_1, 'Go', 9.5)

student_2.rate_lect(lecturer_1, 'Python', 9.2)
student_2.rate_lect(lecturer_2, 'C#', 8.8)
student_2.rate_lect(lecturer_2, 'C#', 9.9)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print(student_1)
print(student_2)

print(student_1 < student_2)
print(lecturer_1 > lecturer_2)

print(average_stud_score([student_1, student_2], 'Python'))
print(average_stud_score([student_1, student_2], 'C#'))
print(average_stud_score([student_1, student_2], 'Go'))

print(average_lect_score([lecturer_1, lecturer_2], 'Python'))
print(average_lect_score([lecturer_1, lecturer_2], 'C'))
print(average_lect_score([lecturer_1, lecturer_2], 'Go'))
