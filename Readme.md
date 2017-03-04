# Allgemeines
Dieses Projekt stellt die Word2Vec API von gensim mittels Sockets im Netzwerk bereit.
Der Client verfügt über ein eigenes Interface um mit gensim zu interagieren, dies ermöglicht CodeCompletion in IDEs.

# Server starten
In der server.py den Host und Ports anpassen (verbesserungswürdig).

In der Konsole ausführen:
```bash
python server.py
```

# Client
Zur Nutzung des Servers hier Beispielcode:

```python
from word2vec import Word2Vec
word2vec = Word2Vec()
word2vec.connect()
print(word2vec.similar_by_word(word="la"))
word2vec.close()
```

# Hinweise
Den Server nur im lokalen Netzwerk ausführen, da keine Sicherheitsmechanismen eingebaut sind.

