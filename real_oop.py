class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_sc(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avg_grade(self):
        grades_list = sum(self.grades.values(), [])
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return (
            f"Имя: {self.name} \n"
            f"Фамилия: {self.surname} \n"
            f"Средняя оценка за домашние задания: {self.avg_grade()} \n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}\n"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        grades_list = sum(self.grades.values(), [])
        return sum(grades_list) / len(grades_list)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg_grade()}"

    def __lt__(self, other):
        return self._avg_grade() < other._avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()


lecturer_1 = Lecturer("Ivan", "Pupsov")
lecturer_1.courses_attached += ["Python"]

lecturer_2 = Lecturer("Moko", "Poko")
lecturer_2.courses_attached += ["Python"]

reviewer_1 = Reviewer("Olga", "Bull")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["C++"]

reviewer_2 = Reviewer("Alina", "Bull")
reviewer_2.courses_attached += ["Python"]
reviewer_2.courses_attached += ["C++"]

student_1 = Student("Katya", "Smirnova")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["C#"]

student_2 = Student("Oleg", "Olegovich")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["C#"]

reviewer_1.rate_hw(student_1, "Python", 3)
reviewer_1.rate_hw(student_1, "Python", 3)
reviewer_1.rate_hw(student_1, "Python", 6)

reviewer_2.rate_hw(student_2, "Python", 2)
reviewer_2.rate_hw(student_2, "Python", 4)
reviewer_2.rate_hw(student_2, "Python", 6)

student_1.rate_sc(lecturer_1, "Python", 8)
student_1.rate_sc(lecturer_1, "Python", 9)
student_1.rate_sc(lecturer_1, "Python", 10)

student_1.rate_sc(lecturer_2, "Python", 8)
student_1.rate_sc(lecturer_2, "Python", 9)
student_1.rate_sc(lecturer_2, "Python", 10)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def student_rating(course):
    avg_grade_student = []
    for student in student_list:
        for course1, grades in student.grades.items():
            if course == course1:
                avg_grade_student.extend(grades)
                new_z: float = sum(avg_grade_student) / len(avg_grade_student)
                return f"{new_z}"
            else:
                return


def lecturer_rating(course):
    avg_grade_lecturer = []
    for lecturer in lecturer_list:
        for course1, grades in lecturer.grades.items():
            if course == course1:
                avg_grade_lecturer.extend(grades)
                new_z: float = sum(avg_grade_lecturer) / len(avg_grade_lecturer)
                return f"{new_z}"
            else:
                return


print(lecturer_1, reviewer_1, student_1, "\n")  ## проверка на __str__
print()
print(
    student_1 < student_2, student_1 > student_2, lecturer_2 == lecturer_1, sep="\n"
)  ## проверка на методы сравнения
print()
print(f"Средняя оценка всех студентов курса 'Python' - {student_rating('Python')}")
print()
print(f"Средняя оценка всех лекторов курса 'Python' - {lecturer_rating('Python')}")
