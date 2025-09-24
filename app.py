import streamlit as st
import pandas as pd
import joblib

model_components = joblib.load('final_model.pkl')
model = model_components['model']
scaler = model_components['scaler']
numerical_cols = model_components['numerical_cols']
selected_cols = model_components['selected_cols']

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction App")
st.write("Enter your health metrics below to predict the likelihood of heart disease.")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.slider("Resting Blood Pressure (trestbps)", 90, 200, 120)
    chol = st.slider("Serum Cholestoral in mg/dl (chol)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", [0, 1, 2])

with col2:
    thalach = st.slider("Maximum Heart Rate Achieved (thalach)", 70, 220, 150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.slider("ST depression induced by exercise (oldpeak)", 0.0, 6.2, 1.0)
    slope = st.selectbox("Slope of the peak exercise ST segment (slope)", [0, 1, 2])
    ca = st.selectbox("Number of major vessels colored by flourosopy (ca)", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (thal)", [1, 2, 3]) # Note: 0 is not a valid value in original dataset

if st.button("Predict", key="predict_button"):
    # 1. Create a DataFrame from user input with all original feature names
    input_data = pd.DataFrame({
        'age': [age], 'sex': [1 if sex == 'Male' else 0], 'cp': [cp], 'trestbps': [trestbps],
        'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach],
        'exang': [exang], 'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]
    })


    numerical_cols_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    input_data[numerical_cols_to_scale] = scaler.transform(input_data[numerical_cols_to_scale])

    categorical_cols_original = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
    input_encoded = pd.get_dummies(input_data, columns=categorical_cols_original)

    input_aligned = input_encoded.reindex(columns=selected_cols, fill_value=0)

    prediction = model.predict(input_aligned)
    prediction_proba = model.predict_proba(input_aligned)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error(f"High Risk of Heart Disease (Probability: {prediction_proba[0][1]:.2f})")
        st.write("Please consult a doctor for further evaluation.")
    else:
        st.success(f"Low Risk of Heart Disease (Probability: {prediction_proba[0][0]:.2f})")
        st.write("This is a good sign, but always maintain a healthy lifestyle.")
