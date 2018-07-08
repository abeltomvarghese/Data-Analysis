import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')
start = datetime.datetime(2010,1,1)
end = datetime.datetime.now()
df = web.DataReader("XOM", "morningstar",start,end)

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis = 1)
print(df.head().to_string())
df['High'].plot()
plt.legend()
plt.show()