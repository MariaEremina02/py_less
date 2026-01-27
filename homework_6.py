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

#homeworf func
#1
def min_of_two (a, b):
   if a < b:
       return a
   else:
       return b
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
min1 = min_of_two(number1, number2)
min2 = min_of_two(number2, number3)
min_of_4 = min_of_two (min1, min2)
print (min_of_4)

#2
number = int(input())
sum = 0
for divisor in range(1, number):
   if number % divisor == 0:
       sum += divisor
if sum == number:
   print ("YES")
else:
   print ("NO")

#3
def fib (n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   previous_number = 0
   current_number = 1
   for i in range (2, n + 1):
       next_number = previous_number + current_number
       previous_number = current_number
       current_number = next_number
   return next_number
n = int(input())
print(fib(n))

#4
def closest_mod_5 (num):
   after_division = num % 5
   if after_division == 0:
       return num
   else:
       return num + (5 - after_division)
x = int(input())
print(closest_mod_5(x))

#5
def check_variable (variable_name):
   if variable_name[0].isdigit():
       return False
   forbidden_symbols = ": ! @ # $ % ^ & * ()"
   for symbol in variable_name:
       if not (symbol.isdigit() or symbol == "_"):
           return False
       if symbol in forbidden_symbols:
           return False
   return True
while True:
   user_input = input()
   if user_input == "Поработали, и хватит":
       break
   if check_variable(user_input):
       print("Можно использовать")
   else:
       print ("Нельзя использовать")

#6
digit_num =[]
for number in range(11, 100, 2):
   digit_num.append(number)
print(digit_num)

#7
numbers =[]
for num in range (100, 1000)
   if number % 3 == 0 and number % 5 == 0:
       numbers.append(num)
print(numbers)

#8
def unique_elem(sorted_list):
   if len(sorted_list) == 0:
       return 0
   unique_count = 1
   for index in range (1, len(sorted_list)):
       if sorted_list[index] != sorted_list[index-1]:
           unique_count += 1
   return unique_count
numbers = list(map(int, input().split()))
print (unique_elem(numbers))

#9
numbers = list(map(int, input().split()))
lenght = len(numbers)
if lenght == 1:
   print(numbers[0])
else:
   result = []
   for i in range(lenght):
       left_neighbor = numbers[i - 1]
       right_neighbor = numbers[(i + 1) % lenght]
       result.append(left_neighbor + right_neighbor)
   print(*result)

#decorators
#1
def log_result(function):
   def wrapper(number):
       result = function(number)
       print(result)
       return result
   return wrapper
@log_result
def square(number):
   return number * number
square(int(input()))

#2
def repeat(n):
   def decorator_repeat(func):
       def wrapper():
           result = None
           for _ in range(n):
               result = func()
           return result
       return wrapper
   return decorator_repeat
@repeat(int(input()))
def hello_world():
   print('Hello World!')
   return "nice!"
final_result = hello_world()
print(f"Last resul: {final_result}")

#3
def bench (func):
   def wrapper():
       try:
           return func()
       except Exception as error:
           print("Type of error:", type(error).__name__)
           print("Сообщение:", error)
   return wrapper()
@bench
def divide_by_zero():
   return 100/0
divide_by_zero()

#4
words = ["keyboard", "mouse", "processor"]
word_lengths = list(map(len, words))
print(word_lengths)

#5
words = ['apple', 'Banana', 'cherry', 'DATE']
lowercase_words = list(filter(str.islower, words))
print(lowercase_words)

#6
people =[("Карина", 14),("Дмитрий", 37), ("Екатерина", 22)]
adults = list(filter(lambda person: person[1] > 18, people))
print(adults)

#7
from functools import reduce
lists = [[1,2],[3,4],[5,6]]
next_list = reduce(lambda x,y: x+y, lists)
print(next_list)

#8
list = ['cat','car','mouse','dog','snake','cow']
result = {}
for word in list:
   first_letter = word[0]
   if first_letter not in result:
       result[first_letter] = []
   result[first_letter].append(word)
print(result)

#9
products = [("milk", 2, 5), ("bread", 1, 3), ("cola", 4, 10)]
total_price = list(map(lambda product: product[1] * product[2], products))
print(total_price)