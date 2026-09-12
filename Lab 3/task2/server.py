import socket

HOST = "127.0.0.1"
PORT = 5000

grading_scheme = {
    4.33: ("A+", "Excellent"),
    4.00: ("A", "Excellent"),
    3.66: ("A-", "Very good"),
    3.33: ("B+", "Very good"),
    3.00: ("B", "Very good"),
    2.66: ("B-", "Good"),
    2.33: ("C+", "Good"),
    2.00: ("C", "Good"),
    1.66: ("C-", "Passable"),
    1.33: ("D+", "Passable"),
    1.00: ("D", "Passable"),
    0.00: ("E", "Failure")
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server is running")
print(f"Listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client connected: {client_address}")
    data = client_socket.recv(1024).decode()

    try:
        grade_point = float(data)

        if grade_point in grading_scheme:
            letter_grade, qualification = grading_scheme[grade_point]
            response = f"Letter Grade: {letter_grade}\nQualification: {qualification}"
        else:
            response = "Invalid grade point. Please enter a valid grade point."

    except ValueError:
        response = "Invalid input. Please enter a numeric grade point."
    client_socket.send(response.encode())
    client_socket.close()
