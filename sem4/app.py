from cProfile import label
import numpy as np 
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt 
import pandas_datareader as data
from keras.models import load_model
import streamlit as st

start  ='2012-01-01'
end =date.today().strftime("%Y-%m-%d")


st.title('Market Predicitor')

user_input=st.text_input('Stock Ticker','ICICIBANK.NS')
df=data.DataReader(user_input,'yahoo',start,end)

st.subheader('Data')
st.write(df.describe())

st.subheader('Closing Price')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close,label='Closing Price')
plt.legend()
st.pyplot(fig)


st.subheader('Closing Price With 100 Days Moving Average')
ma100= df.Close.rolling(100).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100,label='100 Days MAVG')
plt.plot(df.Close,label='Closing Price')
plt.legend()
st.pyplot(fig)

st.subheader('Closing Price With 200 and 100 Days Moving Average')
ma100= df.Close.rolling(100).mean()
ma200= df.Close.rolling(200).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100,label='100 Days MAVG')
plt.plot(ma200,label='200 Days MAVG')
plt.plot(df.Close)
plt.legend()
st.pyplot(fig)



data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
data_training_array=scaler.fit_transform(data_training)



model= load_model('keras_model1.h5')

past_100_days=data_training.tail(100)
final_df =past_100_days.append(data_testing,ignore_index=True)
input_data=scaler.fit_transform(final_df)
x_test=[]
y_test=[]
for i in range (100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])


x_test ,y_test = np.array(x_test),np.array(y_test)
y_predicated=model.predict(x_test)
scaler=scaler.scale_


scale_factor=1/scaler[0]
y_predicated=y_predicated*scale_factor
y_test=y_test*scale_factor



st.subheader('Prediction')
fig2=plt.figure(figsize=(12,6))
plt.plot(df.Close, 'b', label='Original Price')
plt.plot(y_predicated, 'r', label='Predicated price')
plt.legend()
st.pyplot(fig2)



