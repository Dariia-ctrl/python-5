#def hello_world():
#    print("Hello world")
#

#hello_world()

#def hello_world(name):
#    print(f'Hello world {name}!!!')
#hello_world( 'Dasha ')

#def rectangle_area(width, heighr):
#    return width * heighr


#width = int(input("Введіть ширину прямокутника: "))
#heighr = int(input("Введіть довжину прямокутника: "))

#S = rectangle_area(width, heighr)

#print(f'Площа дорівнюєє {S} cm2')

#def hello_world(name, message = 'Hello World!'):
#    print(f'Hello {name}, your message is {message}')

#hello_world('Ivan', 'Python')

#def price_with_discount(price, discount):
#    return price - price * discount / 100


#print(price_with_discount(1000))

#def min_max(numbers):
 #   return min(numbers), max(numbers)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#min_, max_ = min_max(numbers)

#def is_even(num):
#    ***Повертає True якщо парне, - інакше False***
 #   return num % 2 == 0

#print(is_even(3))
#print(is_even.__doc__)

def rectangle_area(width, height):
    return width * height

def main():
    width = 7
    height = 6

    print(f'Ширина, {width}')
    print(f'Висота, {height}')
    result = rectangle_area(width, height)
    print(f'Площа прямокутного трикутника: {result}')

main()