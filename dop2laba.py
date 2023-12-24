while True:
    try:
        def decimal_to_octal(number):
            # Проверяем, является ли число отрицательным
            is_negative = False
            if number < 0:
                is_negative = True
                number = -number
            # Преобразуем число в восьмеричную систему счисления
            octal = ""
            while number > 0:
                octal = str(number % 8) + octal
                number = number // 8
            # Если число было отрицательным, применяем дополнительный код
            if is_negative == True:
                octal = "1" + octal

            return octal
        number = int(input("Введите число в десятичной системе счисления: "))
        octal_number = decimal_to_octal(number)
        print("Число", number, "в восьмеричной системе счисления в дополнительном коде: ", octal_number)
    except:
        print('ERROR! Try again!')
