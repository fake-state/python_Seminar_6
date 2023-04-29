# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


first_element = int(input('Введите первый эллемент > '))
step_of_progression = int(input('Введите шаг прогрессии > '))
number_of_elements = int(input('Введите количество элементов > '))

arifmetic_progression = [first_element]

for i in range(2, number_of_elements):
    arifmetic_progression.append(first_element + step_of_progression * (i-1))

print(arifmetic_progression)
