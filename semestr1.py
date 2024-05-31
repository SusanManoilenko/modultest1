import tkinter as tk
from tkinter import messagebox
from math import sqrt


def calculate_area():
    try:
        # Отримання значень довжин сторін з полів введення
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Перевірка на додатність сторін
        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Помилка", "Всі значення повинні бути додатніми числами")
            return

        # Перевірка на умову існування трикутника
        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Помилка", "Такий трикутник не існує")
            return

        # Обчислення площі трикутника за формулою Герона
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))

        # Виведення результату
        messagebox.showinfo("Площа трикутника", f"Площа трикутника: {area:.2f}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення")


# Створення головного вікна
root = tk.Tk()
root.title("Обчислення площі трикутника за формулою Герона")

# Отримання розмірів екрану
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Розміщення вікна по центру екрану
window_width = 300
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Встановлення фону
root.configure(bg="#FFEBCD")

# Додавання надпису з більшим шрифтом та жирністю
label_title = tk.Label(root, text="Знайти площу трикутника за трьома сторонами.\nФормула Герона.", bg="#FFEBCD",
                       fg="black", font=("Times New Roman", 20, "bold"))
label_title.pack(pady=10)

# Створення та розміщення елементів у головному вікні
label_a = tk.Label(root, text="Сторона a:", bg="#FFEBCD", font=("Times New Roman", 12))
label_a.pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Сторона b:", bg="#FFEBCD", font=("Times New Roman", 12))
label_b.pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

label_c = tk.Label(root, text="Сторона c:", bg="#FFEBCD", font=("Times New Roman", 12))
label_c.pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack(pady=5)

calculate_button = tk.Button(root, text="Обчислити площу", command=calculate_area, bg="#FFEBCD", fg="red",
                             font=("Times New Roman", 12))
calculate_button.pack(pady=10)

# Додавання формули Герона як коментаря
label_formula = tk.Label(root, text="Формула Герона: S = √(p(p - a)(p - b)(p - c)),\nде p = (a + b + c) / 2",
                         bg="#FFEBCD", font=("Times New Roman", 10))
label_formula.pack(pady=10)

# Запуск головного циклу обробки подій
root.mainloop()
