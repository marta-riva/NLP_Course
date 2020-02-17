import codecs # serve per aprire file txt
import os

# printing, small for e cazzate varie

counter = 0
for i in range(10):
    counter = counter + 1
    print(counter)


# creare liste, appendere roba
shopping_bag = ["ice-cream","peanut butter","tomatoes","beer"]

shopping_bag.append("pasta")

shopping_bag.remove("tomatoes")
print (shopping_bag)

# dizionari
shopping_bag = {'ice-cream':3, 'peanut butter':1, 'beer':6, 'pasta':2}
print (shopping_bag["ice-cream"])



# importiamo e leggiamo i testi

abspath = os.path.abspath(__file__)
