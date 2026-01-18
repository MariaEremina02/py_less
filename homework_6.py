#1
x = (1, 2, 5, 7)
try:
    x = x / 2
    print(x)
except TypeError as error:
    print("Ошибка:", error)

#2
numbers = [10, 23, 44, 66, 51]
try:
    print (numbers [77])
except IndexError:
    print ("Элемента нет в списке")

#3
import math
side_a = float(input("Введите сторону А: "))
side_b = float(input("Введите сторону B: "))
side_c = float(input("Введите сторону C: "))
try:
    if side_a ==0 or side_b==0 or side_c==0:
        raise ArithmeticError ("Сторона треугольника не может быть равна 0!!!")
    perimeter = (side_a + side_b + side_c)/2
    area = math.sqrt (perimeter * (perimeter - side_a) * (perimeter - side_b) * (perimeter - side_c))
    print ("Площадь треугольника равна:", area)
except ArithmeticError as error:
    print ("Ошибка:", error)

#4
numbers = [1, 31, 44, 55, 68]
remove_one_element = 10
try:
    if remove_one_element not in numbers:
        raise TypeError("Элемента нет в списке. Удалить невозможно")
    numbers.remove(remove_one_element)
except TypeError as error:
    print ("Ошибка:", error)

#5
data_dictionary = {"processore" : "amd ryzen 9", "ram" : 32}
key_to_find = "graphics card"
try:
    if key_to_find not in data_dictionary:
        raise KeyError ("Данный ключ отсутствует в словаре")
    print (data_dictionary[key_to_find])
except KeyError as error:
    print ("Ошибка:", error)

#6
string = "10 5 abc 3"
elements = string.split()
total_sum = 0
for element in elements:
   try:
        number = int(element)
        total_sum += number
    except ValueError:
        pass
print ("Сумма равна:", total_sum)

#7
string = "aaa bb ss rra aa b"
try:
    if not isinstance(string, str):
        raise TypeError ("Данные должны быть в значении строка")
    letter_frequency = {}
    for symbol in string:
        if symbol != " ":
            letter_frequency[symbol] = letter_frequency.get(symbol, 0) + 1
    for letter, count in letter_frequency.items():
        print(letter, count)
except TypeError:
    print ("TypeError")