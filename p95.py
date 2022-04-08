#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


st.title('Model Deployment: Random forest Regressor' )
st.sidebar.header('User input Parameters')


def user_input_features():
    ambient  = st.sidebar.number_input('Insert Scaled  ambient temperature',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    coolant  = st.sidebar.number_input('Insert Scaled coolant temperature',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    u_d = st.sidebar.number_input('Insert Scaled u_d',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    u_q = st.sidebar.number_input('Insert Scaled u_q',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")    
    motor_speed  = st.sidebar.number_input('Insert Scaled motor_speed',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    i_d = st.sidebar.number_input('Insert Scaled i_d',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    i_q = st.sidebar.number_input('Insert Scaled i_q',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    stator_yoke  = st.sidebar.number_input('Insert Scaled stator_yoke temperature',min_value=-3.0,max_value=3.0,step=1e-4,format="%.4f")
    data={ 'ambient':ambient,
            'coolant':coolant,
          'u_d':u_d,
          'u_q':u_q,
          'motor_speed':motor_speed,
          'i_d':i_d,
          'i_q':i_q,
          'stator_yoke':stator_yoke}
    features=pd.DataFrame(data,index=[0])
    return features

df = user_input_features()
st.subheader('user input parameters')
st.write(df)

motor=pd.read_csv("temperature_data.csv")
motor.drop("profile_id",axis=1,inplace=True)
motor.drop("stator_tooth",axis=1,inplace=True)
motor.drop("stator_winding",axis=1,inplace=True)
motor.drop("torque",axis=1,inplace=True)
min_thershold,max_thershold=motor["pm"].quantile([0.1,0.9])
motor=motor[(motor["pm"]>min_thershold) & (motor["pm"]<max_thershold)]
X=motor.drop("pm",axis=1)
y=motor["pm"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=45)

rf = RandomForestRegressor(random_state=45)
rf.fit(X_train,y_train)

predicted_result = rf.predict(df)[0]

st.subheader('Model Result')
st.write("The Scaled rotor temperature is : {:.4f}".format(predicted_result))


