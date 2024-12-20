import math
import random
import time
import matplotlib.pyplot as plt


def interpolation_search(lys, val):
    """
    Реализация интерполяционного поиска.
    """
    low = 0
    high = len(lys) - 1
    while low <= high and val >= lys[low] and val <= lys[high]:
        if low == high:
            if lys[low] == val:
                return low
            return -1
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1


def generate_random_array(size):
    """
    Создает массив случайных чисел.
    """
    return [random.randint(1, 1000000) for _ in range(size)]


def measure_execution_time(array_type, array_sizes, repetitions=100):
    """
    Измеряет время выполнения интерполяционного поиска для различных массивов.
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
            interpolation_search(arr, target)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)

        average_time = total_time / repetitions
        times.append(average_time)
        print(array_type, f"{size}  ", average_time, "секунд")
    return times


def plot_Onation_interpolation(sizes):
    complexities = {
        "Лучший случай O(1)":lambda n:1,
        "Средний случай O(loglogn)": lambda n: math.log(math.log(n)),
        "Худший случай O(n)": lambda n: n
    }
    plt.figure(figsize=(12, 8))
    for label, func in complexities.items():
        cases = [func(size) for size in sizes]
        plt.plot(sizes, cases, label=label)

    plt.xlabel("Размер массива")
    plt.ylabel("Оценка времени выполнения")
    plt.title("Теоретические графики временной сложности для Интерполяционного поиска")
    plt.legend()
    plt.grid()
    plt.show()

# Настройки
array_sizes = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000]
plot_Onation_interpolation(array_sizes)

sorted_times = measure_execution_time('sorted', array_sizes)

# Построение графиков времени выполнения
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, sorted_times, label="Отсортированный массив", marker='o')
plt.title("Время выполнения интерполяционного поиска")
plt.xlabel("Размер массива")
plt.ylabel("Среднее время (секунды)")
plt.legend()
plt.grid(True)
plt.show()


