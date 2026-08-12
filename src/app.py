from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Kalp Hastalığı Risk Tahmini",
    page_icon="❤️",
    layout="centered"
)

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "heart_disease_knn_final_model.joblib"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.title("❤️ Kalp Hastalığı Risk Tahmini")
st.write(
    "Bu uygulama, girilen klinik bilgilere göre kalp hastalığı risk tahmini yapar."
)
st.warning("Bu uygulama eğitim amaçlıdır; tıbbi teşhis yerine kullanılamaz.")

st.subheader("Hasta Bilgileri")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Yaş", min_value=20, max_value=100, value=55)
    sex = st.selectbox("Cinsiyet", ["Male", "Female"])
    cp = st.selectbox(
        "Göğüs Ağrısı Tipi",
        ["typical angina", "atypical angina", "non-anginal", "asymptomatic"]
    )
    trestbps = st.number_input(
        "Dinlenme Kan Basıncı", min_value=80.0, max_value=250.0, value=140.0
    )
    chol = st.number_input(
        "Kolesterol", min_value=100.0, max_value=600.0, value=250.0
    )

with col2:
    fbs = st.selectbox("Açlık Kan Şekeri Yüksek mi?", [False, True])
    restecg = st.selectbox(
        "EKG Sonucu",
        ["normal", "lv hypertrophy", "st-t abnormality"]
    )
    thalch = st.number_input(
        "Maksimum Kalp Atış Hızı", min_value=50.0, max_value=250.0, value=150.0
    )
    exang = st.selectbox("Egzersize Bağlı Anjina", [False, True])
    oldpeak = st.number_input(
        "ST Depresyonu (oldpeak)", min_value=0.0, max_value=10.0, value=2.0
    )

if st.button("Risk Tahmini Yap", type="primary"):
    patient = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalch": thalch,
        "exang": exang,
        "oldpeak": oldpeak
    }])

    prediction = model.predict(patient)[0]
    probability = model.predict_proba(patient)[0][1]

    st.divider()

    if prediction == 1:
        st.error("Tahmin: Kalp hastalığı riski var.")
    else:
        st.success("Tahmin: Kalp hastalığı riski düşük.")

    st.metric("Tahmini risk olasılığı", f"%{probability * 100:.1f}")