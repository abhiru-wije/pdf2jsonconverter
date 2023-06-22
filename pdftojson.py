import streamlit as st
from nanonets import NANONETSOCR
import tempfile
import os

def process_file(file):
    model = NANONETSOCR()
    model.set_token('95e09787-0a63-11ee-9c73-1e85f057e35b')
    pred_json = model.convert_to_prediction(file)
    value = pred_json['results'][0]['page_data'][0]['raw_text']
    return value

st.title('PDF to JSON Conveter')

uploaded_file = st.file_uploader("Choose a file", type="pdf")
if uploaded_file is not None:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())

    temp_file.close()

    file_path = temp_file.name

    with open(file_path, "rb") as file:
        print(file.read())

    os.remove(file_path)

    result = process_file(uploaded_file)
    st.write(result)

