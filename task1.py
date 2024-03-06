import threading
import os
import time


def search_in_file(file_path, keywords, result):
    """Пошук ключових слів у файлі."""
    try:
        with open(file_path, "r") as file:  # Безпечно відкриваємо файл для читання
            text = file.read()  # Читаємо весь вміст файлу
            for keyword in keywords:  # Перевіряємо кожне ключове слово
                if keyword in text:  # Якщо ключове слово знайдено у тексті
                    result[keyword].append(
                        file_path
                    )  # Додаємо файл до результатів для цього ключового слова
    except (
        Exception
    ) as e:  # Обробляємо будь-які винятки (наприклад, помилки читання файлу)
        print(f"Error reading file {file_path}: {e}")


def threaded_file_search(file_paths, keywords):
    """Функція для багатопотокового пошуку ключових слів."""
    threads = []  # Список для зберігання потоків
    result = {keyword: [] for keyword in keywords}  # Словник для зберігання результатів

    # Створюємо потік для кожного файлу
    for file_path in file_paths:
        thread = threading.Thread(
            target=search_in_file, args=(file_path, keywords, result)
        )
        threads.append(thread)  # Додаємо потік до списку потоків
        thread.start()  # Запускаємо потік

    # Чекаємо завершення всіх потоків
    for thread in threads:
        thread.join()

    return result


# Приклад використання
keywords = ["example", "test"]
file_paths = ["file1.txt", "file2.txt", "file3.txt"]

start_time = time.time()  # Записуємо час початку виконання
result = threaded_file_search(file_paths, keywords)  # Виконуємо пошук
end_time = time.time()  # Записуємо час завершення виконання

print(f"Results: {result}")
print(f"Time taken: {end_time - start_time} seconds")
