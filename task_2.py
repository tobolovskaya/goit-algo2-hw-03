import csv
import os
from BTrees.OOBTree import OOBTree
from timeit import timeit

# Перевірка, чи файл існує
file_path = "generated_items_data.csv"

if not os.path.exists(file_path):
    print("Помилка: Файл не знайдено. Перевірте шлях до файлу.")
    exit()

if os.stat(file_path).st_size == 0:
    print("Помилка: Файл порожній. Додайте дані перед запуском.")
    exit()

# Завантаження даних
def load_data_from_csv(file_path):
    items = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(
                {
                    "ID": int(row["ID"]),
                    "Name": row["Name"],
                    "Category": row["Category"],
                    "Price": float(row["Price"]),
                }
            )
    return items

# Функції для додавання даних
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item  # Зберігаємо всі атрибути в значеннях

def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

# Діапазонний запит для OOBTree
def range_query_tree(tree, min_price, max_price):
    return [(key, value) for key, value in tree.items() if min_price <= value["Price"] <= max_price]

# Діапазонний запит для словника dict
def range_query_dict(dictionary, min_price, max_price):
    return [
        (key, value)
        for key, value in dictionary.items()
        if min_price <= value["Price"] <= max_price
    ]

def main():
    items = load_data_from_csv(file_path)

    tree = OOBTree()
    dictionary = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    min_price, max_price = 10.0, 50.0

    tree_time = timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
    dict_time = timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()
