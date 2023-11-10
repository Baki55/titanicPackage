import pickle as pk
import numpy as np
from fastapi import FastAPI
import pandas as pd
import sklearn

def pred(Pclass, SibSp, Parch, Sex_female, Sex_male):
	user_data = {"Pclass": Pclass,
				"SibSp": SibSp,
				"Parch": Parch,
				"Sex_female": Sex_female,
				"Sex_male": Sex_male}
	predict_df = pd.DataFrame(user_data, index=[0])
	prediction = model.predict(predict_df)
	return prediction

with open("../titanicModel.pkl", "rb") as file:
	model = pk.load(file)

app = FastAPI()


@app.get('/')
def index():
	return {'ok': True}

@app.post('/predict')
async def read_item(Pclass: int = 1, SibSp: int = 0, Parch: int = 0, Sex_female: int = 0, Sex_male: int = 1):
	prediction = pred(Pclass, SibSp, Parch, Sex_female, Sex_male)
	return {"prediction" : int(prediction)}