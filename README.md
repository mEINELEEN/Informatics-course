Доп ко 2 лабе. 
Доп осуществляет перевод числа в восьмеричную систему счисления при помощи дополнительного кода.
Описание программы:   
  Начинаем писать программу с цикла (while True), что позволяет нам бесконечно выполнять работу алгоритма, при том условии, что пользователь не допускает ошибки при вводе. В цикл (while True) вставляем операторы try и except, чтобы при допуске ошибки, программа сообщала на экран, что допущена ошибка при вводе.
  Далее задаём функцию decimal_to_octal, зависящую от number. Создаём переменную is_negative и присваиваем ей False.Осуществляем проверку числа: если     number < 0, то присваем переменной (is_negative) True и превращаем наше число в положительное: number = -number. Преобразуем number в число восьмеричной системы счисления: задаём пустую запись octal и начинаем цикл (while number > 0), и он будет работать, пока число (number) не станет меньше, чем 0. В нашу запись (octal) добавляем запись остатка числа (number) деленного на 8, число (number), в свою очередь, делим без остатка на 8, чтобы число уменьшалось, и цикл (while number > 0), спустя время, завершил работу.
  Если наше число (number) было изначально отрицательным, и наша переменная (is_negative) хранит в себе True, то мы используем дополнительный код и добавляем к нашей записи (octal) 1 слева. Возвращаем запись (octal).
  А если наше число (number) изначально положительное, то мы оставляем неизменной переменную (is_negative) и просто переводим число (number) в число восьмеричной системы счисления путём, указанным выше. Возвращаем запись (octal).
  Задаём число (number), которое вводится пользователем, задаём переменную (octal_number), которая будет хранить в себе функцию decimal_to_octal(number). Выводим (octal_number). 
  Конец программы.
