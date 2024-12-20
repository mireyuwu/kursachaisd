import random
import time
import matplotlib.pyplot as plt


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def generate_random_array(size):
    """
    Создает массив случайных чисел.
    """
    return [random.randint(1, 10000000) for _ in range(size)]


def measure_execution_time(array_type, array_sizes, repetitions=100):
    """
    Измеряет время выполнения линейного поиска для различных массивов.
    """
    times = []
    for size in array_sizes:
        if array_type == 'random':
            arr = generate_random_array(size)
        elif array_type == 'sorted':
            arr = sorted(generate_random_array(size))
        elif array_type == 'reversed':
            arr = sorted(generate_random_array(size), reverse=True)
        else:
            raise ValueError("Unknown array type")

        total_time = 0
        for _ in range(repetitions):
            target = random.choice(arr)
            start_time = time.perf_counter()
            linear_search(arr, target)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)

        average_time = total_time / repetitions
        times.append(average_time)  # Добавляем среднее время в список
        print(array_type, f"{size}  ", average_time, "секунд")
    return times  # Возвращаем список времен


def plot_Onation_linear(sizes):
    complexities = {
        "Лучший случай O(1)":lambda n:1,
        "Средний и худший случай O(n)": lambda n: n
    }

    plt.figure(figsize=(12, 8))
    for label, func in complexities.items():
        cases = [func(size) for size in sizes]
        plt.plot(sizes, cases, label=label)

    plt.xlabel("Размер массива")
    plt.ylabel("Оценка времени выполнения")
    plt.title("Теоретические графики временной сложности для Линейного поиска")
    plt.legend()
    plt.grid()
    plt.show()


# Настройки
array_sizes = [100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
plot_Onation_linear(array_sizes)
# Измерение времени выполнения
random_times = measure_execution_time('random', array_sizes)
sorted_times = measure_execution_time('sorted', array_sizes)
reversed_times = measure_execution_time('reversed', array_sizes)

# Построение графиков времени выполнения
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, random_times, label="Случайный массив", marker='o')
plt.plot(array_sizes, sorted_times, label="Отсортированный массив", marker='o')
plt.plot(array_sizes, reversed_times, label="Массив, отсортированный в обратном порядке", marker='o')
plt.title("Время выполнения линейного поиска")
plt.xlabel("Размер массива")
plt.ylabel("Среднее время (секунды)")
plt.legend()
plt.grid(True)
plt.show()
