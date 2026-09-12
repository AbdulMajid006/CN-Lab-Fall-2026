# Task#2:
# Create a client-server program where the client requests the grading scheme (enter grade
# points) and the server responds with the answer according to the given grading scheme
# (respond letter grade and qualification according to the client's entered marks).

    # 4.33  A+    Excellent
    # 4.00  A     Excellent
    # 3.66  A-    Very good
    # 3.33  B+    Very good
    # 3.00  B     Very good
    # 2.66  B-    Good
    # 2.33  C+    Good
    # 2.00  C     Good
    # 1.66  C-    Passable
    # 1.33  D+    Passable
    # 1.00  D     Passable
    # 0.00  E     Failure


import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to grading server.")

grade_point = input("Enter grade point: ")
client_socket.send(grade_point.encode())
response = client_socket.recv(1024).decode()

print("\nResult from server:")
print(response)
client_socket.close()
