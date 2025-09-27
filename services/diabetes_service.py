import pickle

import numpy as np
from schemas.diabetes_schemas import PatientData

with open('RFDiabetesv132.pkl', 'rb') as file:
    model = pickle.load(file)

labels = ["sano", "enfermo"]

def diabetes_prediction(data: PatientData):
    xin = np.array([
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree_function,
        data.age
    ]).reshape(1, 8)
    prediction = model.predict(xin)
    print("prediction", prediction)
    return labels[prediction[0]]
                
                    
                    
                    