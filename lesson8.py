"""
# Problem 2
num = set()
for i in range(5):
    num.add(int(input('Number >>> ')))
print(min(num))

"""

"""
# Problem 3
try:
    eval(input("Text function >>> "))
except:
    print('Нет такой функции')

"""

"""
# Problem 4
while True:
    try:
        money = int(input("How much money do you want ( 50000+ ) >>> "))
        if money >= 50000:
            break
    except:
        print('Text only number!!!')
print(f'You have to pay {round(money * 3.47,2)}')

"""

"""
# Problem 1
try:
    age = int(input('Text your age >>> '))
    print(f'Your 7th letter is {age[8]}')
    print(name, age)
except TypeError:
    print('Text only number in your age!!!')
except IndexError:
    print('The name len must be 9')
except NameError:
    print("Doesn't have age!!!")
"""

"""
# Problem 3
lst = []
for i in range(10):
    lst.append(i)
print(lst)

"""

"""
# was

# a = (0)
# b = (1,)
# numbers = []
# while b > a:
# numbers += b
# b += 1

# my
a = (0,)
b = (1,)
numbers = []
while b > a:
    numbers.append(b)
b += 1
"""

