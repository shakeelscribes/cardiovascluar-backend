# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import os

# ─────────────────────────────────────
# 1. LOAD MODEL & SCALER
# ─────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model  = pickle.load(open('cardio_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

print("✅ Model loaded!")
print("✅ Scaler loaded!")
print(f"✅ Scaler expects {scaler.n_features_in_} features")

# ─────────────────────────────────────
# 2. FASTAPI APP
# ─────────────────────────────────────
app = FastAPI(
    title="CVD Prediction API",
    description="Cardiovascular Disease Early Risk Prediction",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────
# 3. INPUT STRUCTURE
# ─────────────────────────────────────
class PatientData(BaseModel):
    gender: int       # 1 = female, 2 = male
    age_years: float  # age in years  e.g. 45.0
    height: int       # cm
    weight: float     # kg
    ap_hi: int        # systolic  BP (mmHg)
    ap_lo: int        # diastolic BP (mmHg)
    cholesterol: int  # 1=normal  2=above normal  3=well above normal
    gluc: int         # 1=normal  2=above normal  3=well above normal
    smoke: int        # 0 / 1
    alco: int         # 0 / 1
    active: int       # 0 / 1


# ─────────────────────────────────────
# 4. HOME ENDPOINT
# ─────────────────────────────────────
@app.get("/")
def home():
    return {
        "status": "✅ CVD Prediction API running",
        "version": "2.0.0",
        "endpoint": "POST /predict"
    }


# ─────────────────────────────────────
# 5. PREDICTION ENDPOINT
# ─────────────────────────────────────
@app.post("/predict")
def predict(data: PatientData):
    print("📥 Received data:", data)
    try:
        # ── Derived features (must match training pipeline) ──
        bmi               = round(data.weight / (data.height / 100) ** 2, 2)
        pulse_pressure    = data.ap_hi - data.ap_lo
        mean_arterial_pressure = round((data.ap_hi + 2 * data.ap_lo) / 3, 2)

        # ── Feature order MUST match training (14 features) ──
        # age_years, gender, height, weight, bmi,
        # ap_hi, ap_lo, pulse_pressure, mean_arterial_pressure,
        # cholesterol, gluc, smoke, alco, active
        features = pd.DataFrame([[
            data.age_years,
            data.gender,
            data.height,
            data.weight,
            bmi,
            data.ap_hi,
            data.ap_lo,
            pulse_pressure,
            mean_arterial_pressure,
            data.cholesterol,
            data.gluc,
            data.smoke,
            data.alco,
            data.active
        ]], columns=[
            'age_years', 'gender', 'height', 'weight', 'bmi',
            'ap_hi', 'ap_lo', 'pulse_pressure', 'mean_arterial_pressure',
            'cholesterol', 'gluc', 'smoke', 'alco', 'active'
        ])

        # ── Gradient Boosting does NOT need scaling ──────────
        # scaler.transform() is intentionally skipped here.
        # The scaler.pkl is retained for reference / future models.
        prediction  = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        # ── BMI category ─────────────────────────────────────
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal"
        elif bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        # ── Risk level ────────────────────────────────────────
        if probability >= 0.7:
            risk_level = "High"
            risk_color = "red"
            advice = "Please consult a cardiologist immediately."
        elif probability >= 0.4:
            risk_level = "Medium"
            risk_color = "orange"
            advice = "Moderate risk. Schedule a checkup soon."
        else:
            risk_level = "Low"
            risk_color = "green"
            advice = "Low risk! Maintain a healthy lifestyle."

        return {
            "success": True,
            "prediction": int(prediction),
            "probability": round(float(probability) * 100, 2),
            "risk_level": risk_level,
            "risk_color": risk_color,
            "advice": advice,
            "bmi": bmi,
            "bmi_category": bmi_category,
            "derived": {
                "pulse_pressure": pulse_pressure,
                "mean_arterial_pressure": mean_arterial_pressure
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }