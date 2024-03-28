# GuessServer
Create a Guess-the-Number server. Using UDP. The server will pick a random number
from 1 to 1000. clients will be able to send a number to the server (as a UTF-8 string)
and will get a response: "too big" / "too small" / "correct". if correct, the server will choose
another random number.
