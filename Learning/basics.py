import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
web_stats = {'Day': [1,2,3,4,5,6],
             'Visitors': [43,53,34,45,64,34],
             'Bounce_Rate': [65,72,62,64,54,66]}
df = pd.DataFrame(web_stats)
##print(df)   #printing the entire dataframe
##print(df.head()) #print the first n-1 rows
##print(df.tail()) #print the last bit of dataframe
##print(df.tail(2)) #prints last 2 rows of dataframe
##print(df.set_index('Day'))  #set the day as the index
##df2 = df.set_index('Day')
##print(df2)

#to select a particular column
#print(df['Visitors'])
#print(df.Visitors)

#printing out select columns
#print(df[['Bounce_Rate','Visitors']])

#printing out a column in a list
#print(df.Visitors.tolist())

# #converting columns to an array
# print(np.array(df[['Bounce_Rate','Visitors']]))
#print(np.array(df['Bounce_Rate']))


df3 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
print(df3)