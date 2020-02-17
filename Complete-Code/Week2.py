import json
import os
from bs4 import BeautifulSoup
actualDir = os.path.dirname(os.path.abspath(__file__))
actualDir = os.path.join(actualDir, "NLP_Course", "Datasets\\")
os.chdir(actualDir)

with open('trump.json', encoding="utf8") as f:
    tweets = json.load(f)

print(len(tweets))

for tweet in tweets:
    print(tweet["text"])
    break

for filename in os.listdir(actualDir):
    if ".txt" in filename:
        print(filename)
        doc = open(actualDir + "/" +filename, "r")
        doc = doc.read()

        # look at the original HTML
        soup = str(doc).split("<!-- END WAYBACK TOOLBAR INSERT -->")[1]

        soup = BeautifulSoup(soup, "lxml")

        text = ""

        # simply take all the paragraphs
        for para in soup.find_all('p'):
            text += para.text

        print(text)
        print(" ")
        break