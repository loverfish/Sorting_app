import os
import random
from abc import ABC, abstractmethod

from intetics.settings import BASE_DIR


def my_decorator(a_function_to_decorate):

    def the_wrapper_around_the_original_function(*args):
        import time
        tic = time.perf_counter()
        result = a_function_to_decorate(*args)
        toc = time.perf_counter()
        t = '{:0.6f}'.format(toc - tic)
        return result, t
    return the_wrapper_around_the_original_function


class Sorting(ABC):
    @abstractmethod
    def sort(self, *args):
        pass
        # assert False, 'action must be defined in child class!'


class Bubble(Sorting):
    @my_decorator
    def sort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


class Insertion(Sorting):
    @my_decorator
    def sort(self, nums):
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


class Merge(Sorting):
    @my_decorator
    def sort(self, arg):
        return self.merge_sort(arg)

    @staticmethod
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

    def merge_sort(self, nums):
        # Возвращаем список, если он состоит из одного элемента
        if len(nums) <= 1:
            return nums

        # Для того чтобы найти середину списка, используем деление без остатка
        # Индексы должны быть integer
        mid = len(nums) // 2

        # Сортируем и объединяем подсписки
        left_list = self.merge_sort(nums[:mid])
        right_list = self.merge_sort(nums[mid:])

        # Объединяем отсортированные списки в результирующий
        return self.merge(left_list, right_list)


#                           Функция обработки скачанного фвйла

def handle_uploaded_file(f):
    with open(os.path.join(BASE_DIR, 'media/temp/new_f.txt'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


#                           Функция генерации файла со случайными числами в одну строку

def create_file(my_file, n):
    with open(my_file, "w") as outFile:
        outFile.writelines(['{} '.format(random.randint(0, 500)) for _ in range(n)])


#                           Функция чтения файла со случайными числами, возвращает список

def read_file(my_file):
    with open(my_file, 'r') as f:
        return [int(x) for x in f.readline().split()]


algorithms_class = {
    'BS': Bubble,
    'IS': Insertion,
    'MS': Merge,
}


alg_types = {
    'BS': 'bubble sort',
    'IS': 'insertions sort',
    'MS': 'merge sort',
}
