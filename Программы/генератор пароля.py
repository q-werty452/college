# игра угадай число
import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 100. Попробуй угадать его.")

secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        q = int(input("Введи число: "))
        attempts = attempts + 1
        if q < secret:
            print("Мое число больше!")
        elif q > secret:
            print("Мое число меньше!")
        else:
            print(f"Поздравляю! Ты угадал число {secret} за {attempts} попыток.")
            break
    except ValueError:
        print("Пожалуйста, введи целое число.")



# генератор пароля
import random
import string

def generate_password(n):
    if n <= 0:
        return ""

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "" 

    for i in range(n):  
        random_char = random.choice(chars) 
        password += random_char            

    return password  


w = int(input("Введите длину пароля: "))
print(generate_password(w))




# Проверка шаблонав
filename = "spam.txt"
url = "http://www.python.org"


if filename.lower().endswith((".txt", ".md", ".py")):
    print("Файл — текстовый, markdown или python")
elif url.startswith(("http://", "https://")):
    print("HTTP(S) URL")


# Палиндромы
def is_palindrome(text):
    q = text.replace(" ", "").lower()
    return q == q[::-1]

w = input("Введите текст: ")
if is_palindrome(w):
    print(f"{w}-палиндром")
    print(w[::-1])
else:
    print(f"{w} - не палиндром")
    print(w[::-1])
is_palindrome(w)

