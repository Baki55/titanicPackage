import streamlit
import json
import requests

streamlit.title("Prediction for Titanic problem (Kaggle)")

streamlit.write("\nWe choose five parameters to train our Machine Learning Model:")
streamlit.write("-Pclass: Ticket class")
streamlit.write("-SibSp: Number of siblings/spouses aboard the Titanic")
streamlit.write("-Parch: Number of parents/childrens aboard the Titanic")
streamlit.write("-Sex_female: 0 (True) or 1 (False)")
streamlit.write("-Sex_male: 0 (True) or 1 (False)\n")

Pclass = streamlit.slider('Pclass', 1, 3, 1)
SibSp = streamlit.slider('SibSp', 1, 5, 1)
Parch = streamlit.slider('Parch', 1, 5, 1)
Sex_female = streamlit.number_input('Sex_female', min_value=0, max_value=1)
Sex_male = streamlit.number_input('Sex_male', min_value=0, max_value=1)

inputs = {"Pclass": int(Pclass),
				"SibSp": int(SibSp),
				"Parch": int(Parch),
				"Sex_female": int(Sex_female),
				"Sex_male": int(Sex_male)}

if streamlit.button('Prediction'):
	res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(inputs))
	streamlit.subheader(f"Response from API = {res.text}")