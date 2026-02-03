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