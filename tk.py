import tkinter as tk

def greet():
    name = entry.get()
    if name.strip():
        label_result.config(text=f"Привет, {name}!", fg="#2e8b57")
    else:
        label_result.config(text="Пожалуйста, введите имя.", fg="#b22222")

root = tk.Tk()
root.title("Приветствие")
root.geometry("400x250")
root.configure(bg="#f0f4f8")

FONT_MAIN = ("Segoe UI", 16, "bold")
FONT_ENTRY = ("Segoe UI", 16)
FONT_RESULT = ("Segoe UI", 18, "bold")

# Инструкция
label = tk.Label(root, text="Введите ваше имя:", font=FONT_MAIN, bg="#f0f4f8", fg="#333")
label.pack(pady=(30,10))

# Поле ввода
entry = tk.Entry(root, font=FONT_ENTRY, justify="center", fg="#333", bg="#e8eaed", bd=2, relief="groove")
entry.pack(ipady=5, ipadx=5, pady=5)

# Цвета кнопки при наведении
def on_enter(e):
    button.config(bg="#2e8b57", fg="white")
def on_leave(e):
    button.config(bg="#4caf50", fg="white")

# Кнопка
button = tk.Button(root, text="Поздороваться", font=FONT_MAIN, bg="#4caf50", fg="white", activebackground="#2e8b57", activeforeground="white", command=greet, relief="raised", bd=3, cursor="hand2")
button.pack(pady=15)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Метка для результата
label_result = tk.Label(root, text="", font=FONT_RESULT, bg="#f0f4f8")
label_result.pack(pady=10)

entry.focus()
root.mainloop()