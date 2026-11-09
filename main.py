# ===== T-1. Главное меню (общая задача) =====
TITLE = "Копилка"  # впишите название своего продукта
MENU = []  # пункты меню: (название, функция)
 
 
def ask_int(text):
    # спрашивает целое число, пока его не введут правильно
    while True:
        value = input(text).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Ошибка: введите целое число")
 
 
def ask_float(text):
    # спрашивает число (можно дробное), пока его не введут правильно
    while True:
        value = input(text).strip().replace(",", ".")
        try:
            return float(value)
        except ValueError:
            print("Ошибка: введите число")
 
 
def start():
    while True:
        print()
        print("=====", TITLE, "=====")
        for number, item in enumerate(MENU, start=1):
            print(number, "-", item[0])
        print("0 - Выход")
        choice = input("Выберите пункт: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            MENU[int(choice) - 1][1]()
        else:
            print("Нет такого пункта меню")

# ===== US-2. Добавить расход =====
expenses = []  # список расходов
 
 
def add_expense():
    amount = ask_float("Сумма расхода, руб.: ")
    if amount <= 0:
        print("Ошибка: сумма должна быть больше 0")
        return
    category = input("Категория (еда, транспорт, развлечения): ").strip()
    expenses.append({"сумма": amount, "категория": category})
    print("Расход добавлен")

 # ===== US-3. Список расходов =====
def show_expenses():
    if len(expenses) == 0:
        print("Расходов пока нет")
        return
    for number, e in enumerate(expenses, start=1):
        print(f"{number}. {e['категория']} — {e['сумма']:.2f} руб.")

MENU.append(("Список расходов", show_expenses))
# ===== US-4. Общая сумма расходов =====
def total_expenses():
    total = 0
    for e in expenses:
        total = total + e["сумма"]
    print(f"Всего потрачено: {total:.2f} руб.")
 
 
MENU.append(("Общая сумма расходов", total_expenses))

# ===== US-5. Сумма по категории =====
def category_total():
    category = input("Категория: ").strip().lower()
    total = 0
    for e in expenses:
        if e["категория"].lower() == category:
            total = total + e["сумма"]
    print(f"Потрачено в категории «{category}»: {total:.2f} руб.")
 
 
MENU.append(("Сумма по категории", category_total))
# ===== ЗАПУСК: эта строка всегда должна быть последней =====
start()
