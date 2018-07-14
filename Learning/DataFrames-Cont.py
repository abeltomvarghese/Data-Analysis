import pandas as pd
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
#MERGING A DATASET
print(pd.merge(df1,df2, on=["HPI","Int_rate"]))
#SETTING NEW INDEX AFTER MERGING
df4 = pd.merge(df1,df3, on="HPI")
df4.set_index("HPI", inplace=True)
print(df4)
#ALTERNATIVE TO SETTING INDEX AFTER MERGING - SET INDEX BEFORE MERGING
df1.set_index("HPI", inplace = True)
df3.set_index("HPI", inplace=True)
joined = df1.join(df3)
print(joined)

#CREATING INDEXES USING DIFFERING COLUMNS OF DATA
df5 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })
df6 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})
merged = pd.merge(df5, df6, on="Year")
print(merged)
#SETTING THE INDEX
merged = pd.merge(df5,df6,on="Year")
merged.set_index("Year", inplace=True)
print(merged)
#USING HOW TO CONTROL DIFFERING DATA IN A COLUMN
merged = pd.merge(df5,df6,on="Year",how="left")
merged.set_index("Year", inplace=True)
print(merged)

merged = pd.merge(df5,df6,on="Year",how="right")
merged.set_index("Year", inplace=True)
print(merged)

merged = pd.merge(df5,df6,on="Year",how="outer")
merged.set_index("Year", inplace=True)
print(merged)

merged = pd.merge(df5,df6,on="Year",how="inner")
merged.set_index("Year", inplace=True)
print(merged)

#USING JOIN FOR DIFFERING DATA IN COLUMNS
df5.set_index("Year", inplace=True)
df6.set_index("Year", inplace=True)
joined = df5.join(df6, how="outer")
print(joined)