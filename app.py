# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 23:31:02 2022

@author: Abi
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import sklearn


# loading the saved model
loaded_model = pickle.load(open('D:/Project/rf_regressor.pkl', 'rb'))

def predict_price(brand, min_cost_price, max_cost_price, vehicle_age,km_driven, fuel_type, 
                  transmission_type, mileage, engine, max_power, seats):

    input_data = {"brand": [brand], "min_cost_price":[min_cost_price],"max_cost_price":[max_cost_price],
            "vehicle_age": [vehicle_age],"km_driven":[km_driven], "fuel_type":[fuel_type],"transmission_type":[transmission_type], "mileage":[mileage],"engine":[engine],"max_power":[max_power],"seats":seats}
    df = pd.DataFrame(input_data)
    y = loaded_model.predict(df)
    st.write("The estimated price is",round(y[0]))
    return(y[0])
             
    
def main():
    # giving a title
        
    html_temp = """
    <div style="background-color:white;padding:1.0px">
    <h1 style="color:black;text-align:center;">Used Car Price Prediction</h1>
    </div><br>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # getting the input data from the user
    
    brand_val= st.selectbox('Select brand of the car',('Audi', 'BMW', 'Bentley', 'Datsun', 'Ferrari', 'Force', 'Ford', 'Honda',
                                'Hyundai', 'ISUZU', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Land Rover', 'Lexus', 'MG',
                                'Mahindra', 'Maruti', 'Maserati', 'Mercedes-AMG', 'Mercedes-Benz', 'Mini',
                                'Nissan', 'Porsche', 'Renault', 'Rolls-Royce', 'Skoda', 'Tata', 'Toyota',
                                'Volkswagen', 'Volvo'), key='car_brand')

    if(brand_val=='Audi'):
        brand=0
    elif(brand_val=='BMW'):
        brand=1
    elif(brand_val=='Bentley'):
        brand=2
    elif(brand_val=='Datsun'):
        brand=3
    elif(brand_val=='Ferrari'):
        brand=4
    elif(brand_val=='Force'):
        brand=5
    elif(brand_val=='Ford'):
        brand=6
    elif(brand_val=='Honda'):
        brand=7
    elif(brand_val=='Hyundai'):
        brand=8
    elif(brand_val=='ISUZU'):
        brand=9
    elif(brand_val=='Isuzu'):
        brand=10
    elif(brand_val=='Jaguar'):
        brand=11
    elif(brand_val=='Jeep'):
        brand=12
    elif(brand_val=='Kia'):
        brand=13
    elif(brand_val=='Land Rover'):
        brand=14
    elif(brand_val=='Lexus'):
        brand=15
    elif(brand_val=='MG'):
        brand=16
    elif(brand_val=='Mahindra'):
        brand=17
    elif(brand_val=='Maruti'):
        brand=18
    elif(brand_val=='Maserati'):
        brand=19
    elif(brand_val=='Mercedes-AMG'):
        brand=20
    elif(brand_val=='Mercedes-Benz'):
        brand=21
    elif(brand_val=='Mini'):
        brand=22
    elif(brand_val=='Nissan'):
        brand=23
    elif(brand_val=='Porsche'):
        brand=24
    elif(brand_val=='Renault'):
        brand=25
    elif(brand_val=='Rolls-Royce'):
        brand=26
    elif(brand_val=='Skoda'):
        brand=27
    elif(brand_val=='Tata'):
        brand=28
    elif(brand_val=='Toyota'):
        brand=29
    elif(brand_val=='Volkswagen'):
        brand=30
    elif(brand_val=='Volvo'):
        brand=31
    
    min_cost = st.number_input('Enter the minimum cost price',step=10000, key ='min_price') 
    max_cost = st.number_input('Enter the maximum cost price',step=10000, key ='max_price') 
    age = st.number_input('Enter the age of the car',step=1, key ='age') 
    kms = st.number_input('Enter kilometer driven',step=1000, key ='kms') 
   
    
    Fuel_Type = st.selectbox('Select fuel type',("CNG" ,'Diesel' ,'Electric', 'LPG', 'Petrol'), key='fuel')
    if(Fuel_Type=='CNG'):
        fuel_type=0
    elif(Fuel_Type=='Diesel'):
        fuel_type=1
    elif(Fuel_Type=='Electric'):
        fuel_type=2
    elif(Fuel_Type=='LPG'):
        fuel_type=3
    else:
        fuel_type=4
        
    Transmission = st.selectbox('What is the Transmission Type ', ('Manual','Automatic'), key='manual')
    if(Transmission =='Manual'):
        trans =1 
    else:
        trans = 0
     
    mile = st.number_input('Enter mileage',step=1, key ='mile') 
    eng = st.number_input('Enter engine capacity',step=100, key ='eng') 
    power = st.number_input('Enter power',step=10, key ='power') 
    seats = st.number_input('Enter number of seats',step=1, key ='seats') 
    
    if st.button("Estimate Price", key='predict'):
        predict_price(brand, min_cost, max_cost, age,kms, fuel_type,trans, mile, eng, power, seats)
        

if __name__ == '__main__':
    main()