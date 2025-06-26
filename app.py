from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle

# Load model
with open("liver_disease_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Mount static and template folders
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class PatientData(BaseModel):
    Age: int
    Gender: int
    BMI: float
    AlcoholConsumption: float
    Smoking: int
    GeneticRisk: int
    PhysicalActivity: float
    Diabetes: int
    Hypertension: int
    LiverFunctionTest: float

@app.post("/predict")
def predict(data: PatientData):
    features = [[
        data.Age, data.Gender, data.BMI, data.AlcoholConsumption, data.Smoking,
        data.GeneticRisk, data.PhysicalActivity, data.Diabetes,
        data.Hypertension, data.LiverFunctionTest
    ]]
    pred = model.predict(features)[0]
    return {"prediction": "Liver Disease" if pred == 1 else "No Liver Disease"}
