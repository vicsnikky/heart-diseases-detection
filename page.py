import numpy as np
import pickle 
import streamlit as st
from sklearn.preprocessing import LabelEncoder
import pandas as pd


#load the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#Creatinng a function for prediction

def heart_disease_prediction(input_data):

#change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

#reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return 'The person doesnt have heart disease'
    else:
        return 'The person have heart disease'


def main():
  
  #giving a title
  st.title('Heart Disease Detection Web App')

  #getting the inpute data from the user
age = st.text_input('Enter your age: ')
sex  = st.text_input('Sex' )
cp = st.text_input('Chest pain type' )
trestbps = st.text_input('Resting blood pressure: ')
chol = st.text_input('Serum cholestoral in mg/dl: ')
fbs = st.text_input('Fasting blood sugar' )
restecg = st.text_input('Resting electrocardiographic results: ')
thalach = st.text_input('Maximum heart rate achieved: ')
exang = st.text_input('Exercise induced angina: ' )
oldpeak = st.text_input('oldpeak ')
slope = st.text_input('he slope of the peak exercise ST segmen: ')
ca = st.text_input('number of major vessels' )
thal = st.text_input('thal' )
    
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    #code for prediction

diagnosis = ''

#creating a button for prediction
    
if st.button('Heart Test Result'):
        age_int = int(age)
        sex_int = int(sex)
        cp_int = int(cp)
        trestbps_int = int(trestbps)
        chol_int = int(chol)
        fbs_int = int(fbs)
        restecg_int = int(restecg)
        thalach_int = int(thalach)
        exang_int = int(exang)
        oldpeak_float = float(oldpeak)
        slope_int = int(slope)
        ca_int = int(ca)
        thal_int = int(thal)

        diagnosis = heart_disease_prediction([age_int,sex_int,cp_int,trestbps_int,chol_int,fbs_int,restecg_int,thalach_int,exang_int,oldpeak_float,slope_int,ca_int,thal_int])

st.success(diagnosis)
  
    
if __name__ == '__main__':
    main()
    