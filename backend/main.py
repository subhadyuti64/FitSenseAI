from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from utils import load_model, predict_image

app = FastAPI()
model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    label = predict_image(image, model)
    return {"prediction": label}
