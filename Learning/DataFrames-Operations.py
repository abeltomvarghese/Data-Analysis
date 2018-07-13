import pandas as pd
#CONCATENATING A DATAFRAME
df1 = pd.DataFrame({"HPI": [80,85,88,85],
       "Int-Rate": [2,3,2,2],
       "US_GDP_THOUSANDS": [50,55,65,55]},
        index=[2001,2002,2003,2004])
df2 = pd.DataFrame({"HPI": [80,85,88,85],
                    "Int-Rate": [2,3,2,2],
                    "US_GDP_THOUSANDS": [50,55,65,55]},
                   index=[2005,2006,2007,2008])
df3 = pd.DataFrame({"HPI":[80,85,88,85],
                    "Int-Rate":[2,3,2,2],
                    "Low_Tier_HPI":[50,52,50,53]},
                   index=[2001,2002,2003,2004])
concat = pd.concat([df1,df2,df3])
#print(concat)
#APPENDING A DATAFRAME
df4 = df1.append(df2)
print(df4)
#APPENDING A NEW RECORD
s = pd.Series([80,2,50], index=['HPI','Int-Rate','US_GDP_THOUSANDS'])
df5 = df1.append(s, ignore_index=True)
print(df5.to_string())