import multiprocessing


# Функція для обробки даних
def process_data(data_chunk):
    # Приклад обробки даних - у цьому випадку просто повертаємо довжину кожного рядка
    processed_data = [len(line) for line in data_chunk]
    return processed_data


if __name__ == "__main__":
    # Великий обсяг даних для обробки
    big_data = [
        "Lorem ipsum dolor sit amet",
        "consectetur adipiscing elit",
        "sed do eiusmod tempor incididunt",
        "ut labore et dolore magna aliqua",
        "Ut enim ad minim veniam",
        "quis nostrud exercitation ullamco",
    ]

    # Розділення даних на частини для паралельної обробки
    num_cores = multiprocessing.cpu_count()
    chunk_size = (len(big_data) + num_cores - 1) // num_cores
    data_chunks = [
        big_data[i : i + chunk_size] for i in range(0, len(big_data), chunk_size)
    ]

    # Запуск паралельних процесів для обробки кожної частини даних
    with multiprocessing.Pool(processes=num_cores) as pool:
        processed_results = pool.map(process_data, data_chunks)

    # Об'єднання результатів обробки даних
    final_result = []
    for result in processed_results:
        final_result.extend(result)

    # Виведення оброблених даних
    print("Processed Data:", final_result)
