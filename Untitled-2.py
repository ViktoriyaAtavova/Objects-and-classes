class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._Student__avarage_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    
    def __lt__(self, other):
        return self._Student__avarage_grade < other._Student__avarage_grade
    
    def __avarage_grade(self):
        rating = 0
        countlen = 0
        for marks in self.grades.values():
            countlen += len(marks)
            for mark in marks:
                rating += mark
        avarage_marks = rating / countlen
        return avarage_marks      
            
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._Lecturer__avarage_grade()}"
    
    def __lt__(self, other):
        return self._Lecturer__avarage_grade < other._Lecturer__avarage_grade
    
    def __avarage_grade(self):
        rating = 0
        countlen = 0
        for marks in self.grades.values():
            countlen += len(marks)
            for mark in marks:
                rating += mark
        avarage_marks = rating / countlen
        return avarage_marks 

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


lecturer_1 = Lecturer('Den', 'Franklin')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['JavaScript']
lecturer_2 = Lecturer('Nina', 'Skott')
lecturer_2.courses_attached += ['JavaScript']
lecturer_2.courses_attached += ['Python']


student_1 = Student('Amy', 'Shou', 'f')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JavaScript']
student_1.add_courses('Web-Дизайнер')
student_1.rate_lect(lecturer_1, 'Python', 8)
student_1.rate_lect(lecturer_1, 'Python', 5)
student_1.rate_lect(lecturer_2,'Python', 9)
student_2 = Student('Nick', 'Din', 'm')
student_2.courses_in_progress += ['JavaScript']
student_2.courses_in_progress += ['Python']
student_2.add_courses('Тестировщик')
student_2.rate_lect(lecturer_2, 'JavaScript', 7)
student_2.rate_lect(lecturer_2, 'JavaScript', 8)
student_2.rate_lect(lecturer_1, 'JavaScript', 7)

reviewer_1 = Reviewer('Alexandr', 'Done')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['JavaScript']
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'JavaScript', 8)
reviewer_1.rate_hw(student_2, 'JavaScript', 7)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_2 = Reviewer('Lisa', 'Decker')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['JavaScript']
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'JavaScript', 7)
reviewer_2.rate_hw(student_2, 'JavaScript', 5)
reviewer_2.rate_hw(student_2, 'Python', 8)

print(lecturer_1)
print(lecturer_2)
print(student_1)
print(student_2)
print(reviewer_1)
print(reviewer_2)


def avarage_student(students: list, course):
    all_grades = 0
    countlen = 0
    for student in students:
        if isinstance(student, Student):
            countlen +=1
            for grades in student.grades[course]:
                all_grades += grades
    middle_mark_course = (all_grades / countlen) / len(students)
    return middle_mark_course

print(avarage_student([student_1, student_2], 'Python'))

def avarage_lecturer(lecrurers: list, course):
    all_grades = 0
    countlen = 0
    for lecturer in lecrurers:
        if isinstance(lecturer, Lecturer):
            countlen +=1
            for grades in lecturer.grades[course]:
                all_grades += grades
    middle_mark_course = (all_grades / countlen) / len(lecrurers)
    return middle_mark_course  

print(avarage_lecturer([lecturer_1, lecturer_2], 'JavaScript'))