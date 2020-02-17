import json
import os
from bs4 import BeautifulSoup
import lxml
actualDir = os.path.dirname(os.path.abspath(__file__))
actualDir = os.path.join(actualDir, "NLP_Course", "Datasets\\")
os.chdir(actualDir)

with open('trump.json', encoding="utf8") as f:
    tweets = json.load(f)

print(len(tweets))

for tweet in tweets:
    print(tweet["text"])
    break

nextDir = os.path.join(actualDir,"Articles\\")
for filename in os.listdir(nextDir):
    if ".txt" in filename:
        doc = open(nextDir + filename, "r")
        doc = doc.read()

        # look at the original HTML
        soup = str(doc).split("<!-- END WAYBACK TOOLBAR INSERT -->")[0]

        soup = BeautifulSoup(soup, "html.parser")

        text = " "

        # simply take all the paragraphs
        for para in soup.findAll("p"):
            print(para)
            text += para.text

        print(text)

        break


