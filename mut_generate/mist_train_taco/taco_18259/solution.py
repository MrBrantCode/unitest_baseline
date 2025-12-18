"""
QUESTION:
Карта звёздного неба представляет собой прямоугольное поле, состоящее из n строк по m символов в каждой строке. Каждый символ — это либо «.» (означает пустой участок неба), либо «*» (означает то, что в этом месте на небе есть звезда). 

Новое издание карты звёздного неба будет напечатано на квадратных листах, поэтому требуется найти минимально возможную сторону квадрата, в который могут поместиться все звезды. Границы искомого квадрата должны быть параллельны сторонам заданного прямоугольного поля.


-----Входные данные-----

В первой строке входных данных записаны два числа n и m (1 ≤ n, m ≤ 1000) — количество строк и столбцов на карте звездного неба.

В следующих n строках задано по m символов. Каждый символ — это либо «.» (пустой участок неба), либо «*» (звезда).

Гарантируется, что на небе есть хотя бы одна звезда.


-----Выходные данные-----

Выведите одно число — минимально возможную сторону квадрата, которым можно накрыть все звезды.


-----Примеры-----
Входные данные
4 4
....
..*.
...*
..**

Выходные данные
3

Входные данные
1 3
*.*

Выходные данные
3

Входные данные
2 1
.
*

Выходные данные
1



-----Примечание-----

Один из возможных ответов на первый тестовый пример:

 [Image] 

Один из возможных ответов на второй тестовый пример (обратите внимание, что покрывающий квадрат выходит за пределы карты звездного неба):

 [Image] 

Ответ на третий тестовый пример:

 [Image]
"""

def find_min_square_side(n, m, star_map):
    # Find the topmost row containing a star
    top = 0
    while top < n and '*' not in star_map[top]:
        top += 1
    
    # Find the bottommost row containing a star
    bottom = n - 1
    while bottom >= 0 and '*' not in star_map[bottom]:
        bottom -= 1
    
    # Find the leftmost column containing a star
    left = 0
    while left < m:
        if any(star_map[i][left] == '*' for i in range(n)):
            break
        left += 1
    
    # Find the rightmost column containing a star
    right = m - 1
    while right >= 0:
        if any(star_map[i][right] == '*' for i in range(n)):
            break
        right -= 1
    
    # Calculate the height and width of the bounding box
    height = bottom - top + 1
    width = right - left + 1
    
    # The minimum side length of the square is the maximum of height and width
    min_side = max(height, width)
    
    return min_side