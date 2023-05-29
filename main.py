from mainFunctions import trackExpense
from mainFunctions import addExpense
import test
sep ="-------------------------"
def main():
    whatDo = input("\nWhat do you want to do?\n" + sep + "\nTrack, Add\n")
    if (whatDo.lower() == "track"):
        trackExpense()
    if (whatDo.lower() == "add"):
        addExpense()


while(True):
    main()
    flag = input("\nFinished?\n" + sep + "\n(yes, no)\n")
    if (flag.lower()== "yes"):
        break

