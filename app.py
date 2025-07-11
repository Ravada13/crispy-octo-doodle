import pandas as pd
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/SHEFALI RAVADA/OneDrive/Desktop/project vs/trained_model_1.sav','rb'))

trans_dict = {'Manual': 0, 'Automatic': 1, 'Semi-Auto': 2, 'Other': 3}
fuel_dict = {'Petrol': 0, 'Diesel': 1, 'Hybrid': 2, 'Electric': 3, 'Other': 4}







def main():
    st.title("🚗 Ford Car Price Prediction App")
    year = st.number_input("Year", min_value=1990, max_value=2025, value=2020)
    transmission = st.selectbox("Transmission", ['Manual', 'Automatic', 'Semi-Auto', 'Other'])
    mileage = st.number_input("Mileage", value=30000)
    fuelType = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Hybrid', 'Electric', 'Other'])
    tax = st.number_input("Tax", value=150)
    mpg = st.number_input("Miles per Gallon (mpg)", value=50.0)
    engineSize = st.number_input("Engine Size (liters)", value=1.6)
    
    


    if st.button("Predict Price"):
        input_data = pd.DataFrame({
            'year': [year],
            'transmission': [trans_dict[transmission]],
            'mileage': [mileage],
            'fuelType': [fuel_dict[fuelType]],
            'tax': [tax],
            'mpg': [mpg],
            'engineSize': [engineSize]
            
            
        })
        prediction = loaded_model.predict(input_data)[0]
        st.success(f"Estimated Car Price: £{round(prediction, 2)}")



if __name__=='__main__':
    main()