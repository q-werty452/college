#  Создай класс Book, который описывает книгу.
# title — название книги
# author — автор
# year — год издания
# is_available — доступна ли книга в библиотеке (по умолчанию True)
# info() — выводит информацию о книге в виде:
# "Название: <title>, Автор: <author>, Год: <year>"
# borrow() — если книга доступна, делает is_available = False
# return_book() — делает is_available = True


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Доступна: {self.is_available}")

    def borrow(self):
        if self.is_available == True:
         self.is_available = False
        print("Книга взята она теперь недоступна")
        print(f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Доступна: {self.is_available}")


    def return_book(self):
        self.is_available = True
        print("Книга возвращена она теперь доступна")

book1 = Book("Война и мир", "Лев Толстой", 1869)
book1.info()
# # book1.borrow()
# # book1.return_book()
# # book1.info()






















# 2) Создай класс Student и класс Course
# класс Student
# name
# group
# метод enroll(course) — записывает студента на курс
# класс Course
# name
# students — список студентов
# метод add_student(student) — добавляет студента в курс

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def enroll(self, course):
        course.add_student(self)

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def info(self):
        print(self.students)

student1 = Student("Ахмед", "ПКС-01-25")
course1 = Course("2-ой курс")
course1.add_student("Gena ")
course1.info()





