import socket


def guess_number(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Set a timeout for the socket operations
        client_socket.settimeout(5)

        while True:
            # Prompt the user for a guess
            guess = input("Enter your guess (1-1000) or 'exit' to quit: ")
            if guess.lower() == 'exit':
                print("Exiting the game.")
                break

            # Send the guess to the server
            client_socket.sendto(guess.encode('utf-8'), (server_host, server_port))

            try:
                # Wait for the server's response
                response, _ = client_socket.recvfrom(1024)
                print(f"Server says: {response.decode('utf-8')}")

                # If the guess is correct, let the user know they can guess again
                if response.decode('utf-8').lower() == "correct":
                    print("Congratulations! You guessed correctly.\nTry guessing the new number.")
            except socket.timeout:
                print("No response from server, please try again.")


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    guess_number(HOST, PORT)
