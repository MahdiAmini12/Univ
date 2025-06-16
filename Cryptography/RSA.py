import random

def Prime_Number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def condition_e(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    global e, d, n  
    while True:
        p = random.randint(2, 100)
        q = random.randint(2, 100)
        if Prime_Number(p) and Prime_Number(q) and p != q:
            break

    n = p * q
    phi_n = (p - 1) * (q - 1)

    for i in range(2, phi_n):
        if condition_e(i, n) == 1 and condition_e(i, phi_n) == 1:
            e = i
            break

    for i in range(e + 1, 100000):
        if (i * e) % phi_n == 1 and i != e:
            d = i
            break

    print(f"\n✅ Public Key: ({e}, {n})")
    print(f"🔒 Private Key: ({d}, {n})")

def encrypt_text():
    if e is None or n is None:
        print("❌ Please generate keys first.")
        return
    text = input("Enter a message to encrypt: ")
    ascii_codes = [ord(char) for char in text]
    print("ASCII codes:", ascii_codes)

    global encrypted_data
    encrypted_data = [(char ** e) % n for char in ascii_codes]
    print("🔐 Encrypted data:", encrypted_data)

def decrypt_text():
    if d is None or n is None:
        print("❌ Please generate keys first.")
        return
    if not encrypted_data:
        print("❌ No encrypted data found. Encrypt text first.")
        return
    decrypted_ascii = [(char ** d) % n for char in encrypted_data]
    decrypted_text = ''.join(chr(char) for char in decrypted_ascii)
    print("🔓 Decrypted ASCII:", decrypted_ascii)
    print("✅ Decrypted Text:", decrypted_text)

e = d = n = None
encrypted_data = []

while True:
    print("\n🔸 Menu 🔸")
    print("1. Create private key, public key")
    print("2. Text to crypto (Encrypt)")
    print("3. Crypto to text (Decrypt)")
    print("4. Exit")
    # print("5. Narges")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        generate_keys()
    elif choice == '2':
        encrypt_text()
    elif choice == '3':
        decrypt_text()
    elif choice == '4':
        print("👋 Exiting program. Goodbye!")
        break
    # elif choice == '5':
    #     print("👋eyval Narges ham toro doos dare ")
    #     while True:
    #         print('I Love Narges')
    #     # break
    else:
        print("❌ Invalid choice. Please try again.")

    input("\nPress Enter to return to menu...")
    