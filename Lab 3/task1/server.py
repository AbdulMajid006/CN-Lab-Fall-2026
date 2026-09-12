import socket
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server is running...")
print(f"Listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"\nClient connected: {client_address}")

    try:
        data = client_socket.recv(1024).decode()
        if not data:
            client_socket.close()
            continue

        request = json.loads(data)
        num1 = request["num1"]
        num2 = request["num2"]
        operation = request["operation"]

        if operation == "+":
            answer = num1 + num2

        elif operation == "-":
            answer = num1 - num2

        elif operation == "*":
            answer = num1 * num2

        elif operation == "/":
            if num2 == 0:
                answer = "Cannot divide by zero"
            else:
                answer = num1 / num2

        else:
            answer = "Invalid operation"

        record = {
            "num1": num1,
            "operation": operation,
            "num2": num2,
            "answer": answer,
            "client_ip": client_address[0],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            with open("calculations.json", "r") as file:
                calculations = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            calculations = []

        calculations.append(record)

        with open("calculations.json", "w") as file:
            json.dump(calculations, file, indent=4)

        response = str(answer)
        client_socket.send(response.encode())

        print(f"Received: {num1} {operation} {num2}")
        print(f"Answer sent: {answer}")
        print("Details saved to calculations.json")

    except Exception as e:
        client_socket.send(f"Error: {e}".encode())
    client_socket.close()
