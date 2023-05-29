import plotly.express as px
import plotly.graph_objects as go

# This dataframe has 244 lines, but 4 distinct values for `day`
cock = ['food','entertainment','random','asdf']
val = [3, 2, 10, 14]

data=[go.Pie(labels=cock, values=val, textinfo='label+percent', hole=.3)]
fig = go.Figure(data)
#fig.show()

categoryDict = {
  1: "Food & Dining",
  2: "Entertainment",
  3: "Health",
  4: "Groceries",
  5: "Clothes & Accessories",
  6: "Misc."
}

while(True):
    cat = input("num")
    try:
        cat = categoryDict.get(int(cat))
        break
    except:
        print("Please put in a number\n")
