<div align="center">

# 🫀 CARDIO-GUARD BACKEND
### *High-Performance CVD Risk Inference Engine*

[![Engine: FastAPI](https://img.shields.io/badge/Engine-FastAPI-05998b?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Model: Scikit-Learn](https://img.shields.io/badge/Intelligence-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Deployment: Render](https://img.shields.io/badge/Deployment-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![Status: Operational](https://img.shields.io/badge/System_Status-Operational-00FF00?style=for-the-badge)]()

**Predicting the future of heart health through deterministic machine learning.**

[Access API Nodes](#-api-interface-map) • [Report Neural Anomaly](https://github.com/shakeelscribes/cardiovascluar-backend/issues) • [Project Overview](#-project-vision)

</div>

---

## 🌌 Project Vision

The **Cardio-Neural Backend** is a dedicated microservice engineered to bridge raw biometric telemetry with clinical-grade predictive intelligence. Built for the final year CVD Risk Prediction project at Nellai College of Engineering, this repository handles the heavy lifting of data normalization and algorithmic inference.

---

## 🛠 Technical Architecture

### 🧠 The Intelligence Layer
The core of this system utilizes serialized intelligence nodes to ensure sub-millisecond prediction latency:
* **`cardio_model.pkl`**: A pre-trained Random Forest Classifier optimized for high-dimensional biometric patterns.
* **`scaler.pkl`**: A Standardized Scaling Matrix that ensures input parity with the original training manifold.

### 🔌 Connectivity & Stack
* **FastAPI**: Asynchronous Python framework for high-concurrency biometric ingestion.
* **Uvicorn**: ASGI server implementation for lightning-fast request handling.
* **Scikit-Learn**: The underlying mathematical framework for the inference pipeline.

---

## 🚀 Deployment Protocol

### 1. Synchronize Repository
```bash
git clone https://github.com/shakeelscribes/cardiovascluar-backend.git
cd cardiovascluar-backend
```

### 2. Initialize Neural Environment

```bash
python -m venv env
# Unix/macOS
source env/bin/activate
# Windows
.\env\Scripts\activate

pip install -r requirements.txt
```

### 3. Launch Local Instance

```bash
uvicorn main:app --reload --port 8000
```

---

## 📡 API Interface Map

### **Predict Risk Profile**

`POST /predict`  
*Processes biometric vectors and returns a localized risk assessment.*

**Request Payload:**

```json
{
  "age": 23,
  "gender": 1,
  "systolic_bp": 120,
  "diastolic_bp": 80,
  "cholesterol": 1,
  "glucose": 1,
  "smoke": 0,
  "alcohol": 0,
  "active": 1,
  "bmi": 22.5
}
```

**System Response:**

```json
{
  "risk_score": 0.12,
  "classification": "Low Risk",
  "timestamp": "2026-04-19T18:19:55Z"
}
```

---

## 🏗 System Topology

```mermaid
graph LR
    A[Flutter/Next.js Client] -->|Biometric Payload| B(FastAPI Gateway)
    B --> C{Preprocessing Node}
    C -->|scaler.pkl| D[Feature Normalization]
    D --> E{Inference Engine}
    E -->|cardio_model.pkl| F[Risk Prediction]
    F -->|JSON Response| A

    style B fill:#05998b,stroke:#fff,color:#fff
    style E fill:#F7931E,stroke:#fff,color:#fff
```

---

## 👥 Engineering Collective

This system is maintained and developed by the **Nellai College of Engineering** core team:

* **Mohamed Shakeel** - *Lead Backend Architect*
* **Shabith Subair** - *Core Contributor*
* **Sri Thandapani** - *Core Contributor*
* **Mohamed Imran** - *Core Contributor*

---

<div align="center">

**[ ⚡ SYSTEM OPERATIONAL ]** *Designed for the future of preventive cardiology.*

</div>