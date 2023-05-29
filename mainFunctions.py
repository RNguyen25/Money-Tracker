import numpy as np
from ExpenseObject import expense
sep ="-------------------------"
#different lists for different months
expenses1 = np.empty(32, expense)
expenses2 = np.empty(32, expense)
expenses3 = np.empty(32, expense)
expenses4 = np.empty(32, expense)
expenses5 = np.empty(32, expense)
expenses6 = np.empty(32, expense)
expenses7 = np.empty(32, expense)
expenses8 = np.empty(32, expense)
expenses9 = np.empty(32, expense)
expenses10 = np.empty(32, expense)
expenses11 = np.empty(32, expense)
expenses12 = np.empty(32, expense)

#hashcode 1
#months dictionary
monthsDict = {
  1: expenses1,
  2: expenses2,
  3: expenses3,
  4: expenses4,
  5: expenses5,
  6: expenses6,
  7: expenses7,
  8: expenses8,
  9: expenses9,
  10: expenses10,
  11: expenses11,
  12: expenses12
}

def hash(exp):
  '''month = int(exp.getMonth())
  if month == 1:
    hashMonth(exp, expenses1)
  if month == 2:
    hashMonth(exp, expenses2)
  if month == 3:
    hashMonth(exp, expenses3)
  if month == 4:
    hashMonth(exp, expenses4)
  if month == 5:
    hashMonth(exp, expenses5)
  if month == 6:
    hashMonth(exp, expenses6)
  if month == 7:
    hashMonth(exp, expenses7)
  if month == 8:
    hashMonth(exp, expenses8)
  if month == 9:
    hashMonth(exp, expenses9)
  if month == 10:
    hashMonth(exp, expenses10)
  if month == 11:
    hashMonth(exp, expenses11)
  if month == 12: 
    hashMonth(exp, expenses12)'''
  list = monthsDict.get(int(exp.getMonth()))
  hashMonth(exp,list)

def hashMonth(exp, list):
  head = list[exp.getDay()] 
  if head == None:
    list[exp.getDay()] = exp
  else:
    curr = head
    while (True): 
      if curr.getNext() == "":
        curr.setNext(exp)
        break
      else:
        curr = curr.getNext()

#prompts to add an expense
categoryDict = {
  1: "Food & Dining",
  2: "Entertainment",
  3: "Health",
  4: "Groceries",
  5: "Clothes",
  6: "Misc."
}
def addExpense():
 # while (True):
    da = input("\nWhen was this expense? (mm.dd.yy)   \n")
    n = input("Ok what is the expense? (name)   \n")
    c = input("Ok what is the cost? (xx.xx)   \n")
    #category loop using dictionary
    print("What category does it lie under?   \n" + sep)
    print(categoryDict)
    while(True):  
      while(True):
        cat = input()
        try:
          cat = categoryDict.get(int(cat))
          break
        except:
          print("Please put in a number")
      if(cat != None):
        break
      else:
        print("Please put in a number 1-6")
    e1 = expense(da,n, c, cat)
    hash(e1)

#prompts user to track an expense
def trackExpense():
  month = input("\nwhat month of expense would you like to see? (numbers EX. January = 1)\n")
  intMonth = int(month)
  if intMonth == 1:
    trackExpenseMonth(expenses1)
  if intMonth == 2:
    trackExpenseMonth(expenses2)
  if intMonth == 3:
    trackExpenseMonth(expenses3)
  if intMonth == 4:
    trackExpenseMonth(expenses4)
  if intMonth == 5:
    trackExpenseMonth(expenses5)
  if intMonth == 6:
    trackExpenseMonth(expenses6)
  if intMonth == 7:
    trackExpenseMonth(expenses7)
  if intMonth == 8:
    trackExpenseMonth(expenses8)
  if intMonth == 9:
    trackExpenseMonth(expenses9)
  if intMonth == 10:
    trackExpenseMonth(expenses10)
  if intMonth == 11:
    trackExpenseMonth(expenses11)
  if intMonth == 12: 
    trackExpenseMonth(expenses12)
  
def trackExpenseMonth(list):
  #while (True):
    i = input("\nwhat day of expense would you like to see\n")
    curr = list[int(i)]
    print("\nHere is the all the expenses on " + i + "\n" + sep)
    while (True):
      print(curr)
      try:
        if curr.getNext() != "":
          curr = curr.getNext()
        else:
          break
      except:
        break
    #done = input("are you done (yes)\n")
    #if (done == "yes"):
     # break