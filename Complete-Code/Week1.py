import codecs # serve per aprire file txt
import json
import os
from collections import Counter

# Qui imparo a impostare le working directory

actualDir = os.path.dirname(os.path.abspath(__file__))

projectDir = os.path.join(actualDir, "NLP_Course", "Datasets", "trump.json")


# aprire i file con le directory dinamiche
speech = codecs.open(projectDir,"r","utf-8")

# legge i testi
speech = speech.read()

# tokenizza
words = speech.split(" ")

# prende le parole più usate
words = [x.lower() for x in words]
counting_words = Counter(words)

print(counting_words.most_common(2))