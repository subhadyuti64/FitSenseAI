import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from torchvision.models import resnet18
import torch.nn as nn

class_names = ['casuals', 'elegante', 'sports']

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def load_model(path="backend/fitsense.pth"):
    model = resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 3)
    model.load_state_dict(torch.load(path, map_location='cpu'))
    model.eval()
    return model

def predict_image(image: Image.Image, model):
    img = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]

st.title("👕 FitSense - Simple Predictor")
st.write("Upload an image to detect if it's Casual, Elegant, or Sportswear.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    if st.button("Classify"):
        with st.spinner('Loading model and predicting...'):
            model = load_model()
            label = predict_image(image, model)
        st.success(f"**Predicted Style:** {label.capitalize()}") 