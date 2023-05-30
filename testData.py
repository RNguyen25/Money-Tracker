import numpy as np
#from mainFunctions import expenses
from mainFunctions import addExpense
from mainFunctions import trackExpense
from mainFunctions import hash
from ExpenseObject import expense
import plotly.express as px
#Test data
testData = np.empty(40,expense)
ex0 = expense("08.01.23", "diamond necklace", 10000, "jewelry")
ex1 = expense("08.01.23", "popcorn", 5.32, "food")
ex2 = expense("08.01.23", "movie ticket", 12.32, "entertainment")
ex3 = expense("08.02.23", "McDoanld's", 3.53, "food")
ex4 = expense("08.03.23", "diamond earrings", 5000, "jewelry")
ex5 = expense("08.04.23", "pizza", 8.32, "food")
ex6 = expense("08.05.23", "chips", 2.94, "food")
ex7 = expense("08.06.23", "McDoanld's", 3.49, "food")
ex8 = expense("08.07.23", "Popeyes", 11.86, "food")
ex9 = expense("08.08.23", "fruits", 9.32, "food")
ex10 = expense("08.09.23", "McDoanld's", 10.99, "food")
ex11 = expense("08.10.23", "Burger", 8.32, "food")
ex12 = expense("08.11.23", "Hangry joes", 17.85, "food")
ex13 = expense("08.12.23", "McDoanld's", 35.10, "food")
ex14 = expense("08.13.23", "Shrimp chips", 5.13, "food")
ex15 = expense("08.14.23", "Honey pig", 35.00, "food")
ex16 = expense("08.15.23", "Iron age", 78.47, "food")
ex17 = expense("08.16.23", "McDoanld's", 3.21, "food")
ex18 = expense("08.17.23", "Meat project", 44.32, "food")
ex19 = expense("08.18.23", "The Qui", 50.22, "food")
ex20 = expense("08.19.23", "Honest Grill", 68.99, "food")
ex21 = expense("08.20.23", "BBQ Chicken and beer", 21.87, "food")
ex22 = expense("08.21.23", "McDoanld's", 00.74, "food")
ex23 = expense("08.22.23", "Apple", 2.21, "food")
ex24 = expense("08.23.23", "Banh mi", 11.98, "food")
ex25 = expense("08.24.23", "Pho", 13.21, "food")
ex26 = expense("08.25.23", "McDoanld's", 8.65, "food")
ex27 = expense("08.26.23", "Coke", 2, "drink")
ex28 = expense("08.27.23", "Meokja Meokja", 80.00, "food")
ex29 = expense("08.28.23", "McDoanld's", 2.53, "food")
ex30 = expense("08.29.23", "Hotspot", 33.32, "food")
ex31 = expense("08.30.23", "Airpods", 250.83, "Technology")
ex32 = expense("08.31.23", "iPad", 700.32, "Technology")
ex33 = expense("08.14.23", "Apple pencil", 93.32, "Technology")
ex34 = expense("08.14.23", "Bowling", 15.32, "entetainment")
ex35 = expense("08.14.23", "Boba", 6.75, "drink")
ex36 = expense("08.25.23", "Shirt", 30.32, "Clothes")
ex37 = expense("08.25.23", "McDoanld's", 43.23, "food")
ex38 = expense("08.25.23", "Movie ticket", 5000, "entertainment")


testData = [ex0, ex1, ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12,ex13,ex14,ex15,ex16,ex17,ex18,ex19,ex20,ex21,ex22,ex23,ex24,ex25,ex26,ex27,ex28,ex29,ex30,ex31,ex32,ex33,ex34,ex35,ex36,ex37,ex38]
'''for data in testData:
    hash(data)'''
for i in testData:
   hash(i)

