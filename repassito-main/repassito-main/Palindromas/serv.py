import sys
import socket


class Servidor:
    def initialize_connection(self):
        self.s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        self.s_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        direction = ('0.0.0.0', 16021)
        self.s_server.bind(direction)
        self.s_server.listen(5)
        print("Server up!", file=sys.stderr)

    def palindrome(self, word):
        word = word.replace(" ", "").lower()
        if word == word[::-1]:
            return True
        else:
            return False

    def check(self, message):
        if self.palindrome(message):
            return "Es palindroma"
        else:
            return "No es palindroma"

    def run(self):
        self.initialize_connection()
        while True:
            try:
                self.accept()
                while True:
                    petition = self.receive_petition()
                    if petition is None:
                        break
                    word = self.receive_word()
                    self.send_answer(word)
            except KeyboardInterrupt:
                print("Closing server", file=sys.stderr)
                self.s_server.close()
                sys.exit(1)

    def accept(self):
        self.s_client, self.addr = self.s_server.accept()
        print("Connection opened from: ", self.addr, file=sys.stderr)

    def receive_petition(self):
        petition = self.s_client.recv(1024).decode("utf-8")
        if petition == "Frase":
            print("Received:", petition, file=sys.stderr)
            return petition
        elif petition == "Numero":
            print("Received:", petition, file=sys.stderr)
            return petition

    def receive_word(self):
        word = self.s_client.recv(1024).decode("utf-8")
        print("Received word:", word, file=sys.stderr)
        return word

    def send_answer(self, word):
        response = self.check(word)
        self.s_client.send(response.encode("utf-8"))
        print("Sent:", response, file=sys.stderr)

    def disconnect(self):
        print("Closing connection from", self.addr, file=sys.stderr)
        self.s_client.close()


if __name__ == "__main__":
    server = Servidor()
    server.run()
