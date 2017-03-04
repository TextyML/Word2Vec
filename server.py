import gensim
import asyncore
import socket
import os
import ast

word2vec = gensim.models.KeyedVectors.load_word2vec_format(os.getcwd() + "/model.bin.gz", binary=True)
word2vec.init_sims(replace=True)


class EchoHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)

        if data:
            data = ast.literal_eval(data.decode('utf8'))
            method = data["method"]
            parameter = data["parameter"]

            print("===== Receiving Parameters ====")
            print("Method:", method)
            print("Parameter:", parameter)
            print("===== End of Transmission ====")

            func = word2vec.__getattribute__(method)
            if not func:
                print("Method:", method, "not found")
            else:
                parameter = dict(parameter)
                result = func(**parameter)
                print("==== Results ====")
                print(result)
                print("==== End ====")
                self.send(str.encode(str(result)))


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from %s' % repr(addr))
            handler = EchoHandler(sock)

if __name__ == "__main__":
    server = EchoServer('localhost', 4444)
    print("Server started")
    asyncore.loop()
