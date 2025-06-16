import base64

user_question = input("Text to base64(0) or base64 to Text(1): ")
if user_question == '0':
    text = input("Enter your Text: ")
    text_to_bytes = text.encode()
    bytes_to_base64 = base64.b64encode(text_to_bytes)
    base64_to_string = bytes_to_base64.decode()
    print(base64_to_string)

elif user_question == '1':
    string = input("Enter your String: ")
    string_to_bytes = string.encode()
    base64_to_bytes = base64.b64decode(string_to_bytes)
    bytes_to_text = base64_to_bytes.decode()
    print(bytes_to_text)

else:
    print("Please try again")