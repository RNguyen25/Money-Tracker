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
listDict = {
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
  list = listDict.get(int(exp.getMonth()))
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
      cat = input()
      try:
        cat = categoryDict.get(int(cat))
        if(cat!=None):
          break
        else:
          print("Please put in a number 1-6")
      except:
        print("Please put in a number")
    e1 = expense(da,n, c, cat)
    hash(e1)

#prompts user to track an expense
monthDict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
def trackExpense():
  print("\nwhat month of expense would you like to see?\n" + sep)
  print(monthDict)
  while(True):
    month = input()
    try:
      if (int(month) <=12) and (int(month) > 0):
        list = listDict.get(int(month))
        break
      else:
        print("Please type in a valid number")
    except:
      print("Please type in a number")
  trackExpenseMonth(list)
  
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