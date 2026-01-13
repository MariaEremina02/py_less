#task3
#1
number = int(input())
for current_number in range(1, number + 1):
    print(current_number)

#2
number = 10
for repeat_count in range (20):
    print (number)

#3
number = int(input())
sum_numbers = 0
for current_number in range(1, number + 1):
    if current_number % 2 == 0:
        sum_numbers += current_number
print(sum_numbers)

#4
number = input()
even_numbers = 1
for digit_symbol in number:
    digit_symbol = int(digit_symbol)
    if digit_symbol % 2 == 0 and digit_symbol != 0:
        even_numbers *= digit_symbol
print(even_numbers)

#5
number = int(input())
factorial = 1
for i in range(1, number + 1):
    factorial *= i
    print(factorial, end=' ')

#6
number = int(input())
first_number = 1
while first_number * first_number < number:
    square = first_number * first_number
    first_number +=1
    print(square)

#7
number = input()
sum_num = 0
for digit_symbol in number:
    sum_num += int(digit_symbol)
print(sum_num)

#8
number = input()
min_number = int(number[0])
for digit_symbol in number:
    digit_symbol = int(digit_symbol)
    if digit_symbol < min_number:
        min_number = digit_symbol
print (min_number)

#9
text = input("Напишите, пожалуйста, что-нибудь:")
print(text.replace(",", " "))

#10
number = int(input())
for cow_count in range(1, number + 1):
    if cow_count % 10 == 1 and cow_count % 100 != 11:
        word = "Корова"
    elif 2 <= cow_count % 10 <= 4 and not  (12 <= cow_count % 100 <= 14):
        word = "Коровы"
    else:
        word = "Коров"
print("На лугу", cow_count, word)

#task4
#1
numbers = tuple(map(int, input().split()))
max_number = max(numbers)
min_number = min(numbers)
diff = max_number - min_number
print(diff)

#2
numbers = tuple(map(int, input().split()))
change_count = 0
for i in range (1, len(numbers)):
    if numbers[i - 1] * numbers[i] < 0:
        change_count += 1
print(change_count)

#3
numbers = tuple(map(int, input().split()))
for number in numbers:
    if number > 1:
        flag = True
        for divider in range(2, number):
            if number % divider == 0:
                flag = False
                break
        if flag:
            print(number, end='')

#6
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))
not_included = []
for number in first_list:
    if number not in second_list:
        not_included.append(number)
if not_included:
    print(min(not_included))
else:
    print("Данного элемента не существует")

#7
list_1 = list(map(int, input().split()))
result = []
for number in list_1:
    result.append(number)
    if number % 2 == 0:
        reversed_number = int(str(number)[::-1])
        result.append(reversed_number)
print(result)

#8
list_1 = list(map(int, input().split()))
checked = []
for number in list_1:
    if number not in checked:
       count = 0
       for element in list_1:
            if element == number:
                count += 1
        checked.append(number)
print(number, "-", count)

#11
numbers = list(map(int, input().split()))
seen_numbers = set()
for number in numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)

#12
August_number = int(input("Август загадал число:"))
possible_numbers = set(range(1, August_number + 1))
while True:
    question = input().strip()
    if question == 'help':
        break
    parts = question.split()
    numbers,answer = parts
    numbers = set(map(int,numbers[-1]))
    if answer == "YES":
        possible_numbers &= numbers
    else:
        possible_numbers -= numbers
print(sorted(possible_numbers))

#13
school = {"9a":7, "9b":15, "9c":9}
school["9a"] = 10
school["9d"] = 20
del school["9c"]
total_students = sum(school.values())
print(total_students)

#14
dict = {}
while True:
    line = input()
    if line == '.':
        break
    term, definition = line.split(' – ')
    term = term.strip()
    definition = definition.strip()
    dict[term] = definition
request_count = int(input())
for _ in range(request_count):
    request = input().strip()
    if request in dict:
        print(dict[request])
    else:
        print("Не найдено")
#изменения