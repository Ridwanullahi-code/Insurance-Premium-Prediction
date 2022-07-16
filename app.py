import numpy as np
import pandas as pd 
import pickle
import streamlit as st

st.set_page_config(layout="wide")

def load_model():
	with open('random_forest_regressor_model.pkl', 'rb') as file:
		model = pickle.load(file)
	return model

def show_predict_page():
	
	st.markdown(f'''<h1 style="color:black;font-size:35px;
	 text-align:center;">{"Welcome To Insurance Premium Predator"}</h1>''', unsafe_allow_html=True)

	# Creating form field
	with st.form('form',clear_on_submit=True):
		age = st.text_input('Age',placeholder='Age')
		sex = st.selectbox("Sex",['Male','Female'])
		bmi = st.text_input('Bmi',placeholder='Bmi')
		children = st.text_input('Children',placeholder='Number of Children')
		smoker = st.selectbox('Smoker',['Yes','No'])
		reg = ['Northeast','Northwest','Southeast','Southwest']
		region = st.selectbox('Region',reg)

		st.markdown(""" <style> div.stButton > button:first-child {background-color:green;
			width:600px;color:white; margin: 0 auto; display: block;} </style>""", unsafe_allow_html=True)

		predict = st.form_submit_button("Predict Premium")

		if predict:

			X = pd.DataFrame([[int(age), sex, float(bmi), int(children), smoker, region]], 
	                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

			model = load_model()
			premium = model.predict(X)

			st.subheader(f'Premium: ${premium[0]:.2f}')


print(show_predict_page())
