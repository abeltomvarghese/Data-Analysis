import quandl
import pickle
import pandas as pd
api_key = open("APIKey.txt","r").read()
pickle_out = open("fiddy_states.pickle","wb")

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
main_df = pd.DataFrame()
for abbv in fiddy_states[0][1][1:]:
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken=api_key)
    df.rename(columns={"Value":abbv}, inplace=True)
    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)

pickle.dump(main_df,pickle_out)
pickle_out.close()
