while True:
    try:
        def decimal_to_octal(n):
            # Проверяем, является ли число отрицательным
            is_negative = False
            if n < 0:
                is_negative = True
                n = -n
            # Преобразуем число в восьмеричную систему счисления
            octal = ""
            while n > 0:
                octal = str(n % 8) + octal
                n = n // 8
            # Если число было отрицательным, применяем дополнительный код
            if is_negative:
                octal = "1" + octal

            return octal
        number = int(input("Введите число в десятичной системе счисления: "))
        octal_number = decimal_to_octal(number)
        print("Число", number, "в восьмеричной системе счисления в дополнительном коде: ", octal_number)
    except:
        print('ERROR! Try again!')