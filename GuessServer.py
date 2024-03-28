import random
import socket



def start_server(host, port):
    # Pick the initial random number
    number_to_guess = random.randint(1, 1000)
    print(f"Starting server. Number to guess is: {number_to_guess}")

    # Create the UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to address
        server_socket.bind((host, port))
        print(f"Server running on {host}:{port}")

        while True:
            # Receive data from client
            data, addr = server_socket.recvfrom(1024)
            guess_str = data.decode('utf-8')

            # Check if the received data is a valid number
            if guess_str.isdigit():
                guess = int(guess_str)
                if guess < number_to_guess:
                    response = "too small"
                elif guess > number_to_guess:
                    response = "too big"
                else:
                    response = "correct"
                    print(f"Client {addr} guessed correctly\n. Generating a new number.")
                    number_to_guess = random.randint(1, 1000)
                    print(f"New number to guess is: {number_to_guess}")
            else:
                response = "Please send a valid number."

            # Send the response back to the client
            server_socket.sendto(response.encode('utf-8'), addr)


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    start_server(HOST, PORT)
