import random


def my_shiny_new_decorator(a_function_to_decorate):

    def the_wrapper_around_the_original_function(*args):
        import time
        tic = time.perf_counter()
        res = a_function_to_decorate(*args)
        toc = time.perf_counter()
        t = '{:0.6f}'.format(toc - tic)
        return res, t
    return the_wrapper_around_the_original_function


#                           Функция сортировки методом пузырька, обернутая в декоратор

@my_shiny_new_decorator
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


#                           Функция сортировки методом вставки, обернутая в декоратор

@my_shiny_new_decorator
def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
    return nums


#                           Функция сортировки методом слияния, обернутая в декоратор

@my_shiny_new_decorator
def new_sort(arg):
    res = merge_sort(arg)
    return res


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


#                           Функция генерирования файла со случайными числами в одну строку

def create_file(my_file, n):
    with open(my_file, "w") as outFile:
        outFile.writelines(['{} '.format(random.randint(0, 500)) for _ in range(n)])


#                           Функция чтения файла со случайными числами, возвращает список

def read_file(my_file):
    with open(my_file, 'r') as f:
        return [int(x) for x in f.readline().split()]


algorithms = {
    'BS': bubble_sort,
    'IS': insertion_sort,
    'MS': new_sort,
}


alg_types = {
    'BS': 'bubble sort',
    'IS': 'insertions sort',
    'MS': 'merge sort',
}
