import socket
import threading

HOST = '0.0.0.0'  # اجازه اتصال از هر IP
PORT = 5000        # پورت سرور

clients = {}  # دیکشنری برای نگهداری کلاینت‌ها

def broadcast(message, sender_socket):
    """ ارسال پیام به همه کلاینت‌ها """
    for client in clients.values():
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                pass

def handle_client(client_socket):
    """ مدیریت هر کلاینت به صورت جداگانه """
    username = "کاربر ناشناس"  # مقدار پیش‌فرض نام کاربری
    try:
        username = client_socket.recv(1024).decode()  # دریافت نام کاربری از کلاینت
        clients[username] = client_socket
        print(f"{username} متصل شد.")
        broadcast(f"{username} به چت پیوست!", client_socket)

        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                break
            broadcast(f"{username}: {message}", client_socket)
    
    except:
        pass
    finally:
        print(f"{username} قطع شد.")
        del clients[username]
        broadcast(f"{username} از چت خارج شد.", client_socket)
        client_socket.close()

def start_server():
    """ راه‌اندازی سرور """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"سرور روی {HOST}:{PORT} اجرا شد.")

    while True:
        client_socket, addr = server.accept()
        print(f"اتصال جدید از {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
