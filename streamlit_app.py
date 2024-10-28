# Import libraries
from convert_to_text import convert_to_text
import time
import joblib
import streamlit as st

# Load model
start = time.time()
model = joblib.load("rnd_clf.pkl")
end = time.time()
load_time = end-start
st.text('Ladezeit für Modell: ' + str(load_time) + "s")

# Load images
col1, col2 = st.columns(2, gap='large', vertical_alignment='center')

with col1:
    st.image('ukd_logo.jpg', width=250)

with col2:
    st.image('uoz_wort-bildmarke_rahmenlos_lang_rgb-1.png', width=150)

# The title
st.title('Textgenerator für das prätherapeutische Tumorboard')

# The header
st.header('Bitte Patientenparameter eingeben:')

# Input for patient age
age = st.number_input('Alter (Jahre):', step=10.0)

# Input for patient psa serum level
psa = st.number_input('PSA (ng/ml):', step=1.0)

# Input for dre stage
dre_options = {'cT1': 0, 'cT2a': 1, 'cT2b': 2, 'cT2c': 3, 'cT3a': 4, 'cT3b': 5}
input_dre = st.selectbox('DRU:', dre_options.keys())
dre = dre_options[input_dre]

# Input for gleason score
gleason_sum = st.selectbox('Gleason Score:', ['6', '7', '8', '9', '10'])

# Input for number of positive biopsy cores
cylinder_pos = st.number_input('Zahl der positiven Stanzzylinder:', step=1.0)

# Input for overall biopsy cores
cylinder_max = st.number_input('Zahl der gesamten Stanzzylinder:', step=1.0)

# Run model prediction
button_predict = st.button('Prädiktion')

if button_predict:
    start = time.time()
    prediction = model.predict([[age, psa, dre, gleason_sum, cylinder_pos, cylinder_max]])
    end = time.time()
    prediction_time = end - start
    prediction_text = convert_to_text(prediction[0])
    st.markdown(prediction_text)
    st.text('Outcome Variable: ' + str(prediction))
    st.text('Berechnungszeit: ' + str(prediction_time))


