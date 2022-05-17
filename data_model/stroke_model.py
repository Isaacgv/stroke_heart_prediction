from types import TracebackType
from matplotlib.pyplot import table
from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    firstname : str
    lastname : str
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status:str