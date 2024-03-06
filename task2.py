import multiprocessing
import os
import time


def search_in_file(file_path, keywords, queue):
    """Пошук ключових слів у файлі."""
    result = {
        keyword: [] for keyword in keywords
    }  # Локальний словник результатів для цього процесу
    try:
        with open(file_path, "r") as file:
            text = file.read()
            for keyword in keywords:
                if keyword in text:
                    result[keyword].append(file_path)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    queue.put(result)  # Відправляємо результати у чергу


def multiprocess_file_search(file_paths, keywords):
    """Функція для багатопроцесорного пошуку ключових слів."""
    processes = []
    queue = multiprocessing.Queue()  # Черга для обміну даними між процесами
    result = {keyword: [] for keyword in keywords}

    for file_path in file_paths:
        # Створюємо процес для кожного файлу
        process = multiprocessing.Process(
            target=search_in_file, args=(file_path, keywords, queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # Збираємо результати з черги
    while not queue.empty():
        partial_result = queue.get()  # Отримуємо частковий результат
        for keyword in partial_result:
            result[keyword].extend(partial_result[keyword])  # Об'єднуємо результати

    return result


# Приклад використання
keywords = ["example", "test"]
file_paths = ["file1.txt", "file2.txt", "file3.txt"]

start_time = time.time()
result = multiprocess_file_search(file_paths, keywords)
end_time = time.time()

print(f"Results: {result}")
print(f"Time taken: {end_time - start_time} seconds")
