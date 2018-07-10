import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
web_stats = {"Day":[1,2,3,4,5,6],
             "Visitors":[43,34,65,56,29,76],
             "Bounce Rate": [65,67,78,65,45,52]}
#CONVERT TO DATAFRAME
df = pd.DataFrame(web_stats)
#PRINT THE FIRST FEW VALUES
print(df.head())
#PRINT LAST FEW LINES
print(df.tail())
#SPECIFY HOW MANY OF THE LAST ITEMS YOU WANT
print(df.tail(2))
#SET INDEX FOR THE DATA USING A DATA COLUMN THAT CONNECTS ALL OTHER COLUMNS
df.set_index("Day", inplace=True)   #INPLACE HELPS US TO MODIFY THE DATAFRAME
df[["Visitors", "Bounce Rate"]].plot()   #YOU CAN PLOT THE ENTIRE DICTIONARY (VISITORS AND BOUNCE RATE) BY DOING df.plot()
plt.show()
