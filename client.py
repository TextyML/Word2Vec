from word2vec import Word2Vec

word2vec = Word2Vec()

word2vec.connect()

print(word2vec.similar_by_word(word="la"))

word2vec.close()

