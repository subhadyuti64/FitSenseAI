import streamlit as st
import requests

st.title("👕 FitSense App")
st.write("Upload an image to detect if it's Casual, Elegant, or Sportswear.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Classify"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict", files=files)

        if response.status_code == 200:
            label = response.json()["prediction"]
            st.success(f"**Predicted Style:** {label.capitalize()}")
        else:
            st.error("Prediction failed. Check backend.")
