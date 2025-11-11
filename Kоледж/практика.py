# Практика

                                                                # 05.09.2025 пятница

# переменные

summa = 32000 + 5500

print( summa - ( summa * 15 / 100 ) )

q=2
w="У вики"
e="коробки по"
r="маркеров. Сколко всего маркеров?  "
t="Всего маркеров:"
y=6
print(w,q,e,y,r,t,q*y)


# my name = "john"
# my.name = "john"
# my*name = "john"
# my(name) = "john"
# my+name = "john"
my=name = "john"
print(my)
print(name)
print(my+name)








                                                             # 08.09.2025 понедельник

# канкатенация строк

name = "john"
prof = "student"
bio = "my name is " + name + ", i am " + prof
print(bio)

name = "john"
prof = "student"
age = 25
bio = "my name is " + name + ", i am " + prof  + " and i am " + str(age) + " years old"
# конкатенация строк - это склеивание строк с помощью +
print(bio)

# индексы - это порядковый номер элемента в строке
# индексы начинаются с 0

bio2 = "my name is {0}, i am {1} and i am {2} years old".format(name, prof, age)
print(bio2)


# f строки - это форматированные строки
bio3 = f"my name is {name}, i am {prof} and i am {age} years old"
print(bio3)

# f строки - это самый удобный способ форматирования строк
# в f строках можно использовать любые выражения внутри {} 





# Индекс - это файл, который выполняется первым в папке.

name = " Привет я ахмед !"
print(name[0:17:3])
print(name[0])  # срез строки [начало:конец:шаг]









                                                                           # 09.09.2025 вторник
# Задание 1:
# Написать программу для военкомата, которая запрашивает у пользователя его возраст 

age = int(input("Введите ваш возраст: "))
if age < 16:
    print("Вы еще молоды, вам рано в армию.")
elif age >= 16 and age < 18:
    print("Готовся, скоро в армию.")
elif age >= 18 :
    print("В армию пора!")
elif age > 40:
        print("пора на пенсию.")
elif age > 60:
            print("Отдыхай.")


#  Сделать   программу которая принимает число и показывать что она четная или не четная

num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное.")
else:
    print("Число нечетное.")



                                                                                    # 12.09.2025

# Надо сделать программу которая будет спрашивать наше действия как в телефонной книжке ,
# Есть 3 действия 
# 1 Добавить новый контакт в наш список 
# 2 удолить имя изконтактов 
# 3 поискимени в списке контактов

contacts = ["Aliya","Davlet","Ahmed","Islam"]
num_reg = input("Что вы хотите сделать?\n1-Добавить контакт\n2-Удалить контакт\n3-Поиск контакта\nВыберите действие:")

if num_reg == "1":
    new_name = input("Ведите имя:").title()
    contacts.append(new_name)
    print(contacts)
elif num_reg == "2":
    print(contacts)
    del_name = input("Ведите имя для удоления:").title()
    contacts.remove(del_name)
    print(contacts)
elif num_reg == "3":
    serch_name = input("Какое имя вы ищете:").title()
    if serch_name in contacts :
        print(contacts)
        print(serch_name,"- Это имя есть в ваших контактах") 
        if serch_name not in contacts :
            print(serch_name,"-Этого имени нет в ваших контактах")


                                                                                      #  15.09.25 Понедельник


# Циклы

# пример
for i in range(3, 8): # 3, 4, 5, 6, 7
  print(i)

# for обратный отсчет
for i in range(5, 0, -1): # 5, 4, 3, 2, 1
  print(i)

# for по строке
word = "apple"

for i in word:
  print(i)

# for с шагом 2
for i in range(0, 11, 2):
  print(i)

# Условия внутри for
for i in range(1, 11):
  if i % 2 == 0:
    print(i)

# Таблица умножения
for a in range(1, 10):
  for b in range(1, 10):
    print(f"{a} * {b} = {a * b}")
  print("========")

# Таблица умножения на определенное число
x = int(input("Введите число: "))

for i in range(1, 10):
  print(f"{x} * {i} = {x * i}")



# Примеры с методами строк
q = []
for w in range (1,101,2) :
    q.append(w)

print(q)

#  2-ой пример
q = "a1p2p3l4e"
w = []
for e in q :
    if e.isdigit():
        w.append(e)
print(w)


                                                                # 26.09.2025

# Функции 


# Программа калькулятор: + - * /
def calculator():
  while True:
    try:
      a = float(input("Введите первое число: "))
    except ValueError:
      print ("Только числа!")
      continue
    op = input("Введите операцию (+, -, *, /): ")
    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Только числа!")
        continue
  
    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
          try:
           print("Результат:", a / b)
          except ZeroDivisionError:
             print("На ноль делить нельзя")
             continue
    else:
        print("Ошибка: неизвестная операция.")
  
  calculator()

                                                    # 14.10.25 вторник


# lambda - это способ создания анонимных функций в Python. Анонимные функции - это функции, которые не имеют имени и обычно используются для кратковременных операций.


# 1 Отфилтровать заказы длинее 4 символов
orders = ["apple", "banana", "kiwi", "pear", "grape", "orange"]
long_orders = list(filter(lambda order: len(order) > 4, orders))
print(long_orders)  

# 2 заказы начинаюшиеся на букву 'a'
orders = ["apple", "banana", "kiwi", "pear", "grape", "orange"]
a_orders = list(filter(lambda order: order.startswith('a'), orders))

# 3 преобразовать все заказы в верхний регистр
orders = ["apple", "banana", "kiwi", "pear", "grape", "orange"]
upper_orders = list(map(lambda order: order.upper(), orders))
print(upper_orders)



q = [
    {"названия":"кофе","цена": 120, "категория": "напиток"},
    {"названия":"чай","цена": 80, "категория": "напиток"},
    {"названия":"сок","цена": 150, "категория": "напиток"},
    {"названия":"пицца","цена": 500, "категория": "еда"},
    {"названия":"бургер","цена": 120, "категория": "еда"},
    {"названия":"торт","цена": 300, "категория": "десерт"},
    {"названия":"мороженое","цена": 200, "категория": "десерт"},
    {"названия":"плов","цена": 500, "категория": "основное"},

    
]

# 1 Ввывести те блюда которые дороже 150 
expensive_dishes = list(filter(lambda dish: dish["цена"] > 150, q))
print(expensive_dishes)
# Найти самое дорогое блюдо
most_expensive_dish = max(q, key=lambda dish: dish["цена"])
print(most_expensive_dish)
# отсортировать блюда по цене
sorted_dishes = sorted(q, key=lambda dish: dish["цена"])
print(sorted_dishes)
# Проверить есть ли хоть одно блюдо , где категория десерт
has_dessert = any(dish["категория"] == "десерт" for dish in q)
print(has_dessert)






                                                                     # 21. 10.2025 вторник

# ООП - объектно ориентированное программирование 

class Animal: # Родительский класс . У которого общие параметры для всех дочерних классов
    def __init__(self, name, age, color,gender): # параметры
        self.name = name # атрибуты
        self.age = age
        self.color = color
        self.gender = gender

    def set_name(self, new_name):
        self.name = new_name
    def info (self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color}, Пол: {self.gender}")

class Cat(Animal): # Дочерний класс
    def mau(self):
        print("Мяу мяу!")

class Dog(Animal): # Дочерний класс
    def gav(self):
        print("Гав гав!")

class Lion(Animal): # Дочерний класс
    def roar(self):
        print("Рррр!")

cat1 = Cat("Барсик", 3, "рыжий","самец")
dog1 = Dog("Шарик", 5, "черный","самец")
lion1 = Lion("Симба", 7, "золотой","самец")
lion2 = Lion("Нала", 6, "золотой","самка")
lion3 = Lion("Муфаса", 10, "темно-золотой","самец")
lion3.set_name("Шрам")
cat1.mau()
dog1.gav()
lion1.roar()
cat1.info()
dog1.info()
lion1.info()