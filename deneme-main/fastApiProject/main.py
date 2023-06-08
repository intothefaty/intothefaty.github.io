import numpy as np
from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware
import sklearn
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open('model.pkl', 'rb'))


@app.get("/predict/{patient_data}")
async def predict(patient_data: str):
    patient_data_list = patient_data.split(",")
    for idx, x in enumerate(patient_data_list):
        patient_data_list[idx] = int(x)

    features = np.array(patient_data_list)
    prediction = model.predict([features])
    result = prediction[0]
    print(result)
    print(type(result))
    print(features)
    return int(result)
