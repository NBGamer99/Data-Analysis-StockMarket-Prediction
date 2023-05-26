import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import os
import plotly.express as px
import plotly.graph_objects as go
from VAR import *
from keras.layers import Dense, Dropout, LSTM
from keras. models import Sequential


# os.chdir(os.path.dirname(os.path.realpath(__file__)))


########################################################################
# Toolspack


COLUMNS = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

def convert_to_float(list):
	return [float(x) for x in list]

def get_Stocks(SYMBOL):
	df = pd.read_csv('./Data/'+SYMBOL+'.csv')
	return df

########################################################################


# Company Infos
COMPANIES = SYMBOLS.values()

st.title("Stock Market Predictions")
option = st.selectbox('Enter Stock Symbol',COMPANIES)

df = get_Stocks(str(option))
print(df.head())

st.subheader('Data from 2010 to 2019')
st.dataframe(df.describe(), width=2000)

st.subheader('Closing Price during time')
fig = px.line(df.Close, x=df.index, y=df.Close)
st.write(fig)

st.subheader('Candle Graph to visualize Open, High, Low, Close Price during time')
fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']))
st.plotly_chart(fig)

st.subheader('Volume distribution during time')
fig = px.bar(df.Volume, x=df.index, y=df.Volume, color=df.Volume)
st.write(fig)


# Splitting Data into Training and Testing
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.7)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.7):int(len(df))])

scaler = MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)

# Loading the data
x_train = []
y_train = []

for i in range(100, data_training_array.shape[0]):
	x_train.append(data_training_array[i-100:i])
	y_train.append(data_training_array[i,0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Building the Model

model = None

with st.spinner('Wait The model is on his way ...'):
	if model is None and not check_file_exists("./keras_model.h5"):
		with st.echo(code_location="below"):
			model = Sequential()
			model.add(LSTM(units = 50, activation='relu', return_sequences = True, input_shape=(x_train.shape[1], 1)))
			model.add(Dropout(0.2))
			model.add(LSTM(units = 60, activation='relu', return_sequences = True))
			model.add(Dropout(0.3))
			model.add(LSTM(units = 80, activation='relu', return_sequences = True))
			model.add(Dropout(0.4))
			model.add(LSTM(units = 120, activation='relu'))
			model.add(Dropout(0.5))
			model.add(Dense(units=1))

			# Compile and train the model
			model.compile(optimizer='adam', loss='mean_squared_error')
			st.write(model.fit(x_train, y_train, epochs=50, verbose=1))

			# Save the model
			model.save('keras_model.h5')


# load the model
model = load_model('./keras_model.h5')
st.success("Model Generated and Loaded Successfully !", icon="✅")

past_100_days = data_training.tail(100)
input_data = scaler.fit_transform(data_testing)

# Testing the model
x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
	x_test.append(input_data[i-100:i])
	y_test.append(input_data[i,0])

x_test, y_test = np.array(x_test), np.array(y_test)

# Making Predictions
y_predicted = model.predict(x_test)

# Normalize the data
domin = float(scaler.scale_[0])
scale_factor = 1/domin
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor

st.subheader('Model Prediction')
fig = plt.figure(figsize =(12,6))
plt.plot(y_test, 'b', label="Original Price")
plt.plot(y_predicted, 'r', label="Predicted Price")
plt.xlabel("Time")
plt.ylabel("Price in USD")
plt.legend()
st.pyplot(fig)

# You can access the value at any point with:
# st.session_state.name
