#1
def area_circle(radius):
    return 3.14159 * (radius ** 2)

def area_rectangle(a, b):
    return a * b

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Круг")
    print("2. Прямокутник")
    print("3. Трикутник")

    choice = input("Ваш вибір (1-3 або назва): ").strip().lower()

    if choice == "1" or choice == "круг":
        radius = int(input("Введіть радіус круга: "))
        result = area_circle(radius)
        print("Площа:", result)
    elif choice == "2" or choice == "прямокутник":
        width = int(input("Ширина: "))
        height = int(input("Висота: "))
        result = area_rectangle(width, height)
        print("Площа:", result)
    elif choice == "3" or choice == "трикутник":
        base = int(input("Введіть основу трикутника: "))
        height = int(input("Введіть висоту трикутника: "))
        result = area_triangle(base, height)
        print("Площа:", result)
    else:
        print("Помилка")

main()
#2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def main():
    n = int(input("Введіть натуральне число: "))

    prime_result = is_prime(n)
    divisors_list = divisors(n)
    sum_result = digit_sum(n)

    print("Чи просте:", prime_result)
    print("Дільники:", divisors_list)
    print("Сума цифр:", sum_result)

main()

#3
def average(grades):
    return sum(grades) / len(grades)

def minimum(grades):
    return min(grades)

def maximum(grades):
    return max(grades)

def count_above(grades, value):
    return sum(1 for g in grades if g > value)

def main():
    grades = [10, 8, 12, 9, 11]
    boarder = 9

    print("Оцінки:", grades)
    print("Середній бал:", round(average(grades), 2))
    print("Найменша оцінка:", minimum(grades))
    print("Найбільша оцінка:", maximum(grades))
    print(f"Кількість оцінок вище за {boarder}:", count_above(grades, boarder))

main()

#4
def is_long_enough(password):
    return len(is_long_enough) >= 8

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_upper(password):
    return any(c.isupper() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_special(password):
    return any(not c.isalnum() for c in password)

def validate_password(password):
    errors = []
    if not is_long_enough(password): errors.append("Довжина менша за 8")
    if not has_digit(password): errors.append("Немає цифри")
    if not has_upper(password): errors.append("Немає великої літери")
    if not has_lower(password): errors.append("Немає малої літери")
    if not has_special(password): errors.append("Немає спецсимволу")
    return len(list) == 0, errors

def main():
    password = "Python123"
    is_valid, errors = validate_password(password)
    if is_valid:
        print("Пароль надійний")
    else:
        print("Невиконані вимоги:", errors)

main()
