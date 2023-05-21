import pandas as pd
import streamlit as st
import numpy as np
import datetime as dt
import numpy as np 
from datetime import datetime
import pickle
from pickle import dump
from pickle import load
import matplotlib.pyplot as plt
# [1]

st.title('Model Deployment: SARIMA MODEL')
st.subheader('Apple Dataset')


# [2]

df = pd.read_csv(r'C:\Users\PC\Downloads\Data Science\project\AAPL.csv')
df["Date"]=pd.to_datetime(df["Date"])
df.set_index('Date',inplace=True)


# [3]


periods_input = st.slider('Predictions for Days?',min_value = 1, max_value = 60)


# [4]


loaded_model = pickle.load(open(r'C:\Users\PC\Downloads\Data Science\pickle_file.sav', 'rb'))
predict = loaded_model.forecast(periods_input)
fort=pd.DataFrame(predict.values,index=pd.date_range('2019-12-31',  periods=periods_input), columns=["Adj Close"])


# [5]


if st.button("Predict"):
       st.sidebar.markdown(':red[Predictions on Apple stock Exchange (Year : 2012 - 2019)]')
       st.sidebar.write('the Forecasted Days : ',periods_input)
       st.sidebar.write(predict)
  
       # line plot
       fig, ax = plt.subplots(figsize = (12,6))
       ax.plot(df['Adj Close'],label='Adj Close',color='purple')
       ax.plot(fort,label=('forecasted days',periods_input),color='red')
       plt.legend(loc='upper left', fontsize=10)
       plt.suptitle('Apple Stock Price', fontsize=14)
       st.pyplot(fig)

       st.header("About :")
       st.subheader("Mentor: Neha Gupta")
       st.write("P-185 : Team-6 :")
