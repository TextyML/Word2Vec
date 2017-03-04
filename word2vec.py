import gensim
import os
import socket
import ast
import json


def build_request(method, parameter):
    return str({"method": method,
                "parameter": parameter})


class Word2Vec(object):
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self._sock.close()

    def connect(self, host="localhost", port=4444):
        server_address = (host, port)
        print('connecting to %s port %s' % server_address)
        self._sock.connect(server_address)

    def send(self, data):
        self._sock.send(str.encode(data))

    def receive(self):
        data = self._sock.recv(8192).decode('utf8')
        return ast.literal_eval(data)

    def getparams(self, parameter):
        try:
            del parameter['self']
        except KeyError:
            pass

        return parameter

    def doesnt_match(self, words):
        self.send(build_request("doesnt_match", self.getparams(locals())))
        return self.receive()

    def similar_by_word(self, word, topn=10, restrict_vocab=None):
        self.send(build_request("similar_by_word", self.getparams(locals())))
        return self.receive()

    def most_similar(self, positive=[], negative=[], topn=10, restrict_vocab=None, indexer=None):
        self.send(build_request("most_similar", locals()))
        return self.receive()

    def wmdistance(self, document1, document2):
        self.send(build_request("wmdistance", locals()))
        return self.receive()

    def similar_by_vector(self, vector, topn=10, restrict_vocab=None):
        self.send(build_request("similar_by_vector", locals()))
        return self.receive()

    def n_similarity(self, ws1, ws2):
        self.send(build_request("n_similarity", locals()))
        return self.receive()

    def similarity(self, w1, w2):
        self.send(build_request("similarity", locals()))
        return self.receive()

    def most_similar_cosmul(self, positive=[], negative=[], topn=10):
        self.send(build_request("most_similar_cosmul", locals()))
        return self.receive()
