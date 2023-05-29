import numpy as np

#class for object: 'expense'
class expense:
  month = ""
  day = ""
  year = ""
  date = ""
  name = ""
  cost = ""
  category = ""
  next = ""
  
  #default constructor
  def __init__(self):
    self.month = ""

  #constructor
  def __init__(self, da, n, c, cat):
    currString = ""
    count = 0.0
    self.date = da
    for char in da:
      if (char!='.'):
        currString += char
        count += 1.0
        if (count/2 == 1):
          self.month = currString
        if (count/2 == 2):
          self.day = currString
        if (count/2 == 3):
          self.year = currString
      else:
        currString = ""
      '''
        match (count/2):
        case 1:
          self.month = currString
        case 2:
          self.day = currString
        case 3:
          self.year = currString
      '''
    self.name = n
    self.cost = c
    self.category = cat

  #toString() function
  def __str__(self):
    return self.date + ": " + self.name + ", " + str(self.cost) + ", " + self.category

  #'get' functions
  def getDay(self):
    return int(self.day)
  def getNext(self):
    return self.next    
  def getCost(self):
    return self.cost
  def getMonth(self):
    return self.month

  #'set' functions
  def setMonth(self, e):
    self.month = e
  def setDay(self, e):
    self.day = e
  def setYear(self, e):
    self.year = e
  def setCost(self, e):
    self.cost = e
  def setCategory(self, e):
    self.category = e
  def setNext(self, e):
    self.next = e
