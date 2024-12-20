import math
import random
import time
import matplotlib.pyplot as plt


def binary_search(lys, val):
    """
    Реализация бинарного поиска.
    """
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        elif val < lys[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index


def generate_random_array(size):
    """
    Создает массив случайных чисел.
    """
    return [random.randint(1, 10000000) for _ in range(size)]


def measure_execution_time(array_type, array_sizes, repetitions=100):
    """
    Измеряет время выполнения бинарного поиска для различных массивов.
    """
    times = []
    for size in array_sizes:
        if array_type == 'sorted':
            arr = sorted(generate_random_array(size))
        else:
            raise ValueError("Unknown array type")

        total_time = 0
        for _ in range(repetitions):
            target = random.choice(arr)
            start_time = time.perf_counter()
            binary_search(arr, target)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)

        average_time = total_time / repetitions
        times.append(average_time)
        print(array_type, f"{size}  ", average_time, "секунд")
    return times

def plot_Onation_binary(sizes):
    complexities = {
        "Лучший случай O(1)":lambda n:1,
        "Средний и худший случай O(logn)": lambda n: math.log(n)
    }

    plt.figure(figsize=(12, 8))
    for label, func in complexities.items():
        cases = [func(size) for size in sizes]
        plt.plot(sizes, cases, label=label)

    plt.xlabel("Размер массива")
    plt.ylabel("Оценка времени выполнения")
    plt.title("Теоретические графики временной сложности для Бинарного поиска")
    plt.legend()
    plt.grid()
    plt.show()

# Настройки
array_sizes = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]
plot_Onation_binary(array_sizes)

sorted_times = measure_execution_time('sorted', array_sizes)


# Построение графиков времени выполнения
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, sorted_times, label="Отсортированный массив", marker='o')
plt.title("Время выполнения бинарного поиска")
plt.xlabel("Размер массива")
plt.ylabel("Среднее время (секунды)")
plt.legend()
plt.grid(True)
plt.show()

