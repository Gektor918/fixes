import re


# 1. Если имелось ввиду создать разделение в виде прямой, тогда мы исправляем так:
text = 'snake_|-case_|-name_|-'
def to_camel_case(text):
    return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', text))
print(to_camel_case(text))


# 2. Создание SingletonMeta
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# 3. Задача на подсчет колличества едениц в бинарной строке:
print(bin(15)[2::].count('1'))


# 4. Вероятно задача на суммирование всех цифр в числе:
n = 131
def digital_root(n):
    return n if n < 10 else sum(map(int,str(n)))
print(digital_root(n))


# 5. задача на определение четного или нечетного числа:
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
print(even_or_odd(17))