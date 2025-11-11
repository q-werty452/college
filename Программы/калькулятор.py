#  создать калькулятор  с оброботкай ошибок 

while True:
        try:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            operation = input("Введите операцию (+, -, *, /): ")

            if operation == "+":
                print (x + y)
            elif operation == "-":
                print (x - y)
            elif operation == "*":
                print (x * y)
            elif operation == "/":
                print (x / y)
            elif operation == "**":
                print (x ** y)
            elif operation == "//":
                print (x //y )
            elif operation == "%":
                print (x % y)
                
            else:
                print("Некорректная операция.")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
        except ValueError:
            print("Ошибка: Введите корректное число!")
