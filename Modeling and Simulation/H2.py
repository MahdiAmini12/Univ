import tkinter as tk
from tkinter import ttk, messagebox

# تابع میان ضربی
def middle_square(seed, count):
    numbers = []
    for _ in range(count):
        square = str(seed ** 2).zfill(8)
        mid = square[len(square)//2 - 2: len(square)//2 + 2]
        seed = int(mid)
        numbers.append(seed)
    return numbers

# تابع هم‌نهشتی خطی
def linear_congruential(seed, a, c, m, count):
    numbers = []
    for _ in range(count):
        seed = (a * seed + c) % m
        numbers.append(seed)
    return numbers

# رویداد تولید اعداد تصادفی
def generate_numbers():
    try:
        method = method_var.get()
        if method == "میان ضربی":
            seed = int(entry_seed.get())
            count = int(entry_count.get())
            numbers = middle_square(seed, count)
        elif method == "هم‌نهشتی خطی":
            seed = int(entry_seed.get())
            a = int(entry_a.get())
            c = int(entry_c.get())
            m = int(entry_m.get())
            count = int(entry_count.get())
            numbers = linear_congruential(seed, a, c, m, count)
        else:
            raise ValueError("روش تولید انتخاب نشده است.")

        # نمایش خروجی در ویجت Text
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, "\n".join(map(str, numbers)))
    except Exception as e:
        messagebox.showerror("خطا", f"مشکلی پیش آمد: {e}")

# به‌روزرسانی فرم
def update_form(*args):
    method = method_var.get()
    for widget in form_frame.winfo_children():
        widget.grid_remove()

    lbl_seed.grid(row=0, column=0, padx=5, pady=5)
    entry_seed.grid(row=0, column=1, padx=5, pady=5)
    lbl_count.grid(row=1, column=0, padx=5, pady=5)
    entry_count.grid(row=1, column=1, padx=5, pady=5)

    if method == "هم‌نهشتی خطی":
        lbl_a.grid(row=2, column=0, padx=5, pady=5)
        entry_a.grid(row=2, column=1, padx=5, pady=5)
        lbl_c.grid(row=3, column=0, padx=5, pady=5)
        entry_c.grid(row=3, column=1, padx=5, pady=5)
        lbl_m.grid(row=4, column=0, padx=5, pady=5)
        entry_m.grid(row=4, column=1, padx=5, pady=5)

# رابط گرافیکی
root = tk.Tk()
root.title("تولید اعداد تصادفی")
root.configure(bg="#1e1e1e")

# انتخاب روش
method_var = tk.StringVar()
method_var.trace_add("write", update_form)
method_menu = ttk.Combobox(root, textvariable=method_var, values=["میان ضربی", "هم‌نهشتی خطی"], state="readonly")
method_menu.grid(row=0, column=0, padx=10, pady=10)
method_menu.set("انتخاب روش تولید")

# فرم دریافت ورودی
form_frame = ttk.Frame(root)
form_frame.grid(row=1, column=0, padx=10, pady=10)

lbl_seed = ttk.Label(form_frame, text="Seed:")
entry_seed = ttk.Entry(form_frame)

lbl_count = ttk.Label(form_frame, text="Count:")
entry_count = ttk.Entry(form_frame)

lbl_a = ttk.Label(form_frame, text="A:")
entry_a = ttk.Entry(form_frame)

lbl_c = ttk.Label(form_frame, text="C:")
entry_c = ttk.Entry(form_frame)

lbl_m = ttk.Label(form_frame, text="M:")
entry_m = ttk.Entry(form_frame)

# دکمه تولید
generate_button = ttk.Button(root, text="تولید", command=generate_numbers)
generate_button.grid(row=2, column=0, padx=10, pady=10)

# نمایش خروجی با اسکرول‌بار
result_frame = ttk.LabelFrame(root, text="اعداد تولید شده")
result_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_textbox = tk.Text(result_frame, height=10, wrap="none", yscrollcommand=scrollbar.set, background="#2d2d2d", foreground="white")
result_textbox.pack(fill="both", expand=True, padx=5, pady=5)

scrollbar.config(command=result_textbox.yview)

root.mainloop()
# count تعداد 
#  seed مقدار اولیع 
#  A : ضریب ضربی
#  C: ضزیب افزایشی
#  M : مدوله 
#  فرمول : ((seed * A) + C ) % M

