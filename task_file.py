# задачи на работу с файлами питон
#
# Во входном файле записано два целых числа, которые могут быть разделены пробелами и концами строк.
#
# Выведите в выходной файл их сумму.
#
# Указание. Считайте весь файл в строковую переменную при помощи метода read()
#
# и разбейте ее на части при помощи метода split().

def file_task1(file1, file1_result):
    summa = 0
    with open(file1, 'r') as f:
        int_number = f.read()
        print(int_number)
        a = int_number.split()
        print(a)
        for i in a:
            i = int(i)
            summa += i
    print(summa)
    with open(file1_result, 'w') as f:
        f.write(str(summa))


file_task1("task1_file.txt", "task1_file_result.txt")

# Во входном файле записана одна текстовая строка, возможно, содержащая пробелы.
#
# Выведите эту строку в обратном порядке.
#
# Строка во входном файле заканчивается символом конца строки '\n'.

def file_task2():
    with open('task2_file.txt', 'r') as f:
        string = f.read()
        print(string)
        reversed_string = string[::-1]
        print(reversed_string)

# file_task2()

# Выведите все строки данного файла в обратном порядке.
#
# Для этого считайте список всех строк при помощи метода readlines().
#
# Последняя строка входного файла обязательно заканчивается символом '\n'.

def file_task3():
    with open('task3_file.txt', 'r') as f:
        srting = f.readlines()
        for i in reversed(srting):
            print(i)

# file_task3()

# Выведите в обратном порядке содержимое всего файла полностью.
#
# Для этого считайте файл целиком при помощи метода read().

def file_task4():
    with open('task4_file.txt', 'r') as f:
        string = f.read()
        print(string)
        reversed_string = string[::-1]
        print(reversed_string)

# file_task4()

# В выходной файл выведите все строки наибольшей длины из входного файла, не меняя их порядок.
#
# В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().

def file_task5():
    maxs_lens = 0
    maxs = ""
    with open('task5_file.txt', 'r') as f:
        string = f.readlines()
        string = [line.rstrip() for line in string]
        print(string)
        for i in string:
            a = len(i)
            print(a)
            if a > maxs_lens:
                maxs_lens = a
                maxs = i + "\n"
            elif a == maxs_lens:
                maxs += i
    print(maxs)

# file_task5()

# Определите, есть ли во входном файле символ '@'. Выведите слово YES или NO.
#
# Входной файл может быть очень большим, поэтому считывать файл нужно посимвольно.

def file_task6():
    with open('task6_file.txt', 'r') as f:
        string = f.readlines()
        symbols  = []
        result =  ""
        for symbol in string:
            symbols += symbol
        for symbol in symbols:
            print(symbol)
            if symbol == "@":
                result = "Yes"
        if result != "Yes":
            result = "No"
    print(result)

file_task6()
