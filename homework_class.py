#1
class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def show(self):
        print(self.num1, self.num2)
    def change (self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2
    def max_number(self):
        if self.num1 > self.num2:
            return self.num1
        else:
            return self.num2
n = Numbers(34, 56)
n.show()
print("Сумма:", n.sum())
print("Большее число:", n.max_number())

#2
class Counter:
    def __init__(self):
        self.value = 0

    def plus(self):
        self.value += 1

    def minus(self):
        self.value -= 1
c = Counter()
print("Начало:", c.value)
c.plus()
print("После увеличения:", c.value)
c.minus()
print("После уменьшения:", c.value)

#3
class Shop:
    def __init__ (self):
        self.products = []
    def add(self, name):
        self.products.append(name)
    def remove(self, name):
        self.products.remove(name)
    def find(self, name):
        if name in self.products:
            return True
        else:
            return False
shop = Shop()
shop.add("Молоко")
shop.add("Хлеб")
shop.add("Бананы")
print ("Товары в магазине:", shop.products)
print("Есть ли хлеб?", shop.find("Хлеб"))
print("Есть ли сыр?", shop.find("Сыр"))
shop.remove("Хлеб")
print("После удаления хлеба:", shop.products)

#4
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0
    def can_add(self, money):
        if self.coins + money >= self.capacity:
            return True
        else:
            return False
    def add(self, money):
        self.coins += money
box = MoneyBox(25)
print ("Монет на данный момент:", box.coins)
if box.can_add(23):
    box.add(23)
print ("После добавления:", box.coins)
if box.can_add(5):
    box.add(5)
else:
    print("Нельзя добавить 6 монет — копилка переполнится")

#class2
#1
from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CashPayment(PaymentMethod):
    def pay(self, amount):
        print (f"Оплата наличными суммой: {amount} рублей")
class CardPayment(PaymentMethod):
    def pay(self, amount):
        print (f"Оплата картой суммой: {amount} рублей")
class ApplePayPayment(PaymentMethod):
    def pay(self, amount):
        print (f"Оплата Apple Pay: {amount} рублей")
def process_payment(payment_method, amount):
    payment_method.pay(amount)
payments = [
    CashPayment(),
    CardPayment(),
    ApplePayPayment(),
]
for payment in payments:
    process_payment(payment, 50000)

#2
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class TelegrammNotification(Notification):
    def __init__(self, video_msg):
        self.video_msg = video_msg
    def send(self, message):
        print (f"Telegramm: someone sent you a video message {self.video_msg}. {message}")

class InstagramNotification(Notification):
    def __init__(self, reels):
        self.reels = reels
    def send(self, message):
        print (f"Instagram: someone sent you reels {self.reels}. {message}")

class TwitterNotification(Notification):
    def __init__(self, post):
        self.post = post
    def send(self, message):
        print (f"Twitter: someone sent you a post {self.post}.{message}")

def notify(notification: Notification, message):
    notification.send(message)

notifications = [
    TelegrammNotification("send me a video"),
    InstagramNotification("send me a reels"),
    TwitterNotification("send me a post")
]
for i in notifications:
    notify(i, "U have a new notification ;)")

#3
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Policy:
    rights_of_use = {
        "admin": ["edit", "delete", "view"],
        "user": ["view"]
    }
def has_rights_of_use(user, action):
    return action in Policy.rights_of_use.get(user.role, [])

def check_rights_of_use(action):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if not Policy.rights_of_use(user, action):
                raise PermissionError(
                    f"User '{user.username} don't have rights to use this {action}."
                )
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@check_rights_of_use
def edit_data(user):
    print(f"Data edit")
def delete_data(user):
    print(f"Data delete")
def view_data(user):
    print(f"Viewing data")

admin = User("Maria", "admin")
user = User("Alex", "user")

view_data(admin)
view_data(user)
edit_data(admin)
try:
    delete_data(admin)
except PermissionError as error:
    print (error)

#4
class BankAccount:
    def __init__(self, balance: float = 0):
        self.__balance = balance
        self.daily_limit = 5000
        self.withdrawals_today = 0
        self.max_withdrawals = 3

def deposit(self, amount: float):
    if amount <= 0:
        raise ValueError('amount must be positive')
    self.__balance += amount

def withdraw(self, amount: float):
    if amount <= 0:
        raise ValueError('amount must be positive')
    if amount > self.__balance:
        raise ValueError('insufficient funds')
    if amount > self.daily_limit:
        raise ValueError('the daily limit has been exceeded')
    if self.withdrawals_today >= self.max_withdrawals:
        raise ValueError('maximum withdrawals has been reached')
    self.__balance -= amount
    self.withdrawals_today += 1
    print(f"Withdrawn from the account: {amount}")

def get_balance(self):
    return self.__balance

account = BankAccount(3000)


account.deposit(2000)
account.withdraw(100)
account.withdraw(100)
account.withdraw(100)
print("Current balanc:", account.view_balance())

#iterator
#1
class RangeIterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

def __iter__(self):
    return self

def __next__(self):
    if self.current > 0:
        if self.current >= self.stop:
            raise StopIteration
    else:
        if self.current <= self.stop:
            raise StopIteration

    value = self.current
    self.current += self.step
    return value

start = RangeIterator(3, 9, 2)
print(list(start))
print(list(start))
print(list(start))

#2
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
for n in fibonacci(100):
    print(n)

#4
def flatten(iterable):
    for item in iterable:
        if isinstance (item, list):
            yield from flatten(item)
        else:
            yield item
data = [1, [2, 3], [[4], 5], 6]
flat_list = list(flatten(data))
print(" → ".join(map(str, flat_list)))

#file
1
file = open ("file.txt","r", encoding="utf-8")
for i in range(6):
    line = input("введите строку:")
    file.write(line + "\n")
file.close()

2
file = open ("file.txt","a", encoding="utf-8")
for i in range(3):
    line = input("введите строку")
    file.write(line + "\n")
file.close()

3
file = open ("file.txt","r", encoding="utf-8")
text = file.read()
file.close()
count = 0
for symbol in text:
    if symbol != "\n":
        count += 1
print ("Кол-во символов:", count)

4
file = open ("file.txt","r", encoding="utf-8")
lines = file.readlines()
file.close()
list = []
for line in lines:
    list.append(line.strip())
print(list)

5
file = open ("!.txt","r", encoding="utf-8")
lines = file.readlines()
file.close()
for line in lines:
    line = line.strip()
    if line.endswith("!"):
        print(line)

#6
import json
flights = [
    {"flight_number": "SU123",
    "destination": "Москва",
    "departure_time": "08:30"
  },
  {
    "flight_number": "FR456",
    "destination": "Варшава",
    "departure_time": "12:15"
  },
  {
    "flight_number": "BT789",
    "destination": "Москва",
    "departure_time": "18:40"
}
]

file = open ("flights.json","w", encoding="utf-8")
json.dump(flights, file, ensure_ascii=False, indent=4)
file.close()

file = open("flights.json", "r", encoding="utf-8")
flights = json.load(file)
file.close()

city = input("Введите пункт назначения: ")

for flight in flights:
    if flight["destination"] == city:
        print(flight["flight_number"], flight["departure_time"])