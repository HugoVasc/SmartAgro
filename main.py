import streamlit as st
import pandas as pd
from joblib import load

# Load the model
model = load('gradient_boosting_model.pkl')

# Create the title
st.title('Smart Agro')

nitrogen = st.number_input('Medição de Nitrogênio do Solo', min_value=0.0, max_value=1000.0, value=0.0, step=1.0, format="%.2f")
phosphorus = st.number_input('Medição de Fósforo do Solo', min_value=0.0, max_value=1000.0, value=0.0, step=1.0, format="%.2f")
potassium = st.number_input('Medição de Potássio do Solo', min_value=0.0, max_value=1000.0, value=0.0, step=1.0, format="%.2f")
temperature = st.number_input('Temperatura (ºC)', min_value=-50.0, max_value=100.0, value=0.0, step=0.0005, format="%.6f")
humidity = st.number_input('Umidade', min_value=0.0, max_value=100.0, value=0.0, step=0.0005, format="%.6f")
ph = st.number_input('pH', min_value=0.0, max_value=14.0, value=0.0, step=0.0005, format="%.6f")
rainfall = st.number_input('Precipitação pluvial', min_value=0.0, max_value=10000.0, value=0.0, step=0.0005, format="%.6f")

# Transforma Temperatura de Celsius para Fahrenheit
temperature = (temperature * 1.8) + 32

data = {
  'N': nitrogen,
  'P': phosphorus,
  'K': potassium,
  'temperature': temperature,
  'humidity': humidity,
  'ph': ph,
  'rainfall': rainfall
}

labels = {
  "rice": "arroz",            
  "maize": "milho",           
  "jute": "juta",            
  "cotton": "algodão",          
  "coconut": "coco",         
  "papaya": "mamão",          
  "orange": "laranja",          
  "apple": "maçã",           
  "muskmelon": "melão almiscarado",       
  "watermelon": "melancia",      
  "grapes": "uvas",          
  "mango": "manga",           
  "banana": "banana",          
  "pomegranate": "romã",     
  "lentil": "lentilha",          
  "blackgram": "grama preta",       
  "mungbean": "feijão mungo",        
  "mothbeans": "naftalina",       
  "pigeonpeas": "feijão bóer",      
  "kidneybeans": "feijão",     
  "chickpea": "grão de bico",        
  "coffee": "café"
}


#Tansforma em dataframe
df = pd.DataFrame(data, index=[0])


# Create a button
btn_predict = st.button('Recomendar Cultura', type="primary")


if btn_predict:
  prediction = model.predict(df)
  st.success(f'A cultura recomendada é {labels[prediction[0]]}')