"""
Настройка окружения
"""

# Установить нужную версию Python;
# Создать виртуальное окружение;
# Работа с зависимостями (pip list, pip freeze, pip install/uninstall);

"""
Базовый синтаксис
"""
import typing


# основные типы и структуры
types = [
    ...,
    None,
    True, False, bool,
    1, int,
    1.1, float,
    ' ', " ", """ """, f'', r'', str,
    b'', bytes,
    [], list,
    (), tuple,
    {1, }, set,
    {}, dict
]



"""
Типы данных
"""
str  #строки:'Hello world', "Hello world", """Привет, мир!"""
int  #целые числа: 5, -100, 0, 9
float  #числа с плавающей точкой: 3.14, -0.002, 11.2
complex  #комплексные числа, состоят из действительной и мнимых частей
bool  #булево: True или False
list  #списки, упорядоченные элементы: [1, 2, 3], ['яблоко', 'банан']
set  #множества, уникальные элементы: {1, 2, 3}, {'apple', 'banana'}
tuple  #кортежи, неизменяемые элементы: (1, 2, 3), ('apple', 'banana')
dict  #словари с парами ключ-значение: {'имя': 'Джон', 'возраст': 25}
None  #ничто, отсутствие значения
bytes  #неизмяняемая последовательность байтов для работы с двоичными данными
bytearray  #измяняемая последовательность байтов, массивы


slice  #срезы в строках от start до stop с шагом step: [0:100:3]
range  #диапазоны в циклах и других конструкциях: (0, 100,2)
enumerate  #перечисления именованных констант: for i, v in enumerate(list)


str #все, что представлено в текстовой форме

s1 = 'spam'; s2 = 'eggs' 
print(s1 + s2)  #‘spameggs’, конкатенация (сложение)

print('spam' * 3) #‘spamspamspam’, дублирование строки

len('spam')  #4, длина строки (функция len)

S = 'spam' 
S[0] #'s', доступ по индексу
S[2] #'a', доступ по индексу
S[-2] # 'a', доступ по индексу

s = 'spameggs'
s[3:5] #'me', извлечение среза
s[2:-2] #'ameg', извлечение среза
s[:6] #'spameg', извлечение среза
s[1:] #'pameggs', извлечение среза
s[:] #'spameggs', извлечение среза


#функции и методы строк
s = 'str';  s = "str";  s = '''str''';  s = """str""" #литералы строк
s = "s\np\ta\nbbb" #экранированные строки
s = f"{s} {s}" #форматированные строки
S = r"C:\temp\new" #сырые строки, подавляют экранирование
s = b"byte" #строка байтов
s.find("o", 5, 10) #поиск подстроки в строке, номер первого вхождения или -1
s.rfind("o", 0, 8) #номер последнего вхождения или -1
s.index("world", 0, 11) #номер первого вхождения или ValueError
s.rindex("o", 0, 8) #номер последнего вхождения или ValueError
s.replace("o", "O", 1) #замена шаблона на замену, количество замен
s.split(" ") #разбиение строки по разделителю и создание списка (list)
s.join(list) #сборка строки из списка с разделителем S
s.isdigit() #состоит ли строка из цифр
s.isalpha() #состоит ли строка из букв
s.isalnum() #состоит ли строка из цифр или букв
s.islower() #состоит ли строка из символов в нижнем регистре
s.isupper() #состоит ли строка из символов в верхнем регистре 
s.isspace() #состоит ли строка из неотображаемых символов ((’  ‘), ('\f'), ('\n'), ('\r'), ('\t'), ('\v')) 
s.istitle() #начинаются ли слова в строке с заглавной буквы
s.startswith(str) #начинается ли строка S с шаблона str 
s.endswith(str) #заканчивается ли строка S шаблоном str 
s.upper() #преобразование строки к верхнему регистру
s.lower() #преобразование строки к нижнему регистру 
s.swapcase() #перевод символов нижнего регистра в верхний и наоборот
s.capitalize() #переводит первый символ в верхний регистр, а остальные в нижний
s.center(20, "-") #возврат отцентрованной строки, по краям символ fill (обычно пробел) 
s.count("o", 0, 8) #количество непересекающихся вхождений подстроки в диапазоне
s.expandtabs([tabsize]) #копия строки, в которой все символы табуляции заменяются пробелами
s.strip([chars]) #удаление пробелов в начале и в конце строки
s.lstrip([chars]) #удаление пробелов в начале строки
s.rstrip([chars]) #удаление пробелов в конце строки 
s.partition(sep) #кортеж, часть перед 1-ым шаблоном, сам шаблон, часть после шаблона  
s.rpartition(sep) #кортеж, часть перед последним шаблоном, сам шаблон, часть после шаблона
s.title() #перевод первой буквы каждого слова в верхний регистр, а остальные в нижний 
s.zfill(width) #делает длину строки не меньшей width, возможно заполняя символы нулями
s.ljust(width, fillchar=" ") #делает длину строки не меньшей width заполняя последние символы с fillchar
s.rjust(width, fillchar=" ") #делает длину строки не меньшей width заполняя первые символы с fillchar 
s.format(*args, **kwargs) #форматирование строки  
ord(символ) #символ в его код ASCII
chr(число) #код ASCII в символ


int #поддерживают набор обычных математических операций

# основные операторы
1 + 2 #сложение
1 - 2 #вычитание
1 * 2 #умножение
1 / 2 #деление
1 ** 2 #возведение в степень
1 // 2 #получние целоц части от деления
1 % 2 #взятие остатка
-1 #смена знака числа
abs(-1) #модуль числа


#логические операторы:
1 and 2 #истина, если оба значения X и Y истинны
1 or 2 #истина, если хотя бы одно из значений X или Y истинно
not 1 #истина, если X ложно
1 > 2  #больше
1 >= 2 # больше равно
1 < 2 # меньше
1 <= 2 # меньше равно


#системы счисления
int([object], [x]) # преобразование в десятичные числа
bin(x) #преобразование целого числа в двоичную строку
hex(х) #преобразование целого числа в шестнадцатеричную строку
oct(х) #преобразование целого числа в восьмеричную строку


list #изменяемые коллекции объектов произвольных типов

print(list('список'))  #['с', 'п', 'и', 'с', 'о', 'к']

#методы списков
list.append(x) #добавление элемента в конец списка 
list.extend(L) #расширение списка, добавление в конец все элементы списка L
list.insert(i, x) #вставка x на i-ную позицию 
list.remove(x) #удаление первого x в списке.  Если элемента нет, то ValueError
list.pop([i]) #удаление и возврат i-ного элемента. Если нет индекса, то последний элемент
list.index(x, [start [, end]]) #возврат положения первого x элемента (поиск от start до end)
list.count(x) #возврат количества элементов со значением x
list.sort([key=функция]) #сортировка списка на основе функции 
list.reverse() #разворот списка
list.copy() #поверхностная копия списка
list.clear() #очищение списка


set #множества, не повторяющиеся элементы в случайном порядке
a = set('hello')  #{'h', 'o', 'l', 'e'}
a = {'a', 'b', 'c', 'd'} #{'b', 'c', 'a', 'd'}
a = {i ** 2 for i in range(10)} # генератор множеств
print(a) # {0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
a = {}  # А так нельзя!  print(type(a)) <class 'dict'>


#методы множества
len(s) #количество элементов во множестве
x in s #есть ли x во множестве s
set.isdisjoint(other) #истина, если set и other не имеют общие элементы
set == other #все элементы set принадлежат other и наоборот
set.issubset(other) or set <= other #все элементы set принадлежат other
set.issuperset(other) or set >= other #все элементы other принадлежат set
set.union(other, ...) or set | other | ... #объединение нескольких множеств
set.intersection(other, ...) or set & other & ... #пересечение элементов множеств
set.difference(other, ...) or set - other #множество из всех элементов set, не принадлежащие ни одному
set.symmetric_difference(other); set ^ other #множество из элементов, встречающихся в только одном множестве
set.copy() #копия множества

#операции изменяющие множество:
set.add(elem) #добавление элемента в множество
set.remove(elem) #удаление элемента из множества. KeyError, если нет элемента
set.discard(elem) #удаление элемента, если он находится в множестве
set.pop() #удаление первого элемента из множества. Незнаешь какой элемент удалиться 
set.clear() #очистка множества
set.update(other, ...); set |= other | ... #объединение
set.intersection_update(other, ...); set &= other & ... #пересечение
set.difference_update(other, ...); set -= other | ... #вычитание
set.symmetric_difference_update(other); set ^= other #сохранение только тех элементов, присутствующие в исходном наборе или в передаваемом наборе, но не в обоих

set #изменяемый тип данных
frozenset #неизменяемый тип данных. Похожи на с списки и кортежи
a = set('qwerty'); b = frozenset('qwerty')
a == b  # True


tuple #кортеж - неизменяемый список. Зачем нужны кортежи, если есть списки? 1) Защита от дурака - защищен от изменений, как намеренных, так и случайных. 2) Меньший размер

a = (1, 2, 3, 4, 5, 6)
b = [1, 2, 3, 4, 5, 6]
a.__sizeof__() # 36
b.__sizeof__() # 44

#методы кортежей
a.count(x) #возврат количества вхождений элемента x в кортеже
a.index(x) #возврат индекса первого вхождения элемента x в кортеже. Если нет то ValueError


dict #неупорядоченные коллекции произвольных объектов с доступом по ключу 

#создание словаря с помощью литерала:
d = {} 
d = {'dict': 1, 'dictionary': 2}

#создание словаря с помощью функции dict:
d = dict(short='dict', long='dictionary')
d = dict([(1, 1), (2, 4)])

#Создание словаря с помощью метода fromkeys:
d = dict.fromkeys(['a', 'b'])
d = dict.fromkeys(['a', 'b'], 100)

#создание словаря с помощью генераторов словарей, очень похожие на генераторы списков
my_dict = {x: x**2 for x in range(3, 10)}
print(my_dict)

#методы словарей
dict.clear() #очищает словарь
dict.copy() #копия словаря
dict.get(key[, default]) #возврат значения ключа. Если его нет, то default
dict.keys() #ключи в словаре
dict.values() #значения в словаре
dict.items() #пара (ключ, значение)
dict.pop(key[, default]) #удаление ключа и возврат значения. Если её нет, то default
dict.popitem() #удаление и возврат пары. Если словарь пуст, то KeyError
dict.update([other]) #обновление словаря, добавление пары из other
dict.setdefault(key[, default]) #значение ключа, если его нет, создает ключ со знач. default
dict.fromkeys(seq[, value]) #создание словаря из seq и value (по умолчанию None)


# цикл for
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


# Вложенный цикл
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# использование break в for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        print("Найдено число 5!")
        break
    print(f"Текущее число: {num}")

# использование continue в for
for num in range(1, 10):
    if num % 2 == 0:
        continue
    print(f"Нечётное число: {num}")


# цикл while
counter = 0
while counter < 5:
    print(counter)
    counter += 1


#сложный цикл while
import random
number_to_guess = random.randint(1, 10)
guess = None

while guess != number_to_guess:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess < number_to_guess:
        print("Больше!")
    elif guess > number_to_guess:
        print("Меньше!")
print("Правильно!")


# цикл while
import random
number = random.randint(1, 10)

while True:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess == number:
        print("Угадали!")
        break
    print("Попробуйте ещё раз.")



# while с continue
numbers = [-3, -2, -1, 0, 1, 2, 3]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(f"Положительное число или ноль: {numbers[i]}")
    i += 1


# цикл do while
while True:
    user_input = input("Введите 'выход', чтобы завершить: ")
    if user_input.lower() == "выход":
        print("Программа завершена.")
        break
    print("Вы ввели:", user_input)


# comprehensions
a = [x**2 for x in range(10)]  #list comprehension
b = [x for x in range(10) if x % 2 == 0] #list comprehension
c = (x**2 for x in range(10)) #generator expression
d = {x: x**2 for x in range(10) if x % 2 != 0} #dictionary comprehension
e = {x for x in range(10) if x % 2 == 0} #set comprehension


# присвоение, распаковка, срезы
e, *f, g = [1,2,3,4,5,6,7,8,9,10]
h = [*f]
k = [1, 2, 3][:]
l = {**{}}


# assert используется для временной проверки предположений в коде и может быть отключён
def divide(a, b):
    assert b != 0, "Деление на ноль невозможно"
    return a / b

result = divide(10, 2)  # Ок

# raise используется для явного выброса исключений и ошибок и никогда не отключается.
x = -5
if x < 0:
    raise ValueError("x не может быть отрицательным!")


# обработка исключений
try:
    1 / 0
except ZeroDivisionError as exc:
    pass
else:
    pass
finally:
    ...


#Функция - блок кода выполняющий операцию и возвращающий значение 
#Функция - объект, её можно возвращать из другой функции или передавать как аргумент

def func(a, b, c=2): # c - необязательный аргумент
    return a + b + c

func(1, 2)  # a = 1, b = 2, c = 2 (по умолчанию)   5

def say_hello(name, emoji):
    print(f'hi {name} {emoji}')

say_hello('Andrei', ':D')  # позиционные аргументы
say_hello(emoji=':D', name ='Andrei')  # именованные аргументы


#при позиционных аргументах, перед именем ставится:
def func(*args):
    return args

func(1, 2, 3, 'abc')
(1, 2, 3, 'abc')
func()
()
func(1)
(1,)

#*args кортеж (tuple) из всех переданных аргументов в функцию
#**kwargs произвольное число именованных аргументов возврашаемые в виде словаря (dict)

def func(**kwargs):
    return kwargs

func(a=1, b=2, c=3)
{'a': 1, 'c': 3, 'b': 2}
func()
{}
func(a='python')
{'a': 'python'}


def func(text: str, space: str, action: typing.Callable) -> None:
    if not text:
        return

    print(space + action(text))
    func(text[1:], space + ' ', action)
    print(space + action(text))


# lambda функции
func('*' * 11, '', lambda text: ' '.join(i for i in text))

#рекурсия - функция вызывающее саму себя и решающие задачи, которые могут быть разложены на более мелкие подзадачи

def reverse(text): 
    if len(text) == 0: 
        return ""
    return text[-1] + reverse(text[:-1])

print(reverse("Hello, world!"))


#замыкание - вложенная функция имеющая доступ к переменным внешней функции даже после её завершения выполнения

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure_example = outer_function(10)

result1 = closure_example(5)  # результат: 15 (10 + 5)
result2 = closure_example(8)  # результат: 18 (10 + 8)


#декораторы - обёртки дающие возможность изменить поведение функции, не изменяя её код
import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.name} выполнялась {end_time - start_time:.2f} секунд")
    return wrapper

@my_decorator
def some_long_running_function():
    time.sleep(2)
    print("Функция завершила работу")

some_long_running_function()


def decorator(multiplier: int):
    def dec(func: typing.Callable):
        # Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1

        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                # Генераторы
                yield func(*args, **kwargs)
        return wrap
    return dec


@decorator(10)
def f(num: int) -> int:
    return num


qwe = [*f(1)]


#колбэк-функция  — функция передаётся в другую функцию в качестве аргумента и вызывается позже, когда наступает определённое событие или выполнение кода достигает нужного момента. Примеры использования:
#1. Асинхронное программирование: В библиотеках, как asyncio, колбэк-функции вызываются, когда завершается асинхронная операция.
#2. Обработка событий: В GUI-приложениях (например, с использованием Tkinter), колбэки вызываются при нажатии кнопок.
#3. Функции высшего порядка: Встроенные функции, такие как map(), filter(), принимают колбэк-функции для обработки каждого элемента списка.


#функции и методы - одно и то же, за исключением того, что методы всегда ожидают первым параметром ссылку на сам объект (self). Это значит, что можно создавать декораторы для методов точно так же, как и для функций, не забывая про self.


# if elif else универсальная конструкция для проверки любых условий.
grade = 85

if grade >= 90:
    print("Отлично!")
elif grade >= 75:
    print("Хорошо.")
elif grade >= 50:
    print("Удовлетворительно.")
else:
    print("Плохо.")


#matc case используется для шаблонного сопоставления значений или кортежей, списков, словарей итд.
number = 15

match number:
    case n if n < 10:
        print("Число меньше 10")
    case n if 10 <= n <= 20:
        print("Число от 10 до 20")
    case _:
        print("Число больше 20")



"""
ООП. Классы и наследование, super, магические методы и т.п.
"""
import typing


class A:
    class_attrs = None

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        self.__test_arg = None

    def __len__(self) -> int:
        return len(self.args) + len(self.kwargs)

    def __bool__(self) -> bool:
        return bool(self.__test_arg)

    def main(self) -> None:
        print('Вызов внутри: A')

    @property
    def test_arg(self) -> typing.Any:
        return self.__test_arg

    @test_arg.setter
    def test_arg(self, value: typing.Any):
        self.__test_arg = value


class B(A):

    def main(self) -> None:
        print('Вызов внутри: B до super')
        super().main()
        print('Вызов внутри: B после super')

    @classmethod
    def create(cls, *args, **kwargs) -> 'B':
        return cls(*args, **kwargs)

    @staticmethod
    def get_test() -> str:
        return 'test'


class C(B):

    def main(self) -> None:
        print('Вызов внутри: C до super')
        super().main()
        print('Вызов внутри: C после super')


class D(A):

    def main(self) -> None:
        print('Вызов внутри: D до super')
        super().main()
        print('Вызов внутри: D после super')


class QWE(C, D):

    def main(self) -> None:
        print('Вызов внутри: QWE до super')
        super().main()
        print('Вызов внутри: QWE после super')


if __name__ == '__main__':
    qwe = QWE()
    qwe.main()
    print(QWE.mro())
    print(dir(QWE))



#модуль - файл который можно импортировать в другие программы или модули
math #предоставляет более сложные математические функции для работы с числами:

import math

math.pi #3.141592653589793
math.sqrt(85) #9.219544457292887


#пакет — папка, содержащая один или несколько модулей (.py файлов) и файл __init__.py. Этот файл обозначает папку как пакет, что позволяет её импортировать и использовать.


if __name__ == "__main__": #в Python используется для того, чтобы определить, выполняется ли файл как основной скрипт или импортируется как модуль


"""
Работа с разными форматами:
- работа со временем и датами
- работа с Decimal
- работа с регулярными выражениями
- работа с файлами (например csv)
- Работа с вводом/выводом
- Работа с uuid
- Работа с os
- Работа с кодировками
"""
import csv
import datetime
import decimal
import json
import os
import re
import time
import uuid


# Даты
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

current_time = datetime.datetime.now()
current_timestamp = current_time.timestamp()
in_str = current_time.strftime('%d:%m:%y %H:%M:%S')
in_datetime = datetime.datetime.strptime(in_str, '%d:%m:%y %H:%M:%S')

timestamp = time.time()
from_timestamp = datetime.datetime.fromtimestamp(timestamp)


# работа с Decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_DOWN

a = decimal.Decimal('0.3')
b = decimal.Decimal(0.3)
c = b.quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_UP)


# работа с регулярными выражениями
pattern = re.compile(r'^@(\w+)$')
nicknames = ['@qweqwe', '@@qweqwe', 'qweqwe', 'qwe@qwe']
valid_nicknames = [i for i in nicknames if re.match(pattern, i)]


# Работа с файлами
# some_dict = {'qwe': 123}
# file_name = 'new.json'
file_name = 'new.csv'
with open(file_name, 'w') as file:
    # json.dump(some_dict, fp=file, indent=4, ensure_ascii=False)
    fieldnames = ['nicknames', 'length']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for nickname in valid_nicknames:
        writer.writerow({'nicknames': nickname, 'length': len(nickname)})

with open(file_name, 'r') as file:
    # json_obj = json.load(file)
    reader = csv.DictReader(file)
    for row in reader:
        print(row['nicknames'], row['length'])


# Ввод/вывод
test = input('test:').split()
for i in range(10):
    print(*test, sep='(╯ ° □ °) ╯ ┻━┻', end='\n' + '\t' * i,)


# Работа с uuid
uid = uuid.uuid4()


# Работа с os
path = os.path.join(__file__, 'qweqwe')
os.getenv('ENV_NAME')

os.system('echo 123')


# Кодировки
a = 'qweqwe'.encode('utf-16')
b = a.decode('utf-16')





"""
Написание тестов
"""
# Юнит тесты

import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    """Тестирование функции add."""

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

    def test_add_negative_and_positive(self):
        result = add(-2, 5)
        self.assertEqual(result, 3)

    def test_add_zero_and_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_add_large_numbers(self):
        result = add(999999999, 1)
        self.assertEqual(result, 1000000000)

    def test_add_floats(self):
        result = add(1.2, 3.4)
        self.assertAlmostEqual(result, 4.6)

    def test_add_string(self):
        with self.assertRaises(TypeError):
            add('one', 2)

    def test_add_none(self):
        with self.assertRaises(TypeError):
            add(None, 2)

    def test_add_boolean(self):
        result1 = add(True, 2)
        result2 = add(False, 4)
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 4)


if __name__ == '__main__':
    unittest.main()


"""
Логирование
"""
import logging
import requests

import secrets


class TelegramHandler(logging.Handler):
    """Handler для отправки логов в телеграм."""

    def __init__(self, token, chat_id):
        super().__init__()

        self.token = token
        self.chat_id = chat_id

    def send_message_to_telegram(self, message: str) -> None:
        """Отправляет сообщение в телеграм."""
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {
            'chat_id': self.chat_id,
            'text': message
        }
        requests.post(url=url, json=data)

    def emit(self, record: logging.LogRecord) -> None:
        """
        Зарегистрировать запись лога.

        Данный метод защищён от возможных ошибок, чтобы ошибка при логировании не повлияла на работу кода.
        """
        try:
            message = self.format(record)
            self.send_message_to_telegram(message)
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)


def create_tg_logger(name: str) -> logging.Logger:
    """Создать telegram Logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    handler = TelegramHandler(secrets.TOKEN, secrets.CHAT_ID)
    handler.formatter = logging.Formatter('%(levelname)s: LOGGER: %(name)s TIME: %(asctime)s: MESSAGE: %(message)s')
    logger.addHandler(handler)

    return logger


def main() -> None:
    """Тестовое логирование."""
    logger = create_tg_logger('test-logger')

    print('До')
    logger.critical('qweqwe, ой беда все сюда')
    print('После')


if __name__ == '__main__':
    main()


"""
Соблюдение общих норм для написания красивого кода, который легко читать и поддерживать.
"""

# 1) Соблюдение PEP8.
# 2) Длина строки — 119 символов.
# 3) Импорты отсортированы правильно, неиспользуемых импортов нет.
# 4) Отступы — 4 пробела.
# 5) Одинаковые кавычки, одинаковые методы решения одинаковых проблем.
# 6) Отсутствие закомментированного кода и стандартных комментариев.
# 7) Комментарии к функциям оформлены в виде Docstrings.
# 8) Длинные куски кода логически разделены пустыми строками, как абзацы в тексте.
# 9) Исполняемый код в .py-файлах закрыт конструкцией if __name__ == ‘__main__’
# 10) В f-строках применяется только подстановка переменных. Не применяются логические или арифметические операции.
# 11) Переменные названы в соответствии с их смыслом, по-английски, нет однобуквенных названий и транслита.


# Проектирование
# YAGNI You Aren’t Gonna Need It / Вам это не понадобится
# Неиспользуемый код удаляется, а не комментируется или висит мёртвым грузом

# DRY Don’t Repeat / Не повторяйтесь
# Не должно быть одинаковых классов / функций / больших кусков кода, делающих одно и то же

# KISS Keep It Simple, Stupid / Будь проще
# Нужно стремиться писать максимально простой и понятный код.
# Каждая функция и класс ориентированы на выполнение одной конкретной задачи

# Есть еще SOLID и DI
# но это необязательно для нашего уровня (уровень поиска первой работы)


"""
Навык отладки
"""


import os


TOKEN = os.getenv('TOKEN')  # Токен телеграм-бота
CHAT_ID = os.getenv('CHAT_ID')  # Айди чата, где находится телеграм-бот



"""
Работа с асинхронным python
"""
import asyncio
import time

import aiohttp
import requests


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


URLS = [
    'https://google.com',
    'https://www.youtube.com/',
    'https://www.djangoproject.com/',
    'https://www.python.org/',
    'https://www.wikipedia.org/'
]


def time_tracker(func):
    """Декоратор для измерения скорости работы декорируемой функции."""

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time() - start

        print(f'Функция {func.__name__} отработала за {end} секунд.')

    return wrapper


async def make_async_request(idx, url, session: aiohttp.ClientSession) -> None:
    """Асинхронный запрос на url."""
    async with session.get(url) as response:
        if 200 <= response.status < 300:
            text = 'успешно'
        else:
            text = 'безуспешно'

        print(f'{idx} | {url}: {text}', end='\n')


def make_sync_request(idx, url) -> None:
    """Синхронный запрос на url."""
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        text = 'успешно'
    else:
        text = 'безуспешно'

    print(f'{idx} | {url}: {text}', end='\n')


async def async_run(count: int) -> None:
    """Отправить N асинхронных запросов."""
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(count):
            tasks.append(make_async_request(idx=i, url=URLS[i % len(URLS)], session=session))

        await asyncio.gather(*tasks)


def sync_run(count: int) -> None:
    """Отправить N синхронных запросов."""
    for i in range(count):
        make_sync_request(idx=i, url=URLS[i % len(URLS)])


@time_tracker
def async_main() -> None:
    asyncio.run(async_run(1000))


@time_tracker
def sync_main() -> None:
    sync_run(30)


if __name__ == '__main__':
    async_main()
    sync_main()


"""
Понимание асимптотической сложности в базовых операциях
https://wiki.python.org/moin/TimeComplexity
https://leetcode.com/
"""

# Хотя бы самая минимальная база по Big O notation.

# Чем отличается поиск в списке
if 100500 in [1, 2, 3]:
    ...

# от поиска в множестве
if 100500 in {1, 2, 3}:
    ...


new_test_list = []

# В чем разница между:
for item in (1, 2, 3):
    new_test_list.append(item)
    # vs
    new_test_list.insert(0, item)


# Какая сложность у
new_test_list.pop(-1)
# и у
number = new_test_list[4]


new_list = [1, 2, 3, ]
# Что лучше. Вот так:
for i in range(3):
    new_list.append(i)

# или
new_list.extend([i for i in range(3)])


"""
Паттерны проектирования. Хотя бы синглтон
"""
import random
from collections import defaultdict
from functools import lru_cache


ALL_DRINKS = defaultdict(int)


class Drink:
    """Интерфейс напитка."""

    def main(self):
        raise NotImplemented


class Water(Drink):
    """Вода."""

    def main(self) -> str:
        return 'вода'


class Juice(Drink):
    """Сок."""

    def main(self) -> str:
        return 'Сок'


# декоратор
def drink_counter(func):
    """Считает кол-во выданных напитков."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        ALL_DRINKS[result.__class__.__name__] += 1
        return result

    return wrapper


# фабрика
@drink_counter
def get_drink(price: int) -> Drink:
    """Выдаёт какой-то напиток в зависимости от цены."""
    if price <= 10:
        return Water()

    return Juice()


for _ in range(10):
    drink = get_drink(random.randint(1, 20))

print(ALL_DRINKS)


# Синглтон
unique_juice = Juice()


# либо так
@lru_cache
def get_unique_juice():
    return Juice()

# https://github.com/LpilinAlexandr/python-for-first-job/tree/main
