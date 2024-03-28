import socket
import struct


def guess_number(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Set a timeout for the socket operations
        client_socket.settimeout(5)

        while True:
            try:
                # Prompt the user for a guess
                guess = input("Enter your guess (1-1000) or 'exit' to quit: ")
                if guess.lower() == 'exit':
                    print("Exiting the game.")
                    break

                if guess.isdigit() and 1 <= int(guess) <= 1000:
                    binary_guess = struct.pack('<H', int(guess))  # '<H' for little-endian unsigned short
                    client_socket.sendto(binary_guess, (server_host, server_port))  # Send the guess to the server

                    # Wait for the server's response
                    response, _ = client_socket.recvfrom(1024)
                    print(f"Server says: {response.decode('utf-8')}")

                    # If the guess is correct, let the user know they can guess again
                    if response.decode('utf-8').lower() == "correct":
                        print("Congratulations! You guessed correctly.\nTry guessing the new number.")
                else:
                    print("Please enter a number between 1 and 1000.")

            except socket.timeout:
                print("No response from server, trying again.")
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    guess_number(HOST, PORT)
