import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import simpledialog


HOST = '127.0.0.1'
PORT = 5000

class ChatClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))

        self.root = tk.Tk()
        self.root.title("چت کلاینت")
        self.root.geometry("400x500")

        self.text_area = scrolledtext.ScrolledText(self.root, state='disabled')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="ارسال", command=self.send_message)
        self.send_button.pack(pady=5)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.prompt_username()

        self.root.mainloop()

    def prompt_username(self):
        """دریافت نام کاربری از کاربر"""
        self.username = simpledialog.askstring("نام کاربری", "نام کاربری خود را وارد کنید:")
        if not self.username:
            messagebox.showerror("خطا", "نام کاربری نمی‌تواند خالی باشد!")
            self.root.destroy()
        else:
            self.client_socket.send(self.username.encode())

    def send_message(self, event=None):
        """ارسال پیام به سرور"""
        message = self.entry.get()
        if message:
            self.client_socket.send(message.encode())
            self.entry.delete(0, tk.END)
            if message.lower() == "exit":
                self.client_socket.close()
                self.root.quit()

    def receive_messages(self):
        """دریافت پیام‌های سرور و نمایش در رابط گرافیکی"""
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, message + '\n')
                self.text_area.config(state='disabled')
                self.text_area.yview(tk.END)
            except:
                break

if __name__ == "__main__":
    ChatClient()
