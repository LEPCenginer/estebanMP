from pydantic import BaseModel

class PatientData(BaseModel):
    firts_name: str
    last_name: str
    identification_number: str
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    diabetes_pedigree_function: float
    age: int

